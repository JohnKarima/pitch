from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    comment = StringField('Comment',validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    category_id = SelectField('Which category best suits your post?', choices=[('1', 'Pitches'), ('2', 'Pickup Lines'), ('3', 'One-Liners')])
    content = TextAreaField('Create a post', validators=[Required()])
    submit = SubmitField('Submit') 
