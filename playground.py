from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
  return render_template('index.html', times = 3)

@app.route('/play/<num>')
def playTwo(num):
  return render_template('index.html', times = int(num))

@app.route('/play/<num>/<color>')
def playThree(num, color):
  return render_template('index.html', times = int(num), bgColor = color)

if __name__=="__main__":
  app.run(debug=True)