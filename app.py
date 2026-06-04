from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

# BASE DE DATOS SQLITE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# SQLAlchemy

db = SQLAlchemy(app)


# TABLA INVENTARIO
class Inventory(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    cliente = db.Column(db.String(100))
    videojuego = db.Column(db.String(100))
    genero = db.Column(db.String(50))
    plataforma = db.Column(db.String(50))
    precio = db.Column(db.String(20))


# TABLA COMENTARIOS
class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100))

    comentario = db.Column(db.Text)


# CREAR TABLAS
with app.app_context():
    db.create_all()


# PAGINA PRINCIPAL
@app.route('/')
def index():

    games = Inventory.query.all()

    comments = Comment.query.all()

    return render_template(
        'inventory.html',
        title='Chronosys Studios',
        games=games,
        comments=comments
    )


# GUARDAR COMENTARIOS
@app.route('/comment', methods=['POST'])
def comment():

    nombre = request.form.get('nombre')

    comentario = request.form.get('comentario')

    if nombre and comentario:

        new_comment = Comment(
            nombre=nombre,
            comentario=comentario
        )

        db.session.add(new_comment)

        db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run()
