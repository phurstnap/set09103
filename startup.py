from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home/')
def home():
	return render_template('main.html')
	
@app.route('/home/gallery_people')
def gallery_people():
	return render_template('gallery_people.html')
	
@app.route('/home/gallery_animals')
def gallery_animals():
	return render_template('gallery_animals.html')
	
@app.route('/home/gallery_landscape')
def gallery_landscape():
	return render_template('gallery_landscape.html')
	
@app.route('/home/gallery_buildings')
def gallery_buildings():
	return render_template('gallery_buildings.html')


if __name__ == ("__main__"):
	app.run(host = '0.0.0.0', debug=True)