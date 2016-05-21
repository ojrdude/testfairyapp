"""
Home page view.
"""

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os

import jinja2
import webapp2


class Home(webapp2.RequestHandler):
    """
    Request handling class for the home page view. Serves up dynamic
    content to the Jinja2 template
    """
    
    def get(self):
        """
        Handle a GET request.
        """
        template = VIEWS.get_template('home.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render({
                                             "output": "hello fairy kingdom",
                                              
                                             }))


application = webapp.WSGIApplication([('/', Home)], debug=True)

VIEWS = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()


