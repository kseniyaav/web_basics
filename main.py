from http.server import HTTPServer, SimpleHTTPRequestHandler

server_host, server_port = '127.0.0.1', 8080

if __name__ == '__main__':
    web_server = HTTPServer(
        (server_host, server_port), 
        SimpleHTTPRequestHandler
    )

    print("Server started http://%s:%s" % (server_host, server_port))
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        web_server.server_close()
        print("Server stopped.")
