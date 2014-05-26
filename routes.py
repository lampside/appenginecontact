import webapp2
from webapp2_extras.routes import RedirectRoute

_routes = [
	RedirectRoute('/', 'handlers.MainHandler', name='main', strict_slash=True),
]