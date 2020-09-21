from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    pitch = db.relationship('Pitch',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)
            
    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy = "dynamic")

    def __repr__(self):
        return f'User {self.name}'

class Pitch(db.Model):
    '''
    Pitch class that define Pitch Objects
    '''
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.Text)
    category_id = db.Column(db.Integer)
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    date = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches_by_category(cls,category_id):
        return Pitch.query.filter_by(category_id= category_id)

    def get_pitches(id):
        pitches = Pitch.query.filter_by(category_id=id).all()
        return pitches

    @classmethod
    def get_all_pitches(cls):
        '''
        Function that queries the database and returns all the pitches
        '''
        return Pitch.query.all()


class Comment(db.Model):
    
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save_comments(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        return comments

    @classmethod
    def clear_(cls):
        Comment.all_comments.clear()
