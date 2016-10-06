from flask import Flask, url_for, request, render_template, json
app = Flask(__name__)

@app.route("/admin/", methods= ['POST','GET'])
def admin():
  if request.method == 'POST':
    title = request.form ['title']
    return render_template('newpage.html', title=title)

  else:
    page = '''
      <html>
        <body>
          <form action="" method="post" name= "form">
            <label for= "title">Title</label>
            <input type= "text" name="title" id= "title"/>
            <input type= "submit" name= "submit" id= "submit"/>
          </form>
        </body>
      <html>'''

    return page
if __name__ == "__main__":
  app.run(host= '0.0.0.0', debug = True)
