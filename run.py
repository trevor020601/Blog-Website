from blogsite import app

# Turn on debugger with $env:FLASK_DEBUG=1
# OR use python blogsite.py bc of main method below
if __name__ == '__main__':
    app.run(debug=True)