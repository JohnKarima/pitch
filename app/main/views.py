from flask import render_template, request, url_for, redirect, abort
from flask_login import login_required
from . import main
from ..models import User
from .forms import UpdateProfile
from .. import db

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home: Pitch.com'
    return render_template('index.html', title = title)


@main.route('/allposts')
def allposts():
    '''
    View allposts page function that returns the allposts page and its data
    '''
    title = 'All Posts'
    return render_template('pitches/allposts.html', title = title)

@main.route('/pitches')
def pitches():
    '''
    View pitches page function that returns the pitches page and its data
    '''
    title = 'Pitches'
    return render_template('pitches/pitches.html', title = title)

@main.route('/pickuplines')
def pickuplines():
    '''
    View pickuplines page function that returns the pickuplines page and its data
    '''
    title = 'Pick-up Lines'
    return render_template('pitches/pickuplines.html', title = title)

@main.route('/oneliners')
def oneliners():
    '''
    View oneliners page function that returns the oneliners page and its data
    '''
    title = 'One-Liners'
    return render_template('pitches/oneliners.html', title = title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)