from flask import Flask, request

app = Flask(__name__)

# Issue 1: Hardcoded Secret
password = "admin123"

@app.route('/')
def home():
    return "Welcome!"

# Issue 2: Debug Mode Enabled
@app.route('/hello')
def hello():
    name = request.args.get('name')
    return "Hello " + name

if __name__ == '__main__':
    app.run(debug=True)
