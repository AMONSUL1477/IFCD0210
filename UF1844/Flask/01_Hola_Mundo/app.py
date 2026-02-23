from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def hello_world():
    return 'Hola Mundo'

@app.route('/hola')

def hola():
    cadena = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <h1>
    HOLA USUARIO
    </h1>


    <h2>
    Bienvenido
    </h2>
    
</body>
</html>

"""

    return cadena

@app.route('/prueba')
def prueba():
    return render_template('prueba.html')


@app.route('/prueba1/')
@app.route('/prueba1/<string:nombre>')
@app.route('/prueba1/<string:nombre>/<int:numero>')
def saludo(nombre=None,numero=None):
    salida =""
    if nombre and numero:

        salida = f'Hola {nombre} tienes {numero} años'

    elif nombre:
        salida = f'Hola {nombre}'

    else:
        salida = "Hola caracola"

    return salida

@app.route('/suma',methods =['GET','POST'])
def sumar():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        return str(int(num1) + int(num2))
    else:
        cadena = '''

        <form action="/suma" method="post">
            <label>N1:</label>
            <input type="text" name="num1"/>
            <label>N2:</label>

        <input type="text" name="num2"/>
        <input type="submit" value="Sumar"/>

        </form>


        '''    

        return cadena    
    

@app.route('/jinja1')
def jinja1():
    lista =['uno', 'dos', 'tres', 'cuatro']
    # return render_template('jinja1.html', apellidos = 'Gomez García', numeros = lista)
    return render_template('principal.html')





if __name__== '__main__':
    app.run(debug=True)