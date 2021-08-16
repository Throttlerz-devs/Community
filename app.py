from flask import Flask, render_template
import random

f = ["/static/audio/music1.mp3", "/static/audio/music2.mp3","/static/audio/music3.mp3","/static/audio/music4.mp3"]
music = random.choice(f)

app = Flask(__name__)



@app.route("/")
def home():
    return render_template('index.html', music=music)


if __name__ == "__main__":
    app.run(debug=True)
