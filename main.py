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

sys.path.insert(1, '/Users/<username>/google-cloud-sdk/platform/google_appengine')
sys.path.insert(1, '/Users/<username>/google-cloud-sdk/platform/google_appengine/lib/yaml/lib')
sys.path.insert(1, 'lib')
#stackoverflow shenanigans to fix the path
if 'google' in sys.modules:
    del sys.modules['google']

#from google.appengine.api import users
#from google.appengine.ext import ndb
#from google.appengine.api import urlfetch

url = 'https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key=[urkeylul]'
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


print(directions)



while len(directions)>0:
    [my directions]
    [the api which gives distance between two pairs of lat, lng] <= 100:
        print('merge')
        directions.pop(0)
    



class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        pass

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# app = webapp2.WSGIApplication([
#     ('/eventlist', EventListHandler),
#     ('/emaillist', EmailListHandler),
#     ('/', HomePageHandler),
#     ('/makeuser', MakeUser),
#     ('/aboutus', About)
# ], debug=True)
