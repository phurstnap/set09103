from flask import Flask, url_for, abort, request
app = Flask(__name__)

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
def page_not_found(error):
	return "Couldn't find the page."

@app.route("/")
def root():
  print request.method, request.path, request.form
  return "The default, 'root' route"

@app.route("hello/")
def hello():
  name = request.args.get('name', ''

@app.route("/hello/<name>")
def hello(name):
	return "Hello World! Hello %s" % name

@app.route("/account/", methods=['GET', 'POST'])
def account():
  if request.method == 'POST':
    print request.form
    name = request.form['name']
    return "Hello %s" % name
  else:
    page = '''
    <form action="" method="post" name="form">
    <label for="name">Name: </label>
    <input type="text" name="name" id="name"/>
    <input type="submit" name="submit" id="submit"/>
    </form>
    </body><html>'''

    return page

@app.route("/add/<int:first>/<int:second>")
def add(first, second):
  return str(first+second)

@app.route('/static-example/img')
def static_example_img():
  start = '<img src="'
  url = url_for('static', filename='vmask.jpg')
  end = '">'
  return start+url+end, 20

@app.route("/goodbye")
def goodbye():
	return "Goodbye cruel world!"

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
