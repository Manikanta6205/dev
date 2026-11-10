from flask import Flask, request
import os

app = Flask(__name__)

# Secure password
password = os.environ.get("APP_PASSWORD")

@app.route('/')
def home():
    return "Welcome!"

@app.route('/hello')
def hello():
    name = request.args.get('name', '')
    return "Hello " + name

if __name__ == '__main__':
    app.run(debug=False)
