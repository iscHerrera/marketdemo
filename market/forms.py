from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, ValidationError, DataRequired
from market.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check): # Flask valida el nombre de la funcion con lo que sigue de validate_, por lo tanto va y busca e campo username
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('El Usuario ya exite, por favor trata con otro')

    def validate_email_address(self,email_address_to_check):
        email = User.query.filter_by(email=email_address_to_check.data).first()
        if email:
            raise ValidationError('El Email ya existe, por favor trata con otro')

    username = StringField(label='Nombre de usuario:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Crear Cuenta')


class LoginForm(FlaskForm):
    username=StringField(label='User Name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')


class PurchanseItemForm(FlaskForm):
    submit = SubmitField(label='Comprar producto')


class SellItemForm(FlaskForm):
    submit = SubmitField(label='Vender producto')
