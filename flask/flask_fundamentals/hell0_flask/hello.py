from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
  return "Hello World!"

@app.route("/dojo")
def dojo():
  return "Dojo"

@app.route("/say/<name>")
def name(name):
  return f"Hi {name}"

@app.route("/repeat/<int:numCount>/<hello>")
def repeatHello(numCount, hello):
  return f"hello" * numCount

@app.errorhandler(404)
def page_not_found(e):
  return render_template('index.html')

if __name__== "__main__":
  app.run(debug=True)