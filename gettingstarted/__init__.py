from flask import Flask, render_template
# $env:FLASK_APP = "application.py"
# $export FLASK_ENV = "development"

app = Flask(__name__)  # __name__ represents current file


@app.route("/")
def index():
    headline = "helloooo"
    return render_template("form.html", headline=headline)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)