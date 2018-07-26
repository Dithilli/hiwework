Challenges:

What is a / endpoint exactly? How do I implement this?

An endpoint is a way to access information from a webservice -- i't's the core of an API, accessed with a verb. Here, "get".
How do I implement this without a micro web-framework? Can't. Consider Flask or Bottle 
		
Flask or Bottle:

Flask seems better for large projects, has better documentation and scales better. Bottle fits in a single file and has only python’s main libraries as dependencies. 
			Bottle Instillation - $ sudo pip install bottle
			Bottle Syntax for a simple hello-world program 

How do I create environmental variables? Or Command Line Variables? How do I import those into my script?

Enviromental Variables 

Imported from the OS using import os, there’s only one syntactical call—os.environ.get(). – easily given to the program on a unix command line with (__variablename__)=(___variablevalue____) python myapp.py

For example, in my program, I could call NAME = os.environ.get(“ENTERED_NAME”, “”) (I’m unsure if I need both of those variables in there? Will have to figure out. To set my environmental variable from the command line (in UNIX? Works other places?) I can type DEBUG_MODE=xxx python manage.py

Command Line

Command line arguments are imported into a python script using sys library, specifically sys.argv, which stands for system argument values. This is a list, where the zero index is always ‘argv_list.py’. 

The simple thing to do would be to have a small function that took as NAME sys.argv[1] which SHOULD be the command line argument that fits our name. This is quick and easy and would work provided that no other command line arguments are implemented. Is it enough to explain that I did it this way for the sake of simplicity, but consider implementing argparse if I have time. 
	
  
How do I output the log file for extra credit?

With sys imported, the stdout (“standard out”) is the normal unix pipline for outputs. In fact, that’s what I’m seeing in the console window when I “print”. The syntax looks like this.  sys.stdout.write(‘Output’). Or I can just print. 
  
My log needs three kinds of data - path, from the request object, code, from the response object, and the time the request was served. 

What frameworks do I need to make sure I have? What dependencies are there? They’ll all have to be in my image. 

Current List of Dependencies 
		Import sys #necessary for outputting I think? Also necessary for reading command line arguments
		Import bottle # my chosen micro webplatform for this script
		Import datetime # necessary for the time logging to my standard output because I can't get what I want from the darn 
		Import os #this imports the os library for my environmental variables 
