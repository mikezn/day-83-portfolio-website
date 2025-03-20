from flask import Flask, render_template, request
import smtplib
import os

from werkzeug.utils import redirect

#for best practices store these as environmental variables
my_email = "your_email_address_here"
password = "your_password_here"

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home_page():
    if request.method == "POST":

        # Email for contact form information #
        # Commented out due to sensitive environmental variables

        # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        #     connection.starttls()
        #
        #     connection.login(user=my_email, password=password)
        #
        #     connection.sendmail(
        #         from_addr=my_email,
        #         to_addrs=my_email,
        #         msg=f"Subject: New message from {request.form['name']} ({request.form['email']})\n\n{request.form['message']}")

        return render_template("index.html", message="Success!")
    else:
        return render_template("index.html", message="Contact Me")

if __name__ == "__main__":
    app.run(debug=True)