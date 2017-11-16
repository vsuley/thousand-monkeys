import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Placeholder for Thousand Monkeys,' 
            + ' a Python based genetic programming application.')


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)