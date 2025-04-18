# app.py

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

otp_store = {}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]

        # generate a 6 digit OTP
        import random
        otp = str(random.randint(100000, 999999))
        otp_store[email] = otp

        print(f"[MOCK] otp for {email} is {otp}")

        flash("OTP has been sent to your email. (MOCK)")
        return redirect(url_for("verify_otp", email=email))
    
    return render_template("login.html")


@app.route("/verify/<email>", methods=["GET", "POST"])
def verify_otp(email):
    if request.method == "POST":
        entered_otp = request.form["otp"]
        correct_otp = otp_store.get(email)

        if entered_otp == correct_otp:
            flash("OTP Verified!")
            return redirect(url_for("home"))
        else:
            flash("Invalid OTP. Try again.")
            return redirect(url_for("verify_otp", email=email))
        
    return render_template("verify.html")


if __name__ == "__main__":
    app.run(debug=True)