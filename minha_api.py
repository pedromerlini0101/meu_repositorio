from flask import Flask, jsonify, request
from flask_cors import CORS

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
CORS(app)

@app.route('/')
def homepage():
  return 'minha api'

@app.route('/livros', methods=['GET'])
def listar_livros():
  # lista todos os livros do banco de dados
  return jsonify(livros)

@app.route('/livros/<int:id>', methods=['GET'])
def pegar_livro(id):
  # busca o livro com id esperado
  for livro in livros:
    if livro['id'] == id:
      return jsonify(livro)

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
  # obter informação enviada pelo usuário
  livro_alterado = request.get_json()
  # pega o livro e a sua posição na lista
  for indice, livro in enumerate(livros):
    # compara o id do livro com o id esperado
    if livro['id'] == id:
      # pega o livro achado e atualiza o conteúdo dele
      livros[indice].update(livro_alterado)
      return jsonify(livros[indice])

@app.route('/livros', methods=['POST'])
def add_livro():
  # pega a requisição e adiciona no banco de dados
  novo_livro = request.get_json()
  livros.append(novo_livro)
  return jsonify(livros)

@app.route('/livros/<int:id>', methods=['DELETE'])
def del_livro(id):
  # acha o livro com id esperado e deleta ele do banco de dados
  for indice, livro in enumerate(livros):
    if livro['id'] == id:
      del livros[indice]
      return jsonify(livros)
      
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))  # Define a porta dinamicamente
    app.run(host='0.0.0.0', port=port)  # 0.0.0.0 aceita conexões externas
