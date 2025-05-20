from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = "minhachave_123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)
CORS(app)

# Login manager setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

# Carrega usuário pela sessão
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Criar usuário (registro)
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data.get("username") or not data.get("password"):
        return jsonify({"message": "Missing fields"}), 400

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"message": "User already exists"}), 409

    hashed_password = generate_password_hash(data["password"])
    new_user = User(username=data["username"], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

# Login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()

    if user and check_password_hash(user.password, data.get("password")):
        login_user(user)
        return jsonify({"message": "Logged in"}), 200

    return jsonify({"message": "Invalid credentials"}), 401

# Logout
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out"}), 200

# Add product
@app.route('/api/products/add', methods=["POST"])
@login_required
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': "Product added successfully"}), 201
    return jsonify({'message': "Invalid product data"}), 400

# Delete product
@app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
@login_required
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': "Product deleted successfully"}), 200
    return jsonify({'message': "Product not found"}), 404

# Get one product
@app.route('/api/products/<int:product_id>', methods=["GET"])
@login_required
def get_product(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        })
    return jsonify({"message": "Product not found"}), 404

# Update product
@app.route('/api/products/update/<int:product_id>', methods=["PUT"])
@login_required
def update_product(product_id):
    data = request.json
    product = Product.query.get(product_id)

    if product:
        product.name = data.get("name", product.name)
        product.price = data.get("price", product.price)
        product.description = data.get("description", product.description)
        db.session.commit()
        return jsonify({"message": "Product updated successfully"}), 200

    return jsonify({"message": "Product not found"}), 404

# List all products
@app.route('/api/products', methods=['GET'])
@login_required
def list_products():
    products = Product.query.all()
    product_list = [{
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "description": p.description
    } for p in products]
    return jsonify(product_list)

@app.route('/')
def home():
    return 'API E-commerce funcionando.'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
