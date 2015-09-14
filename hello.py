import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write("Hello, world")
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("temp.html", title="My title", items=items)

class LoginHandler(tornado.web.RequestHandler):
    file_name = "ip.txt"
    FILE = None

    def get(self):
        self.render("login.html", title="login")

    def post(self):
        usr=self.get_argument("username", "") 
        #pwd=self.get_argument("password", "") 
        self.write("Your IP have been added to the white list\n"+usr)
        self.WriteIP(usr)

    def WriteIP(self,ip):
        self.FILE = open(self.file_name, "w") 
        self.FILE.writelines(ip)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/login", LoginHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
