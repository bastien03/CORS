#!/usr/bin/env python3

import http.server
import logging

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path=="/cors":
            logging.warning("--> CORS")
            http.server.SimpleHTTPRequestHandler.send_header(self, 'Access-Control-Allow-Origin', '*')
            http.server.SimpleHTTPRequestHandler.end_headers(self)
        else:
            logging.warning("--> no CORS")

        #logging.warning("======= GET STARTED =======")
        #logging.warning(self.headers)
        self.send_response(207)
        #self.wfile.write({"name":"Truffaut"})
        http.server.SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    http.server.test(HandlerClass=CORSRequestHandler)
