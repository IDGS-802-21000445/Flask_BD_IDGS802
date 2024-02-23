from flask import Flask,request,render_template,Response
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import flash,g
from models import db
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos", methods=["GET","POST"])
def alumnos():
    nom =''
    apa=''
    ama=''
    alum_form  =forms.UserForm(request.form)
    if request.method == 'POST':
        nom=alum_form.nombre.data
        apa=alum_form.apaterno.data
        ama=alum_form.amaterno.data
        mensaje = "Bienvenido {}".format(nom)
        flash(mensaje)
        print("nombre: {}".format(nom))
        print("apterno: {}".format(apa))
        print("amaterno: {}".format(ama))

#archivo_texto.write('\n datos en el archivo')
    return render_template("alumnos.html", form=alum_form,nom=nom,apa=apa,ama=ama)

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()