import json
import re


def add_solutions_chapters_13_16():
    """Add solutions for chapters 13-16"""

    chapters = {
        "13-APIs-Parte2-Criacao.ipynb": {
            1: """**Solução:** Servidor Flask básico

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/sobre')
def sobre():
    return "Esta é uma página sobre nós"

if __name__ == '__main__':
    app.run(debug=True)
```

**Conceitos-chave:** Flask, rotas, decoradores""",
            2: """**Solução:** API que retorna JSON

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/usuario')
def get_usuario():
    usuario = {
        'nome': 'João Silva',
        'email': 'joao@email.com',
        'idade': 30
    }
    return jsonify(usuario)

@app.route('/api/produtos')
def get_produtos():
    produtos = [
        {'id': 1, 'nome': 'Notebook', 'preco': 2500},
        {'id': 2, 'nome': 'Mouse', 'preco': 50}
    ]
    return jsonify(produtos)

if __name__ == '__main__':
    app.run(debug=True)
```

**Conceitos-chave:** jsonify, APIs REST, estruturas de dados""",
            3: """**Solução:** API com parâmetros

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/usuario/<int:user_id>')
def get_usuario_por_id(user_id):
    usuarios = {
        1: {'nome': 'João', 'email': 'joao@email.com'},
        2: {'nome': 'Maria', 'email': 'maria@email.com'}
    }
    
    if user_id in usuarios:
        return jsonify(usuarios[user_id])
    else:
        return jsonify({'erro': 'Usuário não encontrado'}), 404

@app.route('/api/buscar')
def buscar():
    query = request.args.get('q', '')
    return jsonify({'busca': query, 'resultados': []})

if __name__ == '__main__':
    app.run(debug=True)
```

**Conceitos-chave:** Parâmetros de URL, query parameters, tratamento de erros""",
            4: """**Solução:** API com métodos HTTP

```python
from flask import Flask, jsonify, request

app = Flask(__name__)
tarefas = []

@app.route('/api/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/api/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()
    nova_tarefa = {
        'id': len(tarefas) + 1,
        'titulo': dados['titulo'],
        'concluida': False
    }
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

if __name__ == '__main__':
    app.run(debug=True)
```

**Conceitos-chave:** Métodos HTTP, POST, GET, request.get_json()""",
            5: """**Solução:** API completa CRUD

```python
from flask import Flask, jsonify, request

app = Flask(__name__)
livros = [
    {'id': 1, 'titulo': 'Python Básico', 'autor': 'João Silva'},
    {'id': 2, 'titulo': 'Flask Avançado', 'autor': 'Maria Santos'}
]

@app.route('/api/livros', methods=['GET'])
def listar_livros():
    return jsonify(livros)

@app.route('/api/livros/<int:livro_id>', methods=['GET'])
def buscar_livro(livro_id):
    livro = next((l for l in livros if l['id'] == livro_id), None)
    if livro:
        return jsonify(livro)
    return jsonify({'erro': 'Livro não encontrado'}), 404

@app.route('/api/livros', methods=['POST'])
def criar_livro():
    dados = request.get_json()
    novo_livro = {
        'id': max([l['id'] for l in livros]) + 1,
        'titulo': dados['titulo'],
        'autor': dados['autor']
    }
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

@app.route('/api/livros/<int:livro_id>', methods=['PUT'])
def atualizar_livro(livro_id):
    dados = request.get_json()
    livro = next((l for l in livros if l['id'] == livro_id), None)
    if livro:
        livro.update(dados)
        return jsonify(livro)
    return jsonify({'erro': 'Livro não encontrado'}), 404

@app.route('/api/livros/<int:livro_id>', methods=['DELETE'])
def deletar_livro(livro_id):
    global livros
    livros = [l for l in livros if l['id'] != livro_id]
    return jsonify({'mensagem': 'Livro deletado'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```

**Conceitos-chave:** CRUD completo, PUT, DELETE, tratamento de dados""",
        },
        "14-Web-Scraping.ipynb": {
            1: """**Solução:** Extrair títulos H1

```python
from bs4 import BeautifulSoup

html = '''
<html>
<head><title>Minha Página</title></head>
<body>
    <h1>Título Principal</h1>
    <h1>Outro Título</h1>
    <p>Parágrafo normal</p>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
titulos = soup.find_all('h1')

for titulo in titulos:
    print(titulo.text)
```

**Conceitos-chave:** BeautifulSoup, find_all, extração de texto""",
            2: """**Solução:** Extrair links

```python
from bs4 import BeautifulSoup

html = '''
<html>
<body>
    <a href="https://www.google.com">Google</a>
    <a href="https://www.github.com">GitHub</a>
    <a href="/pagina-local">Página Local</a>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')

for link in links:
    print(f"Texto: {link.text}, URL: {link['href']}")
```

**Conceitos-chave:** Extração de atributos, links, href""",
            3: """**Solução:** Contar imagens

```python
from bs4 import BeautifulSoup

html = '''
<html>
<body>
    <img src="imagem1.jpg" alt="Primeira imagem">
    <img src="imagem2.png" alt="Segunda imagem">
    <img src="imagem3.gif" alt="Terceira imagem">
    <p>Texto normal</p>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
imagens = soup.find_all('img')

print(f"Total de imagens: {len(imagens)}")
for img in imagens:
    print(f"Alt: {img.get('alt', 'Sem alt')}")
```

**Conceitos-chave:** Contagem de elementos, atributos opcionais""",
            4: """**Solução:** Extrair parágrafos

```python
from bs4 import BeautifulSoup

html = '''
<html>
<body>
    <p>Primeiro parágrafo com texto importante.</p>
    <p>Segundo parágrafo com mais informações.</p>
    <div>Div não é parágrafo</div>
    <p>Terceiro parágrafo final.</p>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
paragrafos = soup.find_all('p')

for i, p in enumerate(paragrafos, 1):
    print(f"Parágrafo {i}: {p.text.strip()}")
```

**Conceitos-chave:** Extração de texto, strip(), enumeração""",
            5: """**Solução:** Buscar por classe CSS

```python
from bs4 import BeautifulSoup

html = '''
<html>
<body>
    <div class="produto">Notebook - R$ 2500</div>
    <div class="produto">Mouse - R$ 50</div>
    <div class="categoria">Eletrônicos</div>
    <div class="produto">Teclado - R$ 100</div>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
produtos = soup.find_all('div', class_='produto')

for produto in produtos:
    print(produto.text)
```

**Conceitos-chave:** Seletores por classe, class_ parameter""",
        },
        "15-Banco-Dados-SQL.ipynb": {
            1: """**Solução:** Criar tabela livros

```python
import sqlite3

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE livros (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    preco REAL
)
''')

conn.commit()
conn.close()
print("Tabela livros criada com sucesso!")
```

**Conceitos-chave:** CREATE TABLE, tipos de dados SQLite""",
            2: """**Solução:** Inserir livros

```python
import sqlite3

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

livros = [
    ('Python Básico', 'João Silva', 2023, 50.00),
    ('Flask Avançado', 'Maria Santos', 2022, 75.00),
    ('SQL Completo', 'Pedro Costa', 2023, 60.00)
]

cursor.executemany('''
INSERT INTO livros (titulo, autor, ano, preco)
VALUES (?, ?, ?, ?)
''', livros)

conn.commit()
conn.close()
print("Livros inseridos com sucesso!")
```

**Conceitos-chave:** INSERT, executemany, parâmetros""",
            3: """**Solução:** Listar todos os livros

```python
import sqlite3

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM livros')
livros = cursor.fetchall()

print("Todos os livros:")
for livro in livros:
    print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Preço: R$ {livro[4]}")

conn.close()
```

**Conceitos-chave:** SELECT, fetchall, iteração""",
            4: """**Solução:** Buscar por autor

```python
import sqlite3

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

autor = 'João Silva'
cursor.execute('SELECT * FROM livros WHERE autor = ?', (autor,))
livros = cursor.fetchall()

print(f"Livros do autor {autor}:")
for livro in livros:
    print(f"- {livro[1]} ({livro[3]})")

conn.close()
```

**Conceitos-chave:** WHERE, parâmetros, filtros""",
            5: """**Solução:** Contar livros

```python
import sqlite3

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

cursor.execute('SELECT COUNT(*) FROM livros')
total = cursor.fetchone()[0]

print(f"Total de livros na biblioteca: {total}")

conn.close()
```

**Conceitos-chave:** COUNT, fetchone, agregação""",
        },
        "16-Expressoes-Regulares.ipynb": {
            1: """**Solução:** Validar email básico

```python
import re

def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(padrao, email))

# Testando
emails = ['teste@email.com', 'usuario123@gmail.com', 'email.invalido']
for email in emails:
    print(f"{email}: {'Válido' if validar_email(email) else 'Inválido'}")
```

**Conceitos-chave:** Regex básica, validação de email""",
            2: """**Solução:** Validar telefone brasileiro

```python
import re

def validar_telefone(telefone):
    # Aceita formatos: (11) 99999-9999, 11 99999-9999, 11999999999
    padrao = r'^\(?(\d{2})\)?\s?(\d{4,5})-?(\d{4})$'
    return bool(re.match(padrao, telefone))

# Testando
telefones = ['(11) 99999-9999', '11 99999-9999', '11999999999', '123']
for tel in telefones:
    print(f"{tel}: {'Válido' if validar_telefone(tel) else 'Inválido'}")
```

**Conceitos-chave:** Regex com grupos, telefones brasileiros""",
            3: """**Solução:** Validar CPF básico

```python
import re

def validar_cpf_formato(cpf):
    # Remove pontos e traços
    cpf_limpo = re.sub(r'[.-]', '', cpf)
    # Verifica se tem 11 dígitos
    return bool(re.match(r'^\d{11}$', cpf_limpo))

# Testando
cpfs = ['123.456.789-00', '12345678900', '123.456.789-0', 'abc']
for cpf in cpfs:
    print(f"{cpf}: {'Válido' if validar_cpf_formato(cpf) else 'Inválido'}")
```

**Conceitos-chave:** Limpeza de dados, validação de formato""",
            4: """**Solução:** Extrair números de texto

```python
import re

def extrair_numeros(texto):
    padrao = r'\d+'
    numeros = re.findall(padrao, texto)
    return [int(n) for n in numeros]

# Testando
texto = "Tenho 25 anos e 150 reais na conta. Meu telefone é 11999999999."
numeros = extrair_numeros(texto)
print(f"Números encontrados: {numeros}")
```

**Conceitos-chave:** findall, extração de números""",
            5: """**Solução:** Buscar por classe CSS

```python
import re

def encontrar_palavras_palindromos(texto):
    palavras = re.findall(r'\b\w+\b', texto.lower())
    palindromos = []
    
    for palavra in palavras:
        if palavra == palavra[::-1] and len(palavra) > 2:
            palindromos.append(palavra)
    
    return palindromos

# Testando
texto = "A palavra ovo é um palindromo. Ana também. Python não é."
palindromos = encontrar_palavras_palindromos(texto)
print(f"Palíndromos encontrados: {palindromos}")
```

**Conceitos-chave:** findall, palíndromos, manipulação de strings""",
        },
    }

    # Process each chapter
    for notebook_path, solutions in chapters.items():
        print(f"Processing {notebook_path}...")

        # Load notebook
        with open(notebook_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Add solutions
        new_cells = []
        exercise_counter = 0

        for i, cell in enumerate(data["cells"]):
            new_cells.append(cell)

            if cell["cell_type"] == "markdown":
                source_text = "".join(cell["source"])

                # Check if this is an exercise cell
                if re.search(r"\*\*\d+\.\*\*", source_text):
                    exercise_counter += 1

                    if exercise_counter in solutions:
                        solution_content = solutions[exercise_counter]

                        solution_cell = {
                            "cell_type": "markdown",
                            "id": f"solution-{exercise_counter}",
                            "metadata": {},
                            "source": [
                                f'::: {{.callout-note title="Gabarito" collapse="true"}}\n\n{solution_content}\n\n:::'
                            ],
                        }

                        new_cells.append(solution_cell)
                        print(f"  Added solution for exercise {exercise_counter}")

        # Update notebook
        data["cells"] = new_cells

        # Save notebook
        with open(notebook_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)

        print(f"Completed {notebook_path}")


# Run the function
add_solutions_chapters_13_16()
