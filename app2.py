# import the module flask, I want Flask
from flask import Flask

# do I want a debug button?
# For now I don't, but this is how 
# it would look like

#debug = True # I comment it out for now 
# because I don't know if I will need it right
# now

# Now for the next step of app2.py
# app2.py will have

# a route

#@app2 # wait before that we will need an initil-
# ization of my app. # After-all, I need
# if name == 'main':
#     app.run()

# alright to initialize:

app = Flask(__name__) # I still do not understan-
# d why I need '__name__' in my function or
# class initialization

# anyways app is an object of Flask(<with the p-
# arameter of name> ) 

# what do I do next?
# I needd... a route . now . lol

# anyways, a route:

@app.route("/") # this route function attribute
# will tell the browser that 'something'
# is within this url # which we need to set
# up

@app.route("/hello") # this will be first app th-
# at I write all by myself. # wish me luck

# I just have to remember a couple of things 
# about git
# git add -A
# git commit -am "redo app"
# git push origin master

# okay that is out of the way

# after route, 
# what do I do?

# I get a function # response?

def function_hello():
	return "Hello world"

# I don't really remember if I pass 'response'
# on through the definition. 
# I don't think so

# let's run the app

if __name__ == '__main__':
	app.run()

# run server with this file
# python app2.py

# I hope this works.

# debugged ### i forgot to place @ in front
# of the route method of the Flash Class

# i could read an article that talks about dec-
# oraters titled # Understanding Python Deco-
# rators in 12 Easy Steps!
# href = 'semonfranklin.com'

# So, I was wrong..
# I had to git add .
# git commit -am 'redo-app'
# git push origin master

# Thus far we've only looked at static routes. let
# 's create something dynamic.

# Add a new route to app.py:

# # dynamic route
@app.route("/test")
def search():
	return "Hello"











