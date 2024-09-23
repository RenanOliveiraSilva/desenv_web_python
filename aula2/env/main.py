from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Ola Mundo'

@app.route('/rota2')
def index():
    return 'Outro Texto'

app.run()