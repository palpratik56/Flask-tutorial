from flask import Flask
app = Flask(__name__)

@app.route('/<name>')
def home1(name):
    return f'<h2>Hello {name.title()}! Welcome to home page</h2>'

@app.route('/')
def home():
    return '<h2>Welcome Home</h2>'

if __name__ == '__main__':
    app.run(debug=True)