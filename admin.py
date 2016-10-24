from subprocess import call
from flask import Flask, url_for, request, render_template
import json
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
            <input type= "text" name="title" id= "title" />
            <input type= "submit" name= "submit" id= "submit" />
          </form>
        <button onclick= "generate()">Generate Pages</button>
        <script>
          function generate()
          {
            window.location.href="/admin/generate/"
          }
        </script>
        </body>
      </html>'''

    return page

@app.route("/admin/generate/", methods= ['POST','GET'])
def generate():
  with open('data.json', 'r') as f:
    data = json.loads(f.read())

    for pic in data:
      id = pic["id"]
      call (['touch',str(id)+'.html'])
      target = open(str(id)+'.html','w')
      title = pic["title"]
      desc = pic["desc"]
      target.write("This is a test: ")
      target.write(str(id))
      target.write("\n")
      target.write(str(title))
      target.write("\n")
      target.write(str(desc))
      target.write("\n")
    target.close()
    return ''' <html>
        <body>
          <form action="" method="post" name= "form">
            <label for= "title">Title</label>
            <input type= "text" name="title" id= "title" />
            <input type= "submit" name= "submit" id= "submit" />
          </form>
        <button onclick= "generate()">Generate Pages</button>
        <script>
          function generate()
         {
            window.location.href="/admin/generate/"
          }
        </script>
        </body>
      </html>''' 


@app.route("/image/<id>")
def image(id):
  with open('data.json', 'r') as f:
    data = json.loads(f.read())
    for pic in data:
      filename = str(pic['id'])+".html"

    return "hello"
   #   with open(str(pic['id'])+'.html', 'r') as page:
   #     print page
    #    return page

if __name__ == "__main__":
  app.run(host= '0.0.0.0', debug = True)
