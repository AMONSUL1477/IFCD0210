from flask import Flask, render_template,request, redirect, url_for, send_from_directory
import sqlite3

app = Flask(__name__)
BD = "tareas.sqlite"

def get_conection():
    cnx = sqlite3.connect(BD)
    cnx.row_factory = sqlite3.Row # Para usar los nombres de columnas
    return cnx

def init_bd():
    conn = get_conection()
    conn.execute("""
    create table if not exists tarea(
        id integer primary key autoincrement, 
        tarea text not null,
        descripcion text not null,
        fecha text not null)""")
    
    conn.commit()
    conn.close()

    # creamos la base de datos si no existe
init_bd()
    



@app.route("/")
def index():
    conn = get_conection()
    tareas = conn.execute("select * from tarea").fetchall()
    conn.close()
    return render_template("index.html", tars=tareas)

# Editar tarea
@app.route('/editar/<int:id>', methods=['POST','GET'])
def editar(id):
    conn = get_conection()
    tarea = conn.execute('select * from tarea where id = ?', (id,)).fetchone()

    if request.method == 'POST':
        tarea = request.form['tarea']
        descripcion = request.form['descripcion']
        fecha = request.form['fecha']

        conn.execute('''update tarea set tarea=?, descripcion=?, fecha=? where id=? ''',(tarea,descripcion,fecha,id))

        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('editar.html', tarea=tarea)

@app.post('/borrar/<int:id>')
def borrar(id):

    conn = get_conection()
    conn.execute("delete from tarea where id=?", (id,))

    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# insertar

@app.route('/crear', methods=['POST', 'GET'])
def crear():
    if request.method == 'POST':
        tarea = request.form['tarea']
        descripcion = request.form['descripcion']
        fecha = request.form['fecha']

        conn = get_conection()
        conn.execute('''insert into tarea(tarea,descripcion,fecha)
                    values (?,?,?)''',(tarea,descripcion,fecha))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('crear.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save('archivos/'+ file.filename)
    file_url = url_for('uploaded_file',filename=file.filename, external=True)
    return f'Tarea subida correctamente <br> Enlace:<a href="(file_url)">(file_url)</a>'

@app.route('/archivos/<filename>')
def uploaded_file(filename):
    return send_from_directory('archivos',filename)

