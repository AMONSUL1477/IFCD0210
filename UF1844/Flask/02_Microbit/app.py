from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hola():
    return render_template ('home.html')

@app.route('/software')
def get_software():
    return render_template ('software.html')

@app.route('/firmware')
def get_firmware():
    return render_template ('firmware.html')