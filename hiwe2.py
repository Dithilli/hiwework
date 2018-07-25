"""
hiwe2.py is a "hello world" micro webservice that creates a Bottle micro-framework for web applications, and can take a single get to its
solitary endpoint. It then responsds with "Hello WeWork ang greetings from <Name>", where name is either a given default, or set 
by the user using an environment variable, or a command line argument. HiWe will prioritize command line arguments over environment variables.


It also outputs to STDOUT a log that contains the date and time, the endpoint reached, and the http status code.
"""


import os, sys
from bottle import route, run, response, request

"""
Function namer first creates the variable name, and then checks to see if there's a command line argument setting name.
If not, it checks for an environment variable that sets the variable 'name'. If not, it sets the default to "David".

Considered using ArgParse module for inputting command line arguments, but this just didn't need it. 
"""
def namer():
    name = None
    if name == None and len(sys.argv) > 1:
        name = sys.argv[1]
    if name == None:
        name = os.getenv('name')
    if name == None:
        name = "David"
    return name

"""
Logger() 
"""
def logger():
    return request.headers['date'], "Got a request to ", request.path, " endpoint. Replied with ", response.status_code, " code"

"""
The decorator route() is a bottle defined function that runs whatever function is after it whenever a get request hits the defined url. hi() calls namer()
on the off chance that we wanted to check to see if the name had changed in the environmental variables between gets. 
"""
@route('/')
def hi():
    name = namer()
    print(logger())
    return "Hello WeWork and greetings from %s!" % name


run(host='0.0.0.0', port=5000)

