from flask import Flask, render_template, url_for, redirect
from forms import AñadirEstudianteForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'robtop'

users = {
        "rodrigo": {
            "name": "rodrigo",
            "password": "123",
            "notas": [1, 2, 3]
        }
    }

@app.route("/")
def main():
    return render_template('estudiante/index.html')

@app.route("/admin")
def admin():
    return render_template('admin/index.html')

@app.route("/eliminar_estudiante")
def eliminar_estudiante():
    return render_template('admin/eliminar_estudiante/eliminar_estudiante.html')

@app.route("/añadir_estudiante", methods=['GET', 'POST'])
def añadir_estudiante():
    form = AñadirEstudianteForm()
    if form.is_submitted():
        # logica
        print("BIEEN UN LOGIN")

        return redirect(url_for('admin'))
    return render_template('admin/añadir_estudiante/añadir_estudiante.html', form=form)

@app.route("/lista_estudiantes")
def lista_estudiantes():
    return render_template('admin/lista_estudiantes/lista_estudiantes.html', users=users)

app.run(host='0.0.0.0', port=3030)