from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
lugares = []

@app.route('/')
def index():
    return render_template('index.html', lugares=lugares)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form['nome']
    comida = request.form['comida']
    essencial = request.form['essencial']
    lugares.append({
        'nome': nome,
        'comida': comida,
        'essencial': essencial
    })
    return redirect(url_for('index'))

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)