import json
import webapp2
import os
import jinja2
import random
import time
import urllib
import googlemaps
import sys
import urllib2
import math

sys.path.insert(1, '/Users/<username>/google-cloud-sdk/platform/google_appengine')
sys.path.insert(1, '/Users/<username>/google-cloud-sdk/platform/google_appengine/lib/yaml/lib')
sys.path.insert(1, 'lib')
#stackoverflow shenanigans to fix the path
if 'google' in sys.modules:
    del sys.modules['google']

#from google.appengine.api import users
#from google.appengine.ext import ndb
#from google.appengine.api import urlfetch

url = 'https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=[uyourkeyhere]'
fetch_result = urllib2.urlopen(url)    #retrieves api
damn = fetch_result.read()
print damn
fetch_content = json.loads(damn)  #loads json
print(fetch_content)
api_directions = fetch_content['routes'][0]['legs'][0]['steps'] #retrieves the list of events
directions = []
for i in range(len(api_directions)):
    if 'maneuver' in  api_directions[i]:
        x = api_directions[i]['maneuver']
        if x == 'merge':
            directions.append(api_directions[i]['end_location'])
lat = directions[0]['lat'] * 1.0
lng = directions[0]['lng'] * 1.0

while len(directions) > 0:

    rlat = directions[0]['lat'] * 1.0
    rlng = directions[0]['lng'] * 1.0

    delX = math.cos(rlat) * math.cos(rlng) - math.cos(lat) * math.cos(lng)
    delY = math.cos(rlat) * math.sin(rlng) - math.cos(lat) * math.sin(lng)
    delZ = math.sin(rlat)  - math.sin(lat)
    C = math.sqrt((delX)**2 + (delY)**2 + (delZ)**2)
    if(C <= 25):
        print('merge')
        directions.pop(0)
    if (len(directions) != 0):
        lat = directions[0]['lat'] * 1.0
        long = directions[0]['lng'] * 1.0

# jinja_current_directory = jinja2.Environment(
#     loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
#     extensions=['jinja2.ext.autoescape'],
#     autoescape=True)

# app = webapp2.WSGIApplication([
#     ('/eventlist', EventListHandler),
#     ('/emaillist', EmailListHandler),
#     ('/', HomePageHandler),
#     ('/makeuser', MakeUser),
#     ('/aboutus', About)
# ], debug=True)
