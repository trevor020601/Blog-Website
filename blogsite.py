from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

# Turn on debugger with $env:FLASK_DEBUG=1
# OR use python blogsite.py bc of main method below
if __name__ == '__main__':
    app.run(debug=True)