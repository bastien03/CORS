#!/usr/bin/env python3

from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import json

class MyRequestHandler (BaseHTTPRequestHandler) :

    def do_GET(self) :

        #send response code:
        self.send_response(200)

        if self.path == "/cors" :
            #send headers:
            self.send_header("Access-Control-Allow-Origin", "http://localhost:9000")
            self.send_header("Access-Control-Expose-Headers", "Access-Control-Allow-Origin")
           
        self.send_header("Content-type", "application/json")

        # send a blank line to end headers:
        self.wfile.write("\n")

        #send response:
        json.dump({"data": "some-data"}, self.wfile)

server = HTTPServer(("localhost", 8000), MyRequestHandler)

server.serve_forever()