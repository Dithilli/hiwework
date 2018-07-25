import os, sys
from datetime import datetime
from bottle import Bottle, route, run, response, request


name = None

if name == None:
    name = os.getenv('name')
if name == None and len(sys.argv) > 1:
    name = sys.argv[1]
if name == None:
    name = "David"


@route('/')
def hi():
    code = str(response.status)
    time = str(datetime.now())
    endpoint = str(request.fullpath)
    printout = (time + "- Got a request to " + endpoint + "endpoint. Replied with code" + code)
    print(printout)
    sys.stdout.write(printout)
    return "Hello WeWork and greetings from %s!" % name


run(host='localhost', port=8080)

