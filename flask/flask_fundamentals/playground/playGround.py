from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return "Welcome to the Playground."
@app.route('/play')
def play():
  return render_template("boxes.html")

@app.route('/play/<int:num>')
def playX(num):
  return render_template("boxesNum.html", num = num)

@app.route('/play/<int:num>/<color>')
def playXColor(num, color):
  return render_template("boxesNum.html", num = num, color = color)

if __name__== "__main__":
  app.run(debug=True)