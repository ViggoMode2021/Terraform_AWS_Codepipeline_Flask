from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    time = datetime.datetime.now()
    return render_template("index.html", time=time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=False)
