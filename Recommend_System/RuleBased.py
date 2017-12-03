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

    def normalizer(pref):
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

    def normalizer(pref):
        return pref / 5


class curInput:
    # same order as in survey
    def __init__(self, time, weather, latitude, longitude):
        self.time = time
        self.weather = weather
        self.latitude = latitude
        self.longitude = longitude

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
        if norm == 0:
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
# if might be not needed
# class parseToClass:


# argument : list of 'restInfo' objects, current user data, current data
# load weights from csv file and then save it to restInfo
# it must ensure that order of restaurants are same.
# call first this function
# returns : list of 'restInfo' objects.
def loadWeightAndSaveToRest(rest_arr):
    # skip first row
    data = np.loadtxt("weight.csv", delimiter=",", dtype=np.float32, skiprows=1)

    for rest in rest_arr:
        rest.setWeight(data[rest.getCategory()])

    return rest_arr


# need to write this method
# call next this function. distance setting contain this function
# return output vector
def getRecommRest(preference, usrinfo, curinfo, rest_arr):
    # set distance
    for rest in rest_arr:
        rest.setDistance(curinfo.getPosition())

    # distance normalize
    minDist = rest_arr[0].getDistance()
    maxDist = rest_arr[0].getDistance()

    for rest in rest_arr:
        if minDist > rest.getDistance():
            minDist = rest.getDistance()

        if maxDist < rest.getDistance():
            maxDist = rest.getDistance()

    distDiff = maxDist - minDist

    for rest in rest_arr:
        rest.setDistance((0, 0), (rest.getDistance() - minDist) / distDiff)
        rest.addScore(rest.getWeight()[rest.getCategory()] * preference.getPreference(rest.getCategory()))
        rest.addScore(rest.getWeight()[12] * rest.getUserRate())
        rest.addScore(rest.getWeight()[13] * rest.getGlobalRate())
        rest.addScore(rest.getWeight()[14] * rest.getDistance())
        # weather
        # time
        # temperature
        # if out of service time, flush that restaurant's score -1
        if (curinfo.gettime() < rest.getTime()[0]) or (curinfo.gettime() > rest.getTime()[1]):
            rest.setScore(-1)

    return rest_arr

if __name__ == "__main__":
    print("test")