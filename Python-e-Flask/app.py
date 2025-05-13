from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'  # configuração do banco de dados

db = SQLAlchemy(app)  # conexão do banco de dados

# Modelagem

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

@app.route('/api/products/add', methods=["POST"])
def add_products():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': "Product added successfully"}), 201
    return jsonify({'message': "Invalid product data"}), 400

@app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': "Product deleted successfully"}), 200  # Status 200 OK
    return jsonify({'message': "Product not found"}), 404  # Status 404 Not Found

# Definir uma rota raiz (página inicial) e a função que será executada ao requisitar

@app.route('/')
def Hello_Word():
    return 'Hello World'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Criar as tabelas no banco de dados, se ainda não existirem
    app.run(debug=True)
