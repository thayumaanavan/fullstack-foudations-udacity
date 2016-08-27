from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import cgi
import database_read

class webserverHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('content-type','text/html')
                self.end_headers()
                restaurantList=database_read.list_all()    
                output=""
                output +="<html><body>"
                for restaurant in restaurantList:
                    output += restaurant.name+"</br>"

                self.wfile.write(output)
                print output
                return
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('content-type','text/html')
                self.end_headers()

                output=""
                output +="<html><body>&#161 Hola <a href='/hello'>Back to Hello</a>"
                output +="<form method='POST' enctype='multipart/form-data' action='/hello'>\
                Enter something:<input name='message' type='text'> <input type='submit' value='Submit'>\
                </form>"
                output+="</body></html>"
                self.wfile.write(output)
                print output
                return
        except IOError as identifier:
            self.send_error(404,"File not found %s" % self.path)
    
    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()

            ctype,pdict=cgi.parse_header(self.headers.getheader('content-type'))
            if ctype=='multipart/form-data':
                fields=cgi.parse_multipart(self.rfile,pdict)
                messagecontent=fields.get('message')

            output=""
            output += "<html><body>"
            output += "%s" %messagecontent[0]
            output +="<form method='POST' enctype='multipart/form-data' action='/hello'>\
                Enter something:<input name='message' type='text'> <input type='submit' value='Submit'>\
                </form>"
            output+="</body></html>"
            self.wfile.write(output)
            print output

        except:
            pass








def main():
    try:
        port=8080
        server=HTTPServer(('',port),webserverHandler)
        print "webserver running on port %s" %port
        server.serve_forever()

    except KeyboardInterrupt:
        print "Stopping web server.."
        server.socket.close()


if __name__=='__main__':
    main()