from flask import render_template, request, url_for, redirect, abort, flash
from flask_login import login_required, current_user
from . import main
from ..models import User, Pitch
from .forms import UpdateProfile, PitchForm
from .. import db, photos

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    pitches= Pitch.get_all_pitches()
    title = 'Home'
    return render_template('index.html', pitches = pitches, title = title)

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
    pitches= Pitch.get_pitches_by_category(1)
    title = 'Pitches'
    return render_template('pitches/pitches.html', title = title, pitches = pitches)

@main.route('/pickuplines')
def pickuplines():
    '''
    View pickuplines page function that returns the pickuplines page and its data
    '''
    pitches= Pitch.get_pitches_by_category(2)
    title = 'Pick-up Lines'
    return render_template('pitches/pickuplines.html', title = title, pitches = pitches)

@main.route('/oneliners')
def oneliners():
    '''
    View oneliners page function that returns the oneliners page and its data
    '''
    pitches= Pitch.get_pitches_by_category(3)
    title = 'One-Liners'
    return render_template('pitches/oneliners.html', title = title, pitches = pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    title = 'Profile'
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user, title = title)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    title = 'Update'
    if user is None:
        abort(404)
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form, title = title)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/new_post', methods = ['GET','POST'])
def new_post():
    form = PitchForm()
    title = 'New Post'
    if form.validate_on_submit():
        pitch = Pitch( category_id = form.category_id.data, pitch = form.content.data,)
        pitch.save_pitch()
        return redirect(url_for('main.index'))
    return render_template('/new_post.html',pitch_form = form, title = title)