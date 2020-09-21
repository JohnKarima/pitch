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
    # category_name = db.Column(db.text)
    date = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    # comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_pitches(cls):
        return Pitch.query.all()

    @classmethod
    def get_pitches_by_category(cls,category_id):
        return Pitch.query.filter_by(category_id= category_id)

    def get_pitches(id):
        pitches = Pitch.query.filter_by(category_id=id).all()
        return pitches

    @classmethod
    def get_all_pitches(cls):
        '''
        Function that queries the databse and returns all the pitches
        '''
        return Pitch.query.all()







# class PitchCategory(db.Model):
#     __tablename__ ='pitch_categories'
#     id = db.Column(db.Integer, primary_key=True)
#     category_name = db.Column(db.String(255))
#     category_description = db.Column(db.String(255))

#     @classmethod
#     def get_categories(cls):
#         '''
#         This function fetches all the categories from the database
#         '''
#         categories = PitchCategory.query.all()
#         return categories




        

# class Comment(db.Model):
    
#     __tablename__ = 'comments'

#     id = db.Column(db.Integer,primary_key = True)
#     comment_id = db.Column(db.Integer)
#     comment_post = db.Column(db.String)
#     posted = db.Column(db.DateTime,default=datetime.utcnow)
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

#     def save_comment(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_comments(cls,id):
#         comments = Comment.query.filter_by(comment_id=id).all()
#         return comments


