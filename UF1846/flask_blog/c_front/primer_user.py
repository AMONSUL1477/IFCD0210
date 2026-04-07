from werkzeug.security import generate_password_hash

email = 'teo@teo.es'
password = 'nada'
rol = 'admin'

hashed = generate_password_hash(password)

print(f"""insert into usuarios(email,pw_hash,rol,nombre) 
    values ('{email}','{hashed}','{rol}','Teo')""")