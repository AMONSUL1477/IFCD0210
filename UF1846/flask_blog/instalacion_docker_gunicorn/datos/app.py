from flask import Flask,request,jsonify
import mysql.connector
import config
import os

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
                        host=os.environ['DB_HOST'], 
                        user=os.environ['DB_USER'],
                        password=os.environ['DB_PASSWORD'],
                        database=os.environ['DB_NAME'],
                        port=os.environ['DB_PORT'])




def fetch_all(query, params=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query,params or ())
    result = cursor.fetchall()
    conn.close()
    return result

def fetch_one(query, params=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query,params or ())
    result = cursor.fetchone()
    conn.close()
    return result

def execute(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query,params or ())
    conn.commit()
    last_id = cursor.lastrowid
    conn.close()
    return last_id


# Endpoints de usuarios

@app.route('/data/user/by-email')
def get_user_by_email():
    email = request.args.get('email')
    # c = f"select * from usuarios where email = '{email}'"
    # print(c)
    user = fetch_one("select * from usuarios where email = %s", (email,))
    return jsonify(user)


@app.route('/data/user', methods=['POST'])
def create_user():
    data = request.json
    user_id = execute(
        "insert into usuarios(nombre,email,pw_hash,rol,f_alta) values(%s,%s,%s,%s,%s)",
        (
        data['nombre'],
        data['email'],
        data['pw_hash'],
        data['rol'],
        data['f_alta'])
        )
    return jsonify({'id':user_id})

# ---------------------------------
# POSTS

#Obtener todos
@app.route('/data/posts')
def get_posts():
    posts = fetch_all("select * from posts")
    return jsonify(posts)

#Obtener uno
@app.route('/data/post/<int:post_id>')
def get_post(post_id):
    post = fetch_one("select * from posts where id=%s",(post_id,))
    return jsonify(post)

#Crear un post
@app.route('/data/post',methods=['POST'])
def create_post():
    data = request.json
    post_id = execute(
        "insert into posts(id_autor, titulo, contenido,estado) values(%s,%s,%s,%s)",
        (data['id_autor'],data['titulo'],data['contenido'],data['estado'])
    )
    return jsonify({'id':post_id})

#Actualizar post
@app.route('/data/post/<int:post_id>',methods=['PUT'])
def update_post(post_id):
    data = request.json
    execute('update posts set titulo=%s, contenido=%s, estado=%s where id=%s',
            (data['titulo'],data['contenido'],data['estado'],post_id))
    return jsonify({'mensaje':'Post actualizado con éxito.'})


#Eliminar post
@app.route('/data/post/<int:post_id>',methods=['DELETE'])
def delete_post(post_id):
    execute('delete from posts where id = %s',(post_id,))
    return jsonify({'mensaje':'Post borrado.'})

# --------------------------------------------------------

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
