from flask import render_template, url_for, redirect
from flask_login import login_required
from . import main

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home- Pitch.com'
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

