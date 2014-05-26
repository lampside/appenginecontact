import os
import webapp2
import jinja2
import cgi
from google.appengine.api import mail

jinja_environment = jinja2.Environment(autoescape=True,
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "html")))
	
class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template("index.html")
		self.response.out.write(template.render())