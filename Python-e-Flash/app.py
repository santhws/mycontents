# Importação 
from flask import Flask

app = Flask(__name__)

# Definir uma rota raiz (página inicial) e a função que será executada ao requisitar
@app.route('/')
def Hello_Word():
    return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)


