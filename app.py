# app.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Smart City! Welcome to your CyberSecure Portal"



if __name__ == "__main__":
    app.run(debug=True)