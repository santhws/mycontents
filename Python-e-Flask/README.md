###
    from flask import Flask, request, jsonify
    from flask_sqlalchemy import SQLAlchemy


Essas duas bibliotecas:

**Flask →** é o framework web.</br>
**Flask_SQLAlchemy →** facilita a conexão com bancos de dados, usando o ORM SQLAlchemy.</br>

#

###
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'  
    db = SQLAlchemy(app)

Aqui você criou a aplicação **Flask**.</br>
Configurou o caminho do banco de dados **SQLite** *(ecommerce.db)*.</br>
Inicializou o **SQLAlchemy** para usar essa configuração.</br>

#

###
    class Product(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(120), nullable=False)
      price = db.Column(db.Float, nullable=False)
      description = db.Column(db.Text, nullable=True)

Esse trecho define a estrutura da tabela no banco de dados:

| Campo         | Tipo         | Obrigatório |
| ------------- | ------------ | ----------- |
| `id`          | Inteiro      | Sim (PK)    |
| `name`        | String (120) | Sim         |
| `price`       | Float        | Sim         |
| `description` | Texto        | Não         |

Cada produto será uma linha na tabela product.</br>
db.Model faz a ponte entre a classe Python e a tabela do banco.</br>

#

###

    @app.route('/api/products/add', methods=["POST"])
    def add_products():
      data = request.json
      if 'name' in data and 'price' in data:
      product = Product(name=data["name"], price=data["price"], description=data.get("description", ""))
          db.session.add(product)
          db.session.commit()
          return jsonify({'message': "Product added successfully"}), 201
      return jsonify({'message': "Invalid product data"}), 400

      Recebe dados JSON com name, price e opcionalmente description.

Verifica se os campos obrigatórios estão presentes.</br>
Cria um novo produto e salva no banco.</br>
Retorna uma resposta de sucesso (201) ou erro (400).</br>

#

###
    @app.route('/api/products/delete/<int:product_id>', methods=["DELETE"])
    def delete_product(product_id):
      product = Product.query.get(product_id)
      if product:
         db.session.delete(product)
         db.session.commit()
         return jsonify({'message': "Product deleted successfully"}), 200  
      return jsonify({'message': "Product not found"}), 404  

Pega o product_id da URL.</br>
Busca o produto no banco.</br>
Se existir, deleta e confirma no banco.</br>
Se não, retorna erro 404.</br>

#

###
    @app.route('/')
    def Hello_Word():
       return 'Hello World'

Serve como teste simples para saber se a API está online.</br>

#

###
    if __name__ == "__main__":
      with app.app_context():
          db.create_all()  
      app.run(debug=True

Cria as tabelas no banco se ainda não existirem (db.create_all()).</br>
Inicia o servidor com debug=True, o que ajuda durante o desenvolvimento (mostra erros no navegador).</br>

#





