from flask import Flask
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_wtf.file import FileRequired, FileAllowed


class UploadForm(FlaskForm):
	file = FileField('Upload', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only')])