#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

## IMPORTS ##
import jinja2
import os
import webapp2
from google.appengine.ext import ndb

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(template_dir))

## FUNCTIONS and VARS ##
names = ['Diane', 'Danica', 'Danielle', 'Glenda', 'Leon']
msg = {}

def everyone_sign():
	for i in range(0, len(names)):
		if i == 0:
			msg[names[i]] = "Thank you! Your friends: " + ", ".join(names[i+1:len(names)])
		else:
			msg[names[i]] = "Thank you! Your friends: " + ", ".join(names[0:i]) + ", " + ", ".join(names[i+1:len(names)])	

## HANDLERS ##
class MainHandler(webapp2.RequestHandler):
    def get(self):
    	everyone_sign()
    	template = jinja_environment.get_template('index.html')
    	for i in range(0,len(names)):	
    		html = (template.render({'receiver':names[i], 'message':msg[names[i]]}))
       		self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
