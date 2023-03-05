from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__) 

# create a route
@app.route('/')
@app.route('/home')
def home_page():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

# create custom error pages
# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", e=404)

# internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html", e=500)