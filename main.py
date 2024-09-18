from flask import Flask, render_template, url_for, redirect
from forms import AñadirEstudianteForm, EliminarEstudianteForm, AñadirNotaForm, EliminarNotaForm, LoginForm
from backend.users import login_user, users_dict

app = Flask(__name__)
app.config['SECRET_KEY'] = 'keyultrasecreta'

# este users es un ejemplo, hay que reemplazarlo

@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.is_submitted():
        name = str(form.username.data)
        pwd = str(form.password.data)

        if(login_user(name, pwd)):
            if name == 'admin':
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('estudiante'))
        else:
            pass
    return render_template('login.html', form=form)

@app.route("/estudiante")
def estudiante():
    return render_template('estudiante.html')

@app.route("/admin")
def admin():
    return render_template('admin/index.html')

@app.route("/añadir_estudiante", methods=['GET', 'POST'])
def añadir_estudiante():
    form = AñadirEstudianteForm()
    if form.is_submitted():
        # logica
        # form.password.data
        # form.username.data
        return redirect(url_for('añadir_estudiante'))
    return render_template('admin/añadir_estudiante.html', form=form)

@app.route("/añadir_nota", methods=['GET', 'POST'])
def añadir_nota():
    form = AñadirNotaForm()
    if form.is_submitted():
        # logica
        # form.password.data
        # form.username.data
        return redirect(url_for('añadir_nota'))
    return render_template('admin/añadir_nota.html', form=form)

@app.route("/eliminar_estudiante", methods=['GET', 'POST'])
def eliminar_estudiante():
    form = EliminarEstudianteForm()
    if form.is_submitted():
        # logica
        # form.password.data
        # form.username.data
        return redirect(url_for('eliminar_estudiante'))
    return render_template('admin/eliminar_estudiante.html', form=form)

@app.route("/eliminar_nota", methods=['GET', 'POST'])
def eliminar_nota():
    form = EliminarNotaForm()
    if form.is_submitted():
        # logica
        # form.password.data
        # form.username.data
        return redirect(url_for('eliminar_nota'))
    return render_template('admin/eliminar_nota.html', form=form)

@app.route("/lista_estudiantes")
def lista_estudiantes():
    return render_template('admin/lista_estudiantes.html', users=users_dict)



app.run(host='0.0.0.0', port=3030)