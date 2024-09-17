from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class AñadirEstudianteForm(FlaskForm):
    username = StringField('Usuario')
    password = PasswordField('Contraseña')
    submit = SubmitField('Añadir')