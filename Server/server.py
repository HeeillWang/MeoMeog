#! -*- coding: utf-8 -*-

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import MySQLdb
from urlparse import parse_qs
import time
import json
import cgi
from pyowm import OWM
import sys

sys.path.insert(0, "/home/hsherlcok/CapstoneDesign/MeoMeog/Recommend_System")
import RuleBased

DEBUG = True
API_KEY = 'ae2341409b61ddcf60fa340321084b7e'
weather_mapping = {"clear sky": 0,
                   "few clouds": 0,
                   "scattered clouds": 1,
                   "broken clouds": 1,
                   "shower rain": 2,
                   "rain": 2,
                   "thunderstorm": 2,
                   "snow": 3,
                   "mist": 1 }

ADDR = "10.0.2.15"
PORT = 9999
class MyHandler(BaseHTTPRequestHandler):
    def _set_header(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def do_POST(self):
        self._set_header()
        
        form = cgi.FieldStorage(
            fp = self.rfile,
            headers = self.headers,
            environ = {'REQUEST_METHOD' :'POST'}
        )
        
        jsondata = form.getvalue('data')
        
        if DEBUG:
            print jsondata
        
        decode_json = json.loads(jsondata)
        
        if DEBUG:
            print decode_json
        # gender age kr ch meat soup jp fast flour chicken pizza noodle western sashimi pref_new_rest pref_dist 
        usr_input = []
        usr_input += [decode_json['gender'], decode_json['age'], decode_json['kr'], decode_json['ch'], decode_json['meat'], decode_json['soup'], decode_json['jp'], decode_json['fast'],
                         decode_json['flour'], decode_json['chicken'], decode_json['pizza'], decode_json['noodle'], decode_json['western'], decode_json['sashimi']
                         , decode_json['pref_new_rest'], decode_json['pref_dist']]
        
        if DEBUG:
            print usr_input
            
        # time weather lat long
        cur_input = []
        
        # get current local time of server
        # 0 - early lunch 1 - lunch 2 - late lunch 3 - early dinner 4 - dinner 5- late dinner
        now = time.localtime()
        curdate = "%d:%d" % (now.tm_hour, now.tm_min)
        
        curdate = curdate.split(':')
        if len(curdate[1]) == 1:
            curdate[1] = '0' + curdate[1]
            
        curdate = curdate[0] + curdate[1]
        curdate = int(curdate)
        
        if DEBUG:
            print curdate
            
        cur_input.append(curdate)
        
        # get current weather stat and mapping
        # 0 - clear 1 - cloudy 2 - rain 3 - snow
        owm = OWM(API_KEY)
        obs = owm.weather_at_coords(decode_json['lat'], decode_json['long'])
        w = obs.get_weather()
        stat = w.get_detailed_status()
        temp = w.get_temperature(unit='celsius')
        
        if DEBUG:
            print stat
            print temp
            print type(temp)
            
        temp = temp['temp']
        
        weather = weather_mapping[stat]
        cur_input.append(weather)
            
        cur_input.append(decode_json['lat'])
        cur_input.append(decode_json['long'])
        cur_input.append(temp)
        
        if DEBUG:
            print cur_input
        
        # get restaurant information from database
        cur.execute("SELECT * FROM RestInfo")           # Send QUERY
        
        # Get result and put it into dictionary variable
        restinfo = []
        for row in cur.fetchall():
            tmp = dict()
            tmp['id'] = row[0]
            tmp['name'] = row[1]
            tmp['category'] = row[8]
            tmp['latitude'] = row[2]
            tmp['longitude'] = row[3]
            tmp['globalRate'] = row[4]
            tmp['userRate'] = row[5]
            tmp['startTime'] = row[6]
            tmp['endTime'] = row[7]

            restinfo.append(tmp)
        
        usr_parse, cur_parse, rest_parse = RuleBased.parse(usr_input, cur_input, restinfo)
        
        if DEBUG:
            print ("Parsing Data...")
            print usr_parse
            print cur_parse
        
        RuleBased.loadWeightAndSaveToRest(rest_parse)
        restarr = RuleBased.getRecommRest(usr_parse, cur_parse, rest_parse)
        
        # if DEBUG:
        #    RuleBased.accuraccy_test(rest_parse)
            
        if DEBUG:
            print ("Recommened Restaurant")
            print restarr
        
        restdict = {}
        rank = []
        tmp = {}
        tmp["1name"] = restarr[0].name
        tmp["1cat"] = restarr[0].getCategory();
        tmp["1score"] = restarr[0].getScore()
        rank.append(tmp)
        
        tmp = {}
        tmp["2name"] = restarr[1].name
        tmp["2cat"] = restarr[1].getCategory();
        tmp["2score"] = restarr[1].getScore()
        rank.append(tmp)
        
        tmp = {}
        tmp["3name"] = restarr[2].name
        tmp["3cat"] = restarr[2].getCategory();
        tmp["3score"] = restarr[2].getScore()
        rank.append(tmp)
            
        restdict['rank'] = rank
        resultStr = json.dumps(restdict)
        
        if DEBUG:
            print "Result String"
            print resultStr
                
        self.wfile.write(str(resultStr))

if __name__ == '__main__':

    
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         passwd="1234",
                         db="CapstoneDesign")

    cur = db.cursor()       # Cursor to execute queries.
    
    '''
    To send SQL Queries
    Use this
    
    cur.execute("SELECT * FROM [MY_TALBE_NAME]")
    '''
    
    # Server Connection Part
    server = HTTPServer((ADDR, PORT), MyHandler)
    print "Started WebServer on port", PORT
    print "Press ^C to quit..."

    server.serve_forever()       # Activate the server
