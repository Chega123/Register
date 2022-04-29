from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("nombre")
    surname = request.form.get("apellido")
    genre= request.form.get("genero")
    region = request.form.get("region")
    birhtdate = request.form.get("fecha_de_cumpleaños")
    password = request.form.get("contraseña")
    email = request.form.get("email")
    
    return render_template(
        "session.html",
		nombre=name,
        apellido=surname,
        genero=genre,
        region=region,
        fecha_de_cumpleaños=birhtdate,
        contraseña=password,
        email=email,
    )
