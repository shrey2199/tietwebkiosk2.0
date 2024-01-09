# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, session
from flask_talisman import Talisman
import requests
from urllib.parse import quote
from loginAction import loginAction
from perInfo import getPerInfo
from examMarks import getExamMarks
from examGrades import getExamGrades
from cgpa import getCgpa
from cgpadetail import getCgpaDetails

app = Flask(__name__)
Talisman(app, content_security_policy=None)
app.secret_key = 'jkshefdhvjshvdf9w8erwuerhv'

ses_list = []

# http://localhost:5000/ - this will be the login page, we need to use both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']

        ses = requests.Session()
        ses, logSuccess = loginAction(username, password, ses)

        if logSuccess == 1:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['username'] = username
            ses_list.append(ses)
            # Redirect to home page
            return redirect(url_for('home'))
        elif logSuccess == 0:
            # Account doesn't exist or password incorrect
            msg = 'Incorrect Password!'
        else:
            msg = 'Incorrect Username or Error Occured!'
    return render_template('index.html', msg=msg)

# http://localhost:5000/logout - this will be the logout page
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('username', None)
   if len(ses_list) > 0:
       ses_list.pop()
   # Redirect to login page
   return redirect(url_for('login'))

# http://localhost:5000/home - this will be the home page, only accessible for loggedin users
@app.route('/home')
def home():
    # Check if user is loggedin
    if ('loggedin' in session) and len(ses_list)!=0:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

# http://localhost:5000/profile - this will be the profile page, only accessible for loggedin users
@app.route('/profile')
def profile():
    # Check if user is loggedin
    if ('loggedin' in session) and len(ses_list)!=0:
        # We need all the account info for the user so we can display it on the profile page
        account = getPerInfo(ses_list[0])[0]
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

# http://localhost:5000/results - this will be the profile page, only accessible for loggedin users
@app.route('/results')
def results():
    # Check if user is loggedin
    if ('loggedin' in session) and len(ses_list)!=0:
        
        res_list = getExamMarks(ses_list[0])

        # Show the results page with results table
        return render_template('results.html', results=res_list)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

# http://localhost:5000/grades
@app.route('/grades')
def grades():
    # Check if user is loggedin
    if ('loggedin' in session) and len(ses_list)!=0:

        grade_list = getExamGrades(ses_list[0])

        # Show the grades page with grades table
        return render_template('grades.html', grades=grade_list)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

# http://localhost:5000/cgpa
@app.route('/cgpa')
def cgpa():
    # Check if user is loggedin
    if ('loggedin' in session) and len(ses_list)!=0:

        cg_list = getCgpa(ses_list[0])

        # Show the grades page with grades table
        return render_template('cgpa.html', cgpa=cg_list)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

# http://localhost:5000/cgpadetail
@app.route('/cgpadetails/<cgpa_id>')
def cgpa_detail(cgpa_id):
    # Check if user is loggedin
    if ('loggedin' in session) and len(ses_list)!=0:

        cg_list = getCgpaDetails(ses_list[0], cgpa_id)

        # Show the grades page with grades table
        return render_template('cgpadetails.html', cgpa=cg_list, cgpa_id=cgpa_id)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

# DEBUG SERVER
if __name__ == '__main__':
    app.run(debug=True, port=5000)