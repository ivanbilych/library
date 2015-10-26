from flask.ext.wtf import Form
from wtforms.fields import TextField, PasswordField, BooleanField
from wtforms.validators import Required, Length

class LoginForm(Form):
    login = TextField('login', validators = [Required()])
    password = PasswordField('password', validators = [Required(), Length(min=5)])
    remember_me = BooleanField('remember_me', default = False)
