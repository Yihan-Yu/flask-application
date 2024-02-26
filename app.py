from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# Define submit_page() here
# Reminder: Don't forget the decorator before the "def" line
@app.route("/submit-page", methods=['GET', 'POST'])
def submit_page():
    if request.method == "POST":
        name = request.form["user_name"]
        email = request.form["user_email"]
        return render_template('results.html', name=name, email=email)


if __name__ == '__main__':
    app.run()