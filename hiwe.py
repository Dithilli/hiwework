"""
hiwe2.py is a "hello world" that runs in a Bottle webserver, and responds to a hit on it's only endpoint with "Hello WeWork and greetings from <Name>", where name is either default, or set by the user using an environment variable, or a command line argument.
It also outputs to STDOUT a log that contains the date and time, the endpoint reached, and the http status code.
"""


import os, sys
from datetime import datetime
from bottle import route, run, response, request

"""
Function namer first creates the variable name, and then checks to see if there's a command line argument setting name.
If not, it checks for an environment variable that sets the variable 'HIWENAME'. If not, it sets the default to "David".
Considered using ArgParse for inputting command line arguments, but this just didn't need it. 
"""
def namer():
    name = None
    if len(sys.argv) > 1:
        name = sys.argv[1]
    elif os.getenv('HIWENAME') != None:
        name = os.getenv('HIWENAME')
    else:
        name = "David"
    return name

"""
Function logger creates three variables (code, time, and endpoint) and populates them with information pulled from
the datetime module, or from the http response object, or request object
"""
def logger():
    code = str(response.status_code)
    time = datetime.now()
    printtime = time.strftime("%H:%M:%S")
    endpoint = str(request.fullpath)
    return printtime + " - Got a request to " + endpoint + " endpoint. Replied with code " + code

@route('/')
def hi():
    name = namer()
    print(logger())
    return "Hello WeWork and greetings from %s!" % name



run(host='0.0.0.0', port=8080)
