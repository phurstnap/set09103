from flask import Flask, render_template
app = Flask(__name__)

@app.route('/gallery/')
def gallery():
	return render_template('gallery.html')
	
@app.route('/home/people')
def people():
	return render_template('people.html')
	
@app.route('/home/animals')
def animals():
	return render_template('animals.html')
	
@app.route('/home/landscape')
def landscape():
	return render_template('landscape.html')
	
@app.route('/home/')
def buildings():
	return render_template('buildings.html')


if __name__ == ("__main__"):
	app.run(host = '0.0.0.0', debug=True)