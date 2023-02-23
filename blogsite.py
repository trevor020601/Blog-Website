from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Trevor Karl',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 23, 2023'
    },
    {
        'author': 'Trevor Karl',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 24, 2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

# Turn on debugger with $env:FLASK_DEBUG=1
# OR use python blogsite.py bc of main method below
if __name__ == '__main__':
    app.run(debug=True)