# -*- coding: utf-8 -*-
import webapp2
import logging
import webapp2_extras.routes


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('hello')

routes = [ webapp2.Route('/', MainHandler, 'home')]

app = webapp2.WSGIApplication(routes)
#app.error_handlers[404] = handle_404
#app.error_handlers[500] = handle_500

