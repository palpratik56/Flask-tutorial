from flask import Flask, redirect, url_for
import time

app = Flask(__name__)

@app.route('/')
def home():
    return '<h2>Welcome Home</h2>'

@app.route('/score')
def sc():
    return '<h2 style="color:blue">Welcome to score page! give name and score on the url</h2>'

@app.route('/pass/<s>/<int:m>')
def passed(s,m):
    return f'<h3 style="color:green"> Congrats {s.title()}! You have passed with {m}% </h3>'

@app.route('/fail/<s>/<int:m>')
def failed(s,m):
    return f'<h3 style="color:orange"> Sorry {s.title()}! You have failed with {m}%</h3>'

@app.route('/score/<name>/<int:val>')
def value(name,val):
    if val >= 40:
        time.sleep(2)
        return redirect(url_for('passed', s=name, m=val))
    else:
        time.sleep(2)
        return redirect(url_for('failed', s=name, m=val))
    
if __name__ == '__main__':
    app.run(debug=True)