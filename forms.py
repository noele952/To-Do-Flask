from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class CreateToDo(FlaskForm):
    task = StringField("Task", validators=[DataRequired()])
    # notes = CKEditorField('Notes')
    submit = SubmitField('Submit')
