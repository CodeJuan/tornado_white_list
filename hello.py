import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello, world")
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("temp.html", title="My title", items=items)

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html", title="login")
    def post(self):
        usr=self.get_argument("username", "") 
        pwd=self.get_argument("password", "") 
        self.write(usr)
        self.write(pwd)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/login", LoginHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
