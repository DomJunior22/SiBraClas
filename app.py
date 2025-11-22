# BIBLIOTECAS IMPORTADAS
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import  SQLAlchemy


#INICIANDO O APP FLASK
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('https://sibraclas-production.up.railway.app/inicial.html')

@app.route('/pagar')
def pagar():
     return render_template('pagar.html')





if __name__ == '__main__':
        app.run(debug=True)

