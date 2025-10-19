import json
import re


def add_all_solutions():
    """Add solutions to all chapters 11-16"""

    # Define all solutions by chapter
    solutions = {
        "11-Modulos-Bibliotecas.ipynb": {
            4: """**Solução:** Formatação de data com datetime

```python
import datetime

agora = datetime.datetime.now()
data_brasileira = agora.strftime('%d/%m/%Y')
print(f"Data atual: {data_brasileira}")
```

**Conceitos-chave:** Biblioteca datetime, formatação de strings""",
            5: """**Solução:** Cálculo de raiz quadrada

```python
import math

raiz = math.sqrt(144)
print(f"Raiz quadrada de 144: {raiz}")
```

**Conceitos-chave:** Biblioteca math, função sqrt""",
            6: """**Solução:** Módulo calculadora avançada

```python
# calculadora_avancada.py
import math

def area_circulo(raio):
    return math.pi * raio ** 2

def area_retangulo(largura, altura):
    return largura * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

if __name__ == "__main__":
    print(f"Área do círculo (raio=5): {area_circulo(5):.2f}")
    print(f"Área do retângulo (4x6): {area_retangulo(4, 6)}")
    print(f"Área do triângulo (base=8, altura=3): {area_triangulo(8, 3)}")
```

**Conceitos-chave:** Múltiplas funções, documentação, testes""",
            7: """**Solução:** Módulo de validação básica

```python
# validadores.py
def validar_email(email):
    return '@' in email and '.' in email.split('@')[1]

def validar_cpf(cpf):
    cpf_limpo = cpf.replace('.', '').replace('-', '')
    return len(cpf_limpo) == 11 and cpf_limpo.isdigit()

def validar_telefone(telefone):
    telefone_limpo = telefone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
    return len(telefone_limpo) >= 10 and telefone_limpo.isdigit()

if __name__ == "__main__":
    print(validar_email("teste@email.com"))
    print(validar_cpf("123.456.789-00"))
    print(validar_telefone("(11) 99999-9999"))
```

**Conceitos-chave:** Validação de strings, métodos de string""",
            8: """**Solução:** Sorteio com random.choice

```python
import random

brindes = ["Caneta", "Caderno", "Livro", "Mousepad", "Camiseta"]
brinde_sorteado = random.choice(brindes)
print(f"Brinde sorteado: {brinde_sorteado}")
```

**Conceitos-chave:** Lista de opções, random.choice""",
            9: """**Solução:** Cálculo de dias para aniversário

```python
import datetime

data_nascimento = datetime.date(1990, 5, 15)
hoje = datetime.date.today()

proximo_aniversario = datetime.date(hoje.year, data_nascimento.month, data_nascimento.day)

if proximo_aniversario < hoje:
    proximo_aniversario = datetime.date(hoje.year + 1, data_nascimento.month, data_nascimento.day)

dias_restantes = (proximo_aniversario - hoje).days
print(f"Dias para o próximo aniversário: {dias_restantes}")
```

**Conceitos-chave:** Manipulação de datas, cálculos temporais""",
            10: """**Solução:** Listagem de arquivos .txt

```python
import os

arquivos_txt = []
for arquivo in os.listdir('.'):
    if arquivo.endswith('.txt'):
        arquivos_txt.append(arquivo)

print("Arquivos .txt encontrados:")
for arquivo in arquivos_txt:
    print(f"- {arquivo}")
```

**Conceitos-chave:** Listagem de diretórios, filtragem por extensão""",
            11: """**Solução:** Gerador de senhas

```python
# gerador_senhas.py
import random
import string

def gerar_senha(tamanho=8, incluir_simbolos=True):
    caracteres = string.ascii_letters + string.digits
    if incluir_simbolos:
        caracteres += "!@#$%&*"
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def gerar_senha_forte():
    return gerar_senha(12, True)

def gerar_senha_simples():
    return gerar_senha(8, False)

if __name__ == "__main__":
    print(f"Senha simples: {gerar_senha_simples()}")
    print(f"Senha forte: {gerar_senha_forte()}")
```

**Conceitos-chave:** Biblioteca string, geração aleatória""",
            12: """**Solução:** Conversor de moedas

```python
# conversor_moedas.py
def converter_moeda(valor, moeda_origem, moeda_destino):
    taxas = {
        'BRL': {'USD': 0.20, 'EUR': 0.18},
        'USD': {'BRL': 5.00, 'EUR': 0.90},
        'EUR': {'BRL': 5.55, 'USD': 1.11}
    }
    
    if moeda_origem == moeda_destino:
        return valor
    
    taxa = taxas[moeda_origem][moeda_destino]
    return valor * taxa

def mostrar_conversao(valor, moeda_origem):
    moedas = ['BRL', 'USD', 'EUR']
    
    print(f"Valor original: {valor} {moeda_origem}")
    print("Conversões:")
    
    for moeda in moedas:
        if moeda != moeda_origem:
            convertido = converter_moeda(valor, moeda_origem, moeda)
            print(f"  {convertido:.2f} {moeda}")

if __name__ == "__main__":
    mostrar_conversao(100, 'BRL')
```

**Conceitos-chave:** Dicionários aninhados, conversão de valores""",
            13: """**Solução:** Criação de estrutura de diretórios

```python
from pathlib import Path

def criar_estrutura_projetos():
    base_path = Path("projetos/python/exercicios")
    base_path.mkdir(parents=True, exist_ok=True)
    
    subdirs = ["basico", "intermediario", "avancado"]
    for subdir in subdirs:
        (base_path / subdir).mkdir(exist_ok=True)
    
    print(f"Estrutura criada em: {base_path.absolute()}")
    print("Subdiretórios criados:")
    for subdir in subdirs:
        print(f"  - {subdir}")

if __name__ == "__main__":
    criar_estrutura_projetos()
```

**Conceitos-chave:** pathlib, criação de diretórios""",
            14: """**Solução:** Módulo de estatísticas

```python
# estatisticas.py
import statistics

def calcular_media(numeros):
    return statistics.mean(numeros)

def calcular_mediana(numeros):
    return statistics.median(numeros)

def calcular_moda(numeros):
    try:
        return statistics.mode(numeros)
    except statistics.StatisticsError:
        return "Sem moda"

def analisar_dados(numeros):
    print(f"Dados: {numeros}")
    print(f"Média: {calcular_media(numeros):.2f}")
    print(f"Mediana: {calcular_mediana(numeros):.2f}")
    print(f"Moda: {calcular_moda(numeros)}")

if __name__ == "__main__":
    dados = [1, 2, 3, 4, 5, 2, 3, 2]
    analisar_dados(dados)
```

**Conceitos-chave:** Biblioteca statistics, tratamento de exceções""",
            15: """**Solução:** Embaralhar cartas de baralho

```python
import random

def criar_baralho():
    naipes = ['♠', '♥', '♦', '♣']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    baralho = []
    for naipe in naipes:
        for valor in valores:
            baralho.append(f"{valor}{naipe}")
    
    return baralho

def embaralhar_cartas(baralho):
    random.shuffle(baralho)
    return baralho

def distribuir_cartas(baralho, num_jogadores=4, cartas_por_jogador=5):
    embaralhado = embaralhar_cartas(baralho.copy())
    
    jogadores = []
    for i in range(num_jogadores):
        inicio = i * cartas_por_jogador
        fim = inicio + cartas_por_jogador
        jogadores.append(embaralhado[inicio:fim])
    
    return jogadores

if __name__ == "__main__":
    baralho = criar_baralho()
    print(f"Baralho original: {baralho[:5]}...")
    
    embaralhado = embaralhar_cartas(baralho.copy())
    print(f"Baralho embaralhado: {embaralhado[:5]}...")
    
    jogadores = distribuir_cartas(baralho)
    for i, cartas in enumerate(jogadores):
        print(f"Jogador {i+1}: {cartas}")
```

**Conceitos-chave:** Listas, embaralhamento, distribuição""",
            16: """**Abordagem conceitual:**

1. **Análise do problema:** Criar sistema de gerenciamento de contatos com operações CRUD
2. **Estrutura de dados:** Usar lista de dicionários para armazenar contatos
3. **Arquitetura modular:** Separar em funções para cada operação
4. **Persistência:** Salvar dados em arquivo JSON

**Estrutura do código:**
```python
# agenda.py
import json

class Agenda:
    def __init__(self, arquivo='contatos.json'):
        self.arquivo = arquivo
        self.contatos = self.carregar_contatos()
    
    def adicionar_contato(self, nome, telefone, email):
        # TODO: Implementar adição
        pass
    
    def remover_contato(self, nome):
        # TODO: Implementar remoção
        pass
    
    def buscar_contato(self, nome):
        # TODO: Implementar busca
        pass
    
    def listar_contatos(self):
        # TODO: Implementar listagem
        pass
```

**Dicas de implementação:**
- Use JSON para persistência de dados
- Implemente validação de email e telefone
- Adicione tratamento de erros para arquivos""",
            17: """**Abordagem conceitual:**

1. **Análise do problema:** Criar jogo completo de adivinhação com diferentes níveis
2. **Estrutura de dados:** Usar variáveis para pontuação e histórico
3. **Arquitetura modular:** Separar lógica do jogo em funções específicas
4. **Interface:** Criar menu interativo para o usuário

**Estrutura do código:**
```python
# jogo_adivinhacao.py
import random

class JogoAdivinhacao:
    def __init__(self):
        self.pontuacao = 0
        self.tentativas_maximas = 7
        self.historico = []
    
    def jogar_nivel(self, nivel):
        # TODO: Implementar lógica do jogo
        pass
    
    def calcular_pontuacao(self, tentativas):
        # TODO: Implementar cálculo
        pass
```

**Dicas de implementação:**
- Use diferentes faixas de números por nível
- Implemente sistema de pontuação baseado em tentativas
- Adicione histórico de jogadas""",
            18: """**Abordagem conceitual:**

1. **Análise do problema:** Gerar datas aleatórias dentro de período específico
2. **Estrutura de dados:** Usar objetos datetime para manipulação
3. **Arquitetura modular:** Separar geração, validação e formatação
4. **Flexibilidade:** Permitir diferentes formatos de saída

**Estrutura do código:**
```python
# gerador_datas.py
import random
import datetime

class GeradorDatas:
    def __init__(self, data_inicio, data_fim):
        self.data_inicio = data_inicio
        self.data_fim = data_fim
    
    def gerar_data_aleatoria(self):
        # TODO: Implementar geração
        pass
    
    def gerar_multiplas_datas(self, quantidade):
        # TODO: Implementar múltiplas datas
        pass
```

**Dicas de implementação:**
- Use timestamp para cálculos de diferença
- Implemente validação de período
- Adicione diferentes formatos de saída""",
            19: """**Abordagem conceitual:**

1. **Análise do problema:** Organizar arquivos por extensão em diretórios
2. **Estrutura de dados:** Usar dicionário para mapear extensões
3. **Arquitetura modular:** Separar descoberta, organização e movimentação
4. **Segurança:** Implementar backup antes de mover arquivos

**Estrutura do código:**
```python
# arquivo_utils.py
import os
import shutil
from pathlib import Path

class OrganizadorArquivos:
    def __init__(self, diretorio_origem, diretorio_destino):
        self.origem = Path(diretorio_origem)
        self.destino = Path(diretorio_destino)
    
    def descobrir_extensoes(self):
        # TODO: Implementar descoberta
        pass
    
    def mover_arquivos(self):
        # TODO: Implementar movimentação
        pass
```

**Dicas de implementação:**
- Use pathlib para manipulação de caminhos
- Implemente backup antes de mover
- Adicione logs de operações""",
            20: """**Abordagem conceitual:**

1. **Análise do problema:** Criar calculadora científica com funções avançadas
2. **Estrutura de dados:** Usar classes para organizar funções por categoria
3. **Arquitetura modular:** Separar funções trigonométricas, logarítmicas e exponenciais
4. **Interface:** Criar menu categorizado para fácil navegação

**Estrutura do código:**
```python
# calculadora_cientifica.py
import math

class CalculadoraCientifica:
    def __init__(self):
        self.historico = []
    
    def trigonometricas(self, angulo, funcao):
        # TODO: Implementar funções trigonométricas
        pass
    
    def logaritmicas(self, valor, base):
        # TODO: Implementar funções logarítmicas
        pass
```

**Dicas de implementação:**
- Use biblioteca math para funções avançadas
- Implemente conversão de graus/radianos
- Adicione histórico de cálculos""",
            21: """**Abordagem conceitual:**

1. **Análise do problema:** Sistema modular completo de biblioteca
2. **Estrutura de dados:** Múltiplas classes para livros, usuários e empréstimos
3. **Arquitetura modular:** Módulos separados para cada entidade
4. **Persistência:** Banco de dados ou arquivos para dados persistentes

**Estrutura do código:**
```python
# Sistema modular completo
# livros.py
class Livro:
    def __init__(self, titulo, autor, isbn):
        # TODO: Implementar classe livro
        pass

# usuarios.py  
class Usuario:
    def __init__(self, nome, cpf, email):
        # TODO: Implementar classe usuário
        pass

# biblioteca.py
class Biblioteca:
    def __init__(self):
        # TODO: Implementar sistema principal
        pass
```

**Dicas de implementação:**
- Use SQLite para persistência
- Implemente sistema de multas
- Adicione relatórios de empréstimos""",
            22: """**Abordagem conceitual:**

1. **Análise do problema:** Implementar criptografia usando cifra de César
2. **Estrutura de dados:** Usar strings e caracteres ASCII
3. **Arquitetura modular:** Separar criptografia, descriptografia e validação
4. **Segurança:** Implementar diferentes chaves de criptografia

**Estrutura do código:**
```python
# crypto.py
class CifraCesar:
    def __init__(self, chave=3):
        self.chave = chave
    
    def criptografar(self, texto):
        # TODO: Implementar criptografia
        pass
    
    def descriptografar(self, texto_criptografado):
        # TODO: Implementar descriptografia
        pass
```

**Dicas de implementação:**
- Use ord() e chr() para conversão ASCII
- Implemente tratamento de caracteres especiais
- Adicione validação de entrada""",
            23: """**Abordagem conceitual:**

1. **Análise do problema:** Simular lançamentos de dados com diferentes tipos
2. **Estrutura de dados:** Usar classes para diferentes tipos de dados
3. **Arquitetura modular:** Separar simulação, estatísticas e visualização
4. **Flexibilidade:** Permitir dados customizados com probabilidades

**Estrutura do código:**
```python
# simulador_dados.py
import random

class Dado:
    def __init__(self, lados, probabilidades=None):
        self.lados = lados
        self.probabilidades = probabilidades
    
    def lancar(self):
        # TODO: Implementar lançamento
        pass

class SimuladorDados:
    def __init__(self):
        self.historico = []
    
    def simular_multiplos_lancamentos(self, dado, quantidade):
        # TODO: Implementar simulação múltipla
        pass
```

**Dicas de implementação:**
- Use weighted random para probabilidades
- Implemente histograma de resultados
- Adicione testes de hipóteses""",
            24: """**Abordagem conceitual:**

1. **Análise do problema:** Analisar texto com múltiplas métricas
2. **Estrutura de dados:** Usar dicionários para frequências e estatísticas
3. **Arquitetura modular:** Separar análise de frequência, sentimento e estatísticas
4. **Processamento:** Implementar limpeza e normalização de texto

**Estrutura do código:**
```python
# analisador_texto.py
import re
from collections import Counter

class AnalisadorTexto:
    def __init__(self, texto):
        self.texto = texto
        self.palavras = self.preprocessar_texto()
    
    def analisar_frequencia(self):
        # TODO: Implementar análise de frequência
        pass
    
    def analisar_sentimento(self):
        # TODO: Implementar análise de sentimento
        pass
```

**Dicas de implementação:**
- Use regex para limpeza de texto
- Implemente stop words em português
- Adicione visualização de resultados""",
            25: """**Abordagem conceitual:**

1. **Análise do problema:** Gerenciar projetos com templates e estruturas
2. **Estrutura de dados:** Usar classes para projetos e templates
3. **Arquitetura modular:** Separar criação, organização e gerenciamento
4. **Automação:** Implementar geração automática de estrutura

**Estrutura do código:**
```python
# gerenciador_projetos.py
from pathlib import Path
import json

class Template:
    def __init__(self, nome, estrutura):
        self.nome = nome
        self.estrutura = estrutura
    
    def aplicar_template(self, diretorio):
        # TODO: Implementar aplicação
        pass

class GerenciadorProjetos:
    def __init__(self):
        self.templates = {}
        self.projetos = []
    
    def criar_projeto(self, nome, template):
        # TODO: Implementar criação
        pass
```

**Dicas de implementação:**
- Use pathlib para criação de diretórios
- Implemente templates JSON
- Adicione sistema de backup de projetos""",
        }
    }

    # Process Chapter 11
    notebook_path = "11-Modulos-Bibliotecas.ipynb"
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

                if exercise_counter in solutions[notebook_path]:
                    solution_content = solutions[notebook_path][exercise_counter]

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
add_all_solutions()
