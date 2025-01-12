from flask import Flask, jsonify, request

# codigo que cria uma api de livros
# cada livro contém: id, título, autor

# FUNÇÕES:

# listar_livros() -> ['GET']
# pegar_livro(id) -> ['GET']
# editar_livro(id) -> ['PUT']
# add_livro() -> ['POST']
# del_livro(id) -> ['DELETE']

livros = [
    {
        'id': 1,
        'title': 'book 1',
        'author': 'author 1'
    },
    {
        'id': 2,
        'title': 'book 2',
        'author': 'author 2'
    }
]

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def homepage():
  return 'minha api'

@app.route('/livros', methods=['GET'])
def listar_livros():
  return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def pegar_livro(id):
  for livro in livros:
    if livro['id'] == id:
      return jsonify(livro)

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
  # obter informação enviada pelo usuário
  livro_alterado = request.get_json()
  for indice, livro in enumerate(livros):
    if livro['id'] == id:
      livros[indice].update(livro_alterado)
      return jsonify(livros[indice])

@app.route('/livros', methods=['POST'])
def add_livro():
  novo_livro = request.get_json()
  livros.append(novo_livro)
  return jsonify(livros)

@app.route('/livros/<int:id>', methods=['DELETE'])
def del_livro(id):
  for indice, livro in enumerate(livros):
    if livro['id'] == id:
      del livros[indice]
      return jsonify(livros)
      
app.run()
