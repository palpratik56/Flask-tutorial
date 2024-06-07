from flask import Flask, render_template, url_for, redirect, flash, session, request
from forms import login
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_1234'

# following are the extra two lines to make it a server session 
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
@app.route('/Home')
def home():
    return render_template('home.html', tit='Home')

@app.route('/About')
def ab():
    if 'user_name' not in session:
        flash('Login Required')
        return redirect(url_for('loggedin', nxt=request.url))
    else:
        flash(f"Hi {session['user_name']}, have a nice day!!")
    return render_template('about.html', tit='About')

@app.route('/Contact')
def con():
    if 'user_name' not in session:
        flash('Login Required')
        return redirect(url_for('loggedin', nxt=request.url))
    else:
        flash(f"Hi {session['user_name']}, have a nice day!!")
        return render_template('contact.html', tit='Contact')

@app.route('/Login', methods=['GET', 'POST'])
def loggedin():
    fo = login()
    if fo.validate_on_submit():
        session['user_name'] = fo.uname.data
        flash(f"Successfully logged in as {session['user_name'].title()}!!")
        nxt_url = request.args.get('nxt')
        return redirect(nxt_url or url_for('home'))
    else:
        return render_template('login.html', tit='Login', form=fo)

if __name__ == '__main__':
    app.run(debug=True)