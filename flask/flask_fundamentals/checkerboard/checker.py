from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("checker1.html")

@app.route('/<int:num>')
def changeHeight(num):
  return render_template("checker2.html", num =num)

@app.route('/<int:num1>/<int:num2>')
def changeHeigthWidth(num1, num2):
  return render_template("checker3.html", num1 = num1, num2 = num2)

@app.route('/<int:num1>/<int:num2>/<color1>/<color2>')
def changeColor(num1, num2, color1, color2):
  return render_template("checker5.html", num1 = num1, num2 = num2, color1 = color1, color2 = color2)

if __name__== "__main__":
  app.run(debug=True)