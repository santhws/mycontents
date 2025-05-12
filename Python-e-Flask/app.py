# Importação 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db' #configuração do banco de dados

db = SQLAlchemy(app) #conexão do banco de dados

#Modelagem

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

# Definir uma rota raiz (página inicial) e a função que será executada ao requisitar

@app.route('/')
def Hello_Word():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)
    