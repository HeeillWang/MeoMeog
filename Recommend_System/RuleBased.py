import  numpy as np

#preference of food
#this class will be part of class userInput
class preference:
    #same order as in survey
    def __init__(self, korean, chinese, meat, soup, japanese, fastfood, flour, chicken, pizza, noodle, western, sashimi):
        self.korean = korean
        self.chinese = chinese
        self.meat = meat
        self.soup = soup
        self.japanese = japanese
        self.fastfood = fastfood
        self.flour = flour
        self.chicken = chicken
        self.pizza = pizza
        self.noodle = noodle
        self.western = western
        self.sashimi = sashimi


class userInput:
    #same order as in survey
    def __init__(self, gender, age, preference, pref_for_new_rest, pref_for_distance):
        self.gender = gender
        self.age = age
        self.preference = preference
        self.pref_for_new_rest = pref_for_new_rest
        self.pref_for_distance = pref_for_distance


class curInput:
    # same order as in survey
    def __init__(self, time, weather, latitude, longitude):
        self.time = time
        self.weather = weather
        self.latitude = latitude
        self.longitude = longitude


class restInfo:
    # same order as in restaurant information
    def __init__(self, name, category, latitude, longitude, rate, startTime, endTime):
        self.name = name
        self.category = category
        self.latitude = latitude
        self.longitude = longitude
        self.rate = rate
        self.startTime = startTime
        self.endTime = endTime

    # it calculate square of distance
    # notice that it does not do square root operation
    def setDistance(self, cur_latitude, cur_longitude):
        self.distance = (cur_latitude - self.latitude) * (cur_latitude - self.latitude) + (cur_longitude - self.longitude) * (cur_longitude - self.longitude)

    # weights is list of weight about this restaurant.
    # for example : weight for distance, weight for preference of category... etc.
    # it might be more efficient to use dictionary not a list.
    def setWeight(self, weights):
        self.weight = weights



# parse data(from server) -> to our class(preference, userInput, curInput, restInfo)
# if might be not needed
# class parseToClass:



# argument : list of 'restInfo' objects.
# load weights from csv file and then save it to restInfo
# it must ensure that order of restaurants are same.
# returns : list of 'restInfo' objects.
def loadWeightAndSaveToRest(rest_arr):
    # skip first row
    data = np.loadtxt("weight.csv", delimiter=",", dtype=np.float32, skiprows=1)

    # need to inspect this part : "how to define weights? on each restaurants or globally?"
    #for i in range(1, data.size):
    #    rest_arr[i].setWeight(data[i])

    return rest_arr


# need to write this method
def getRecommRest(usrinfo, date, restinfo):
    print('nothing yet')