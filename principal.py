from flask import Flask, render_template
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')
    
@app.route('/tutores'):
    return render_template('tutores.html')

@app.route('/animais'):
    return render_template('animais.html')

@app.route('/medicos')
def medicos():
    return render_template('medicos.html')

if __name__ == '__main__':
    app.run()
