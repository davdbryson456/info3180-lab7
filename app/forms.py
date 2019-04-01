from flask_wtf import Form
from wtforms import TextAreaField
from flask_wtf.files import FileField,FileAllowed,FileRequired 
from wtforms.validators import DataRequired

class uploadForm(Form):
    
    description=TextAreaField('Description',valiadators=[DataRequired()])
    photo= FileField('photo', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])




