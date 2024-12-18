from flask import Flask, render_template, request, redirect, url_for
from defs import *
from app import SistemaIFS

app =  Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rota')
def rota():
    return redirect(url_for('index'))

@app.route('/dadoscnpj', methods=['POST'])
def datecnpj():
    return render_template('rota.html', new_cnpj=cnpj_cnpj(request.form['cnpj_post']))

@app.route('/dadoscep', methods=['POST'])
def datecep():
    return render_template('rota.html', new_cnpj=cep_cep(request.form['cep_post']))

@app.route('/dadostime', methods=['POST'])
def datetime():
    return render_template('rota.html', new_cnpj=cnpj_cnpj(request.form['time_post']) )

@app.route('/edit')
def edit():
    return render_template('date.html')

@app.route('/IFSAUTO', methods=['POST'])
def automac():
    return render_template('new.html', ifsmais=SistemaIFS(request.form['username'], request.form['password']) )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="8000", debug=True)