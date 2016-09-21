@app.route("/private")
def private():
	# Test for user logged in failed
	# so refirest to login URL
	return redirect(url_for('login'))
	
@app.route('/login')
def login():
	return "Now we would get username and password"
	
@app.route('/force404')
def force404():
	abort(404)
	
@app.errorhandler(404)
def page_not_found(error)
	return "Couldn't find the page."

@app.route("/")
	return "The default, 'root' route"

@app.route("/hello")
def hello():
	return "Hello World!"
	
@app.route("/goodbye")
def goodbye():
	return "Goodbye cruel world!"
	
if __name__ == "__main__"
	app.run(host='0.0.0.0', debug=True)