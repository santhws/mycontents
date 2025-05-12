# Importação 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config('SQLALCHEMY_DATABASE_URI') = 'sqlite:///ecormmerce.db' #configuração do banco de dados

db = SQLAlchemy(app) #conexão do banco de dados

#Modelagem
class Product(db.Model):
    id = db.Collumn(db.Interger, primary_key=True)
    name = db.Collumn(db.String(120), nullable=False)
    price = db.Collumn(db.Float, nullable=False)
    description = db.Collunm(db.Text, nullable=True)

# Definir uma rota raiz (página inicial) e a função que será executada ao requisitar
@app.route('/')
def Hello_Word():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)
    