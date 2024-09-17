from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('estudiante/index.html')

@app.route("/admin")
def admin():
    return render_template('admin/index.html')

@app.route("/eliminar_estudiante")
def eliminar_estudiante():
    return render_template('admin/eliminar_estudiante/eliminar_estudiante.html')

@app.route("/añadir_estudiante")
def añadir_estudiante():
    return render_template('admin/añadir_estudiante/añadir_estudiante.html')

@app.route("/lista_estudiantes")
def lista_estudiantes():
    return render_template('admin/lista_estudiantes/lista_estudiantes.html')

app.run(host='0.0.0.0', port=3030)