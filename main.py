import json
import webapp2
import os
import jinja2
import random
import time
import urllib



from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import urlfetch

url = 'https://app.ticketmaster.com/discovery/v2/events.json?classificationName=music&dmaId=324&apikey=zjreZ4GpbxN2WwZfOOKPooZF2FkTrZKe'
fetch_result = urlfetch.fetch(url)    #retrieves api
fetch_content = json.loads(fetch_result.content)  #loads json
api_event_list = fetch_content['_embedded']['events']  #retrieves the list of events


jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

app = webapp2.WSGIApplication([
    ('/eventlist', EventListHandler),
    ('/emaillist', EmailListHandler),
    ('/', HomePageHandler),
    ('/makeuser', MakeUser),
    ('/aboutus', About)
], debug=True)
