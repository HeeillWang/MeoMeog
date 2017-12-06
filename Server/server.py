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
            
        if curdate < 1100:
            date = 0
        elif curdate < 1400:
            date = 1
        elif curdate < 1600:
            date = 2
        elif curdate < 1800:
            date = 3
        elif curdate < 2000:
            date= 4
        else:
            date = 5
            
        cur_input.append(date)
        
        # get current weather stat and mapping
        # 0 - clear 1 - cloudy 2 - rain 3 - snow
        owm = OWM(API_KEY)
        obs = owm.weather_at_coords(decode_json['lat'], decode_json['long'])
        w = obs.get_weather()
        stat = w.get_status()
        
        if DEBUG:
            print stat
        
        weather = weather_mapping.get(stat)
        cur_input.append(weather)
        
        cur_input.append(decode_json['lat'])
        cur_input.append(decode_json['long'])
        
        # get restaurant information from database
        cur.execute("SELECT * FROM RestInfo")           # Send QUERY
        
        # Get result and put it into dictionary variable
        restinfo = []
        for row in cur.fetchall():
            tmp = dict()
            tmp['id'] = row[0]
            tmp['name'] = row[1]
            tmp['category'] = row[10]
            tmp['latitude'] = row[2]
            tmp['longitude'] = row[3]
            tmp['rating'] = row[4]
            tmp['globalRate'] = row[6]
            tmp['userRate'] = row[7]
            tmp['startTime'] = row[8]
            tmp['endTime'] = row[9]

            restinfo.append(tmp)
            
        if DEBUG:
            print restinfo
        
        usr_parse, cur_parse, rest_parse = RuleBased.parse(usr_input, cur_input, restinfo)
        
        if DEBUG:
            print usr_parse
            print cur_parse
            print rest_parse
            
        restarr = RuleBased.getRecommRest(usr_parse, cur_parse, rest_parse)
        if DEBUG:
            print restarr
            
        self.wfile.write(str(restarr))
        
    def do_GET(self):
        spath = self.path[1:]
        
        pathinfo = spath.split('?')[0]
        
        print pathinfo
        
        # Do something
        # Make proper output with json format and write it into 'wfile'
        self._set_header()
        
        """
        # get GET responses & parse it 
        # {"soup":3,"chicken":3,"gender":"M","ch":3,"pref_dist":4
        # "jp":3,"pref_new_rest":4,"kr":3,"noodle":3,"long":36.24
        # "fast":3,"pizza":3,"flour":3,"meat":3,"sashimi":3,"western":3,"age":25,"lat":126.1234}
        data = parse_qs(self.path[1:].split('?')[1])
        gender = data['gender']
        ch = data['ch']
        soup = data['soup']
        chicken = data['chicken']
        pref_dist = data['pref_dist']
        jp = data['jp']
        pref_new_rest = data['pref_new__rest']
        kr = data['kr']
        noodle = data['noodle']
        longitute = data['long']
        fast = data['fast']
        pizza = data['pizza']
        flour = data['flour']
        meat = data['meat']
        sashimi = data['sashimi']
        western= data['western']
        age = data['age']
        latitute = data['lat']
        """
        
        # get current local time of server
        now = time.localtime()
        date = "%d:%d:%d" % (now.tm_hour, now.tm_min, now.tm_sec)
        if DEBUG:
            print date
        
        # get restaurant information from database
        cur.execute("SELECT * FROM RestInfo")           # Send QUERY
        
        # Get result and put it into dictionary variable
        # 7 globalRate 8 userRate 9 startTime 10 endTime
        restinfo = []
        for row in cur.fetchall():
            tmp = dict()
            tmp['id'] = row[0]
            tmp['name'] = row[1]
            tmp['category'] = row[11]
            tmp['lat'] = row[2]
            tmp['long'] = row[3]
            tmp['rating'] = row[4]
            tmp['globalRate'] = row[7]
            tmp['userRate'] = row[8]
            tmp['startTime'] = row[9]
            tmp['endTime'] = row[10]

            restinfo.append(tmp)
        if DEBUG:
            print restinfo
        
        # usrinfo = data
        # RuleBased.getRecommRest(usrinfo, date, restinfo)
        self.wfile.write("Rule Based Algorithm")

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
