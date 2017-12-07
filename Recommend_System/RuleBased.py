import  numpy as np

#preference of food
#this class will be part of class userInput

class preference:
    #same order as in survey
    def __init__(self, korean, chinese, meat, soup, japanese, fastfood, flour, chicken, pizza, noodle, western, sashimi):
        self.prefList = []
        self.prefList.append(self.normalizer(korean))
        self.prefList.append(self.normalizer(chinese))
        self.prefList.append(self.normalizer(meat))
        self.prefList.append(self.normalizer(soup))
        self.prefList.append(self.normalizer(japanese))
        self.prefList.append(self.normalizer(fastfood))
        self.prefList.append(self.normalizer(flour))
        self.prefList.append(self.normalizer(chicken))
        self.prefList.append(self.normalizer(pizza))
        self.prefList.append(self.normalizer(noodle))
        self.prefList.append(self.normalizer(western))
        self.prefList.append(self.normalizer(sashimi))

    def normalizer(self, pref):
        if pref >= 3:
            pref = pref + 5

        pref = pref / 10
        return pref

    def getPreference(self, num):
        return self.prefList[num]


class userInput:
    #same order as in survey
    def __init__(self, gender, age, preference, pref_for_new_rest, pref_for_distance):
        self.gender = gender
        self.age = age
        self.preference = preference
        self.pref_for_new_rest = self.normalizer(pref_for_new_rest)
        self.pref_for_distance = self.normalizer(pref_for_distance)

    def normalizer(self, pref):
        return pref / 5


class curInput:
    # same order as in survey
    def __init__(self, time, weather, latitude, longitude, temperature):
        self.time = time
        self.weather = weather
        self.latitude = latitude
        self.longitude = longitude
        self.temperature = temperature

    def getPosition(self):
        return (self.latitude, self.longitude)

    def getTime(self):
        return self.time


class restInfo:
    # same order as in restaurant information
    def __init__(self, name, category, latitude, longitude, globalRate, userRate, startTime, endTime):
        self.name = name
        self.category = category
        self.latitude = latitude
        self.longitude = longitude
        self.globalRate = globalRate
        self.userRate = userRate
        self.startTime = startTime
        self.endTime = endTime
        self.score = 0

    # it calculate square of distance
    # notice that it does not do square root operation
    def setDistance(self, position, norm):
        if norm == -1:
            self.distance = (position[0] - self.latitude) * (position[0] - self.latitude) + (position[1] - self.longitude) * (position[1] - self.longitude)
        else:
            self.distance = norm

    # weights is list of weight about this restaurant.
    # for example : weight for distance, weight for preference of category... etc.
    # it might be more efficient to use dictionary not a list.
    def setWeight(self, weights):
        self.weight = weights

    def getCategory(self):
        return self.category

    def getDistance(self):
        return self.distance

    def setScore(self, setter):
        self.score = setter

    def addScore(self, addValue):
        self.score = self.score + addValue

    def getScore(self):
        return self.score

    def getWeight(self):
        return self.weight

    def getUserRate(self):
        return self.userRate

    def getGlobalRate(self):
        return self.globalRate

    def getTime(self):
        return (self.startTime, self.endTime)



# parse data(from server) -> to our class(preference, userInput, curInput, restInfo)
# argument
# user_input : list
# cur_infor : list
# rest_info : list of dictionary => need to inspect later
def parse(user_input, cur_info, rest_info):
    pref = preference(user_input[2], user_input[3], user_input[4], user_input[5], user_input[6], user_input[7], user_input[8], user_input[9], user_input[10], user_input[11], user_input[12], user_input[13])
    user = userInput(user_input[0], user_input[1], pref, user_input[14], user_input[15])
    cur = curInput(cur_info[0], cur_info[1], cur_info[2], cur_info[3], cur_info[4])
    rest = []

    #name, category, latitude, longitude, globalRate, userRate, startTime, endTime
    for i in range(len(rest_info)):
        rest.append(restInfo(rest_info[i]['name'], rest_info[i]['category'], rest_info[i]['latitude'], rest_info[i]['longitude'], rest_info[i]['globalRate'], rest_info[i]['userRate'], rest_info[i]['startTime'], rest_info[i]['endTime']))

    return user, cur, rest




# argument : list of 'restInfo' objects, current user data, current data
# load weights from csv file and then save it to restInfo
# it must ensure that order of restaurants are same.
# call first this function
# returns : list of 'restInfo' objects.
def loadWeightAndSaveToRest(rest_arr):
    # skip first row
    data = np.loadtxt("/home/hsherlcok/CapstoneDesign/MeoMeog/Recommend_System/weight.csv", delimiter=",", dtype=np.float32, skiprows=1)
    #data = np.loadtxt("weight.csv", delimiter=",", dtype=np.float32, skiprows=1)

    for rest in rest_arr:
        rest.setWeight(data[rest.getCategory()])

    return rest_arr


# need to write this method
# call next this function. distance setting contain this function
# return output vector
def getRecommRest(usrinfo, curinfo, rest_arr):
    # set distance
    for rest in rest_arr:
        rest.setDistance(curinfo.getPosition(), -1)


    preference = usrinfo.preference

    # distance normalize
    minDist = rest_arr[0].getDistance()
    maxDist = rest_arr[0].getDistance()

    for rest in rest_arr:
        if minDist > rest.getDistance():
            minDist = rest.getDistance()

        if maxDist < rest.getDistance():
            maxDist = rest.getDistance()

    distDiff = maxDist - minDist
    if distDiff == 0:
        distDiff = 1

    for rest in rest_arr:
        rest.setDistance((0, 0), (rest.getDistance() - minDist) / distDiff)
        rest.addScore(rest.getWeight()[rest.getCategory()] * preference.getPreference(rest.getCategory()))
        rest.addScore(rest.getWeight()[12] * rest.getUserRate())
        rest.addScore(rest.getWeight()[13] * rest.getGlobalRate())

        # changed this line, need inspection later
        rest.addScore(rest.getWeight()[14] * -rest.getDistance() * (1 - 0.5 * usrinfo.pref_for_distance))
        # weather
        # time
        # temperature
        # if out of service time, flush that restaurant's score -1
        if (curinfo.getTime() < rest.getTime()[0]) or (curinfo.getTime() > rest.getTime()[1]):
            if rest.getTime()[0] == -1:
                continue
            else:
                rest.setScore(-1)

    rest_arr = sorted(rest_arr, key=lambda restInfo:restInfo.score, reverse=True)


    return rest_arr[0:3]



def init_score(rest_arr):
    for i in range(len(rest_arr)):
        rest_arr[i].setScore(0)

def accuraccy_test(rest_arr):
    data = np.loadtxt('survey.csv', delimiter=',',dtype=np.float32)

    correct_y = 0 # no. of correct 'yes'
    correct_n = 0 # no. of correct 'no'
    count_y = 0 # counter for yes
    count_n = 0 # counter for no
    
    for i in range(len(data)):
        cur_data = [data[i][16], data[i][17], data[i][19], data[i][20], data[i][18]]
        user_input, cur_input, _ = parse(data[i][0:16], cur_data, [])

        init_score(rest_arr)
        result = getRecommRest(user_input, cur_input, rest_arr)
        ans = data[i][21]

        if(data[i][22] == 1):
            # survey respond is 'yes'
            for j in range(len(result)):
                count_y += 1
                if (ans == result[j].name):
                    correct_y += 1
        else:
            # survey respond is 'no'
            for j in range(len(result)):
                count_n += 1
                if (ans == result[j].name):
                    break;

            if(j == len(result)):
                correct_n += 1

    print("[yes] Correct : ", correct_y, " / total : ", count_y)
    print("[no] Correct : ", correct_n, " / total : ", count_n)







if __name__ == "__main__":
    # test code
    pref = preference(4, 4, 5, 3, 5, 4, 3, 5, 5, 4, 5, 2)
    user = userInput(1, 21, pref, 2, 4)
    cur = curInput(1544, 0, 37.293959, 126.974855, 20)
    rest = []
    rest.append(restInfo(1, 4, 37.297195, 126.971490, 4.6, 3.0, 1100, 2100))
    rest.append(restInfo(2, 5, 37.297716, 126.973346, 4.0, 3.0, 1100, 2100))

    loadWeightAndSaveToRest(rest)
    result = []
    result = accuraccy_test(rest)

    for restaurant in rest:
        print(restaurant.getScore())