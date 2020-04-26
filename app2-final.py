# here I go again.

from flask import Flask

# Import the class

# initili

app = Flask(__name__) # but why do we use __name__

# there I go an app object initil from class Flask

# debug menu
app.config["DEBUG"] = True

# next

@app.route('/')
@app.route('/home')
@app.route('/Home')
def home():
	return "Home page?!?!?!?!"

# I want to create a dynamic route
# not here  (moved-1)

# what do I do next?

# now define a function
@app.route('/about')
@app.route('/About')
def about():
	return "About page"

# (moved here-1)
@app.route('/test/<search_querry>')
def test_function(search_querry):
	return search_querry

# test this code out
@app.route("/integer/<int:value>")
def int_type(value):
	print(value + 1)
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	print(value + 1)
	return "correct"

@app.route("/path/<path:value>")
def path_type(value):
	print(value)
	return "correct"

@app.route("/name/<name>")
def index(name):
	if name.lower() == 'michael':
		return "Hello, {}".format(name)
	else:
		return "Not Found", 404


# run if in current directory

if __name__ == '__main__':
	app.run()