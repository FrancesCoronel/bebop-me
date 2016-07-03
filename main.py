# [START imports]
import os
import urllib

import jinja2
import webapp2

from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

################################ IGNORE: START ################################
# This statement will cause jinja to look for templates in the 'templates'
# directory.
jinja = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), 'templates')))


# Helper function; you probably don't want to use this directly.
def TemplateString(template_name, template_values):
  t = jinja.get_template(template_name)
  return t.render(template_values)


# Helper function; you probably don't want to use this directly.
def Template(template_name, template_values, output_stream):
  output_stream.write(TemplateString(template_name, template_values))

################################# IGNORE: END #################################

# Writes the given text to the response. Use to display simple text
# on the page.
#
# Example:
#   render.Text('Hello, world!!', self.response)
def TextResponse(text, response):
  response.out.write(text)


# Executes the provided template text and writes the resulting string to the
# provided output stream. In this function, the template text is a string
# rather than reading it from a file.
#
# Example:
#    template = 'Hello, {{name}}'
#    template_values = {'name': 'Sabrina'}
#    render.TemplateText(template, template_values, self.response)
def TextTemplateResponse(template_string, template_values, response):
  t = jinja.from_string(template_string)
  response.out.write(t.render(template_values))

# Looks in the templates folder for a file with the name provided in template_name.
# The template gets executed with the given template_values and writes the resulting
# string out to the given response object.
#
# Example:
#    template_values = {
#        'key1': 'value1',
#        'key2': 'value2'
#    }
#    render.TemplateResponse('home.html', template_values, self.response)
def TemplateResponse(template_name, template_values, response):
  Template(template_name, template_values, response.out)

# [END imports]

# class Marker(ndb.Model):
# 	title = ndb.StringProperty(required=True)
# 	latitude = ndb.FloatProperty(required=True)
# 	longitude = ndb.FloatProperty(required=True)

class MainPage(webapp2.RequestHandler):

	def get(self):

		# """
		# markers = [
	 	#  	Marker(title="A", latitude=-25, longitude=131),
		#   Marker(title="B", latitude=-26, longitude=130),
		#   Marker(title="C", latitude=-24, longitude=132),
		#   Marker(title="D", latitude=-25.5, longitude=131.5),
		#   Marker(title="E", latitude=-24.5, longitude=130.5)
		# ]
		# """
		# markers = Marker.query()

		template = JINJA_ENVIRONMENT.get_template('index.jsp')
		TemplateResponse(template, {'results': ""}, self.response)
		#self.response.write(template.render())

class Characters(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('characters.html')
		TemplateResponse(JINJA_ENVIRONMENT.get_template('characters.html'), {'results': ""}, self.response)

# class AddMarker(webapp2.RequestHandler):
# 	def get(self):
# 		TemplateResponse(JINJA_ENVIRONMENT.get_template('addmarker.html'), {'results': ""}, self.response)
# 	def post(self):
# 		Marker(
# 			title=self.request.get("title"),
# 			latitude=float(self.request.get("latitude")),
# 			longitude=float(self.request.get("longitude"))).put()
# 		TemplateResponse(JINJA_ENVIRONMENT.get_template('addmarker.html'), {'results': "SUCCESS"}, self.response)

# class GetReady(webapp2.RequestHandler):
# 	def get(self):
# 		template = JINJA_ENVIRONMENT.get_template('getready.html')
# 		TemplateResponse(JINJA_ENVIRONMENT.get_template('getready.html'), {'results': ""}, self.response)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/characters', Characters)
], debug=True)