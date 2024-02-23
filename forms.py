from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, EmailField
from wtforms import validators

class UserForm(Form):
    nombre = StringField('Nombre',[validators.DataRequired(message='Favor de ingresar el nombre'),
                                   validators.length(min=1,max=40,message='Ingresa nombre valido')
                                   ])
    
    apaterno = StringField('Apaterno')
    amaterno = StringField('materno')
    edad = StringField('Edad',[validators.number_range(min=1,max=20,message='Valor no valido')
                               ])



