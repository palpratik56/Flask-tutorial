from flask import Flask,render_template, url_for, redirect, flash
# from student import stu_data
from forms import signup,login

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'

@app.route('/')
@app.route('/Home')
def home():
    return render_template('home.html', tit='Home')

@app.route('/Signup', methods=['GET', "POST"])
def sign():
    fo = signup()
    if fo.validate_on_submit():
        flash(f'Successfully registered with username {fo.uname.data}!!')
        return redirect(url_for('home'))
    return render_template('signup.html', tit='Sign Up', form = fo)

@app.route('/Login', methods=['GET', "POST"])
def log():
    fo = login()
    un = fo.uname.data
    pwd  = fo.pwd.data
    if fo.validate_on_submit():
        if un=='123rr' and pwd=='12345696':
            flash(f'Successfully Logged in !!')
            return redirect(url_for('home'))
        else:
            flash('Incorrect credentials')
    return render_template('login.html', tit='Log In', form = fo)

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/About')
# def about():
#     return render_template('about.html', tit='ABOUT')

# @app.route('/Check/<int:n>')
# def ch(n):
#     return render_template('check.html', tit='CHECK', num=n)

# @app.route('/Students')
# def stu():
#     return render_template('student.html', tit='STUDENT', studs = stu_data)

# @app.route('/Careers')
# def car():
#     return render_template('career.html', tit='Careers')