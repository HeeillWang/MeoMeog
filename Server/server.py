#! -*- coding: utf-8 -*-

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import MySQLdb
from urlparse import parse_qs
import time
# import RuleBased

DEBUG = True
ADDR = ""
PORT = 9999
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        spath = self.path[1:]
        
        pathinfo = spath.split('?')[0]
        
        print pathinfo
        
        if pathinfo == 'rulebased':
            if DEBUG :
                print ("Rule Based Algorithm request")
                
            # Do something
            # Make proper output with json format and write it into 'wfile'
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # get GET responses & parse it 
            data = parse_qs(self.path[1:].split('?')[1])
            if DEBUG:
                print data['data'][0]
            
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
        elif pathinfo == 'machinelearning':
            print ("Machine Learning Request")
            # Do something
            self.wfile.write("")
            
        else:
            print ("Wrong Path...")
            # Do something
            # Notice user that the path is wrong
            self.wfile.write("")



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
