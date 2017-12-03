import  numpy as np

#preference of food
#this class will be part of class userInput
class preference:
    #same order as in survey
    def __init__(self, korean, chinese, meat, soup, japanese, fastfood, flour, chicken, pizza, noodle, western, sashimi):
        self.korean = self.normalizer(korean)
        self.chinese = self.normalizer(chinese)
        self.meat = self.normalizer(meat)
        self.soup = self.normalizer(soup)
        self.japanese = self.normalizer(japanese)
        self.fastfood = self.normalizer(fastfood)
        self.flour = self.normalizer(flour)
        self.chicken = self.normalizer(chicken)
        self.pizza = self.normalizer(pizza)
        self.noodle = self.normalizer(noodle)
        self.western = self.normalizer(western)
        self.sashimi = self.normalizer(sashimi)

    def normalizer(pref):
        if pref >= 3:
            pref = pref + 5

        pref = pref / 10
        return pref


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

    def addScore(self, addValue):
        self.score = self.score + addValue

    def getScore(self):
        return self.score


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

    # need more code!
    return 0

if __name__ == "__main__":
    #test
