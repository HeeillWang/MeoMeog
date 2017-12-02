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
    # notice that it does not do square root opeartion
    def setDistance(self, cur_latitude, cur_longitude):
        self.distance = (cur_latitude - self.latitude) * (cur_latitude - self.latitude) + (cur_longitude - self.longitude) * (cur_longitude - self.longitude)


# parse data(from server) -> to our class(preference, userInput, curInput, restInfo)
# if might be not needed
# class parseToClass:
