from flask import render_template, flash, redirect
from .forms import LoginForm
from app import app

import HTMLscraper as scrape
from CRNinfoOrganizer import *

@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'Cynthia'}  # fake user
    Matrix = [[ "-" for x in range(6)] for x in range(17)]
    Matrix[0][0] = "-"
    Matrix[0][1] = "Monday"
    Matrix[0][2] = "Tuesday"
    Matrix[0][3] = "Wednesday"
    Matrix[0][4] = "Thursday"
    Matrix[0][5] = "Friday"
    for row in range(1, 17):
            Matrix[row][0] = row + 7
    # gross hardcode begins
    crns = []
    titles = []
    times = []

    for id in allcourses:
       crns.append(id)
       titles.append(getTitle(id))
       times.append(getDayTimes(id))
    # gross hardcode ends

    return render_template("index.html",
                           title='Home',
                           user=user,
                           Matrix=Matrix,
                           allcourses=allcourses,
                           titles=titles,
                           crns=crns,
                           times=times)

# demo page hardcoded too
@app.route('/demo')

def demo():
    user = {'nickname': 'Alice'}  # fake user
    Matrix = [[ "-" for x in range(6)] for x in range(17)]
    Matrix[0][0] = "-"
    Matrix[0][1] = "Monday"
    Matrix[0][2] = "Tuesday"
    Matrix[0][3] = "Wednesday"
    Matrix[0][4] = "Thursday"
    Matrix[0][5] = "Friday"
    Matrix[4][1] = "Principles of Microeconomics"
    Matrix[1][2] = "American Politics"
    Matrix[4][2] = "Comp Program & Prob Solv w/ Lab"
    Matrix[6][2] = "Multivariable Calculus"
    Matrix[7][3] = "Multivariable Calculus"
    Matrix[1][4] = "LAB: Comp Program & Prob Solv"
    Matrix[4][4] = "Principles of Microeconomics"
    Matrix[1][5] = "American Politics"
    Matrix[4][5] = "Comp Program & Prob Solv w/ Lab"
    Matrix[6][5] = "Multivariable Calculus"
    for row in range(1, 17):
            Matrix[row][0] = row + 7
    # gross hardcode begins
    crns = []
    titles = []
    times = []

    for id in allcourses:
       crns.append(id)
       titles.append(getTitle(id))
       times.append(getDayTimes(id))
    # gross hardcode ends

    return render_template("index.html",
                           title='Home',
                           user=user,
                           Matrix=Matrix,
                           allcourses=allcourses,
                           titles=titles,
                           crns=crns,
                           times=times)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign In',
                            form=form)
