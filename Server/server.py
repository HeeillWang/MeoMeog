#! -*- coding: utf-8 -*-

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import MySQLdb
from urlparse import parse_qs
import time
import json
import cgi
# import RuleBased

DEBUG = True
ADDR = ""
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
            header = self.headers,
            environ = {'REQUEST_METHOD' :'POST'}
        )
        
        jsondata = form.getvalue['data']
        if DEBUG:
            print jsondata
        
        decode_json = json.load(jsondata)
        if DEBUG:
            print decode_json
        
        # get current local time of server
        now = time.localtime()
        date = "%d:%d:%d" % (now.tm_hour, now.tm_min, now.tm_sec)
        if DEBUG:
            print date
        
        # get restaurant information from database
        cur.execute("SELECT * FROM RestInfo")           # Send QUERY
        
        # Get result and put it into dictionary variable
        restinfo = []
        for row in cur.fetchall():
            tmp = dict()
            tmp['id'] = row[0]
            tmp['name'] = row[1]
            tmp['lat'] = row[2]
            tmp['long'] = row[3]
            tmp['rating'] = row[4]

            restinfo.append(tmp)
        if DEBUG:
            print restinfo
        
        # usrinfo = data
        # RuleBased.getRecommRest(usrinfo, date, restinfo)
        
        self.wfile.write("Rule Based Algorithm")
        
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
        restinfo = []
        for row in cur.fetchall():
            tmp = dict()
            tmp['id'] = row[0]
            tmp['name'] = row[1]
            tmp['lat'] = row[2]
            tmp['long'] = row[3]
            tmp['rating'] = row[4]

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
