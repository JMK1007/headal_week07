from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "컴퓨터학부 2018117628 김지민"

@app.route("/me/")
def trip():
    mongolia = ["mongolia_1.jpg", "mongolia_2.jpg", "mongolia_3.jpg"]
    photo = random.choice(mongolia)
    return render_template('index.html', my_trip=photo)

if __name__=="__main__":
    app.run(debug=True)