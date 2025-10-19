import json
import re

def create_solution_cell(exercise_num, nivel, chapter_topic, solution_type="full"):
    """Create a solution cell with appropriate content based on exercise level and type"""
    
    if solution_type == "conceptual":
        return create_conceptual_solution(exercise_num, nivel, chapter_topic)
    else:
        return create_full_solution(exercise_num, nivel, chapter_topic)

def create_full_solution(exercise_num, nivel, chapter_topic):
    """Create full code solution for levels 1-3"""
    
    solutions = {
        "modulos": {
            1: """**Solução:** Módulo básico com funções simples

```python
# cumprimentos.py
def dizer_oi():
    return "Olá!"

def dizer_tchau():
    return "Tchau!"

if __name__ == "__main__":
    print(dizer_oi())
```

**Conceitos-chave:** Definição de funções, `if __name__ == "__main__"`""",
            
            2: """**Solução:** Importação e uso de módulo

```python
# teste_cumprimentos.py
import cumprimentos

mensagem = cumprimentos.dizer_oi()
print(mensagem)
```

**Conceitos-chave:** Importação de módulos, uso de funções externas""",
            
            3: """**Solução:** Uso da biblioteca random

```python
import random

numero_sorteado = random.randint(1, 100)
print(f"Número sorteado: {numero_sorteado}")
```

**Conceitos-chave:** Biblioteca random, função randint""",
            
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
    """Calcula a área de um círculo"""
    return math.pi * raio ** 2

def area_retangulo(largura, altura):
    """Calcula a área de um retângulo"""
    return largura * altura

def area_triangulo(base, altura):
    """Calcula a área de um triângulo"""
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
    """Validação básica de email"""
    return '@' in email and '.' in email.split('@')[1]

def validar_cpf(cpf):
    """Validação básica de CPF (apenas formato)"""
    cpf_limpo = cpf.replace('.', '').replace('-', '')
    return len(cpf_limpo) == 11 and cpf_limpo.isdigit()

def validar_telefone(telefone):
    """Validação básica de telefone"""
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

# Substitua pela sua data de nascimento
data_nascimento = datetime.date(1990, 5, 15)
hoje = datetime.date.today()

# Calcular próximo aniversário
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
    """Gera senha aleatória com diferentes níveis de segurança"""
    caracteres = string.ascii_letters + string.digits
    if incluir_simbolos:
        caracteres += "!@#$%&*"
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def gerar_senha_forte():
    """Gera senha forte com símbolos"""
    return gerar_senha(12, True)

def gerar_senha_simples():
    """Gera senha simples sem símbolos"""
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
    """Converte valores entre moedas (valores fictícios)"""
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
    """Mostra conversão para todas as moedas"""
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
    """Cria estrutura de diretórios para projetos Python"""
    base_path = Path("projetos/python/exercicios")
    
    # Criar diretórios (parents=True cria diretórios pai se não existirem)
    base_path.mkdir(parents=True, exist_ok=True)
    
    # Criar subdiretórios
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
    """Calcula a média de uma lista de números"""
    return statistics.mean(numeros)

def calcular_mediana(numeros):
    """Calcula a mediana de uma lista de números"""
    return statistics.median(numeros)

def calcular_moda(numeros):
    """Calcula a moda de uma lista de números"""
    try:
        return statistics.mode(numeros)
    except statistics.StatisticsError:
        return "Sem moda"

def analisar_dados(numeros):
    """Análise completa dos dados"""
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
    """Cria um baralho completo"""
    naipes = ['♠', '♥', '♦', '♣']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    baralho = []
    for naipe in naipes:
        for valor in valores:
            baralho.append(f"{valor}{naipe}")
    
    return baralho

def embaralhar_cartas(baralho):
    """Embaralha as cartas"""
    random.shuffle(baralho)
    return baralho

def distribuir_cartas(baralho, num_jogadores=4, cartas_por_jogador=5):
    """Distribui cartas para os jogadores"""
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

**Conceitos-chave:** Listas, embaralhamento, distribuição"""
        }
    }
    
    # Get solution based on chapter topic and exercise number
    if chapter_topic == "modulos" and exercise_num in solutions["modulos"]:
        return solutions["modulos"][exercise_num]
    else:
        return f"**Solução {exercise_num}:** Implementação completa para nível {nivel}\n\n```python\n# Código da solução aqui\npass\n```\n\n**Conceitos-chave:** Conceitos importantes da solução"

def create_conceptual_solution(exercise_num, nivel, chapter_topic):
    """Create conceptual solution for levels 4-5"""
    
    return f"""**Abordagem conceitual:**

1. **Análise do problema:** Identificar os componentes principais necessários
2. **Estrutura de dados:** Definir como organizar e armazenar as informações
3. **Arquitetura modular:** Dividir em funções e módulos especializados
4. **Integração:** Conectar os componentes de forma eficiente

**Estrutura do código:**
```python
# Componentes principais necessários
def main_function():
    # TODO: Implementar lógica principal
    pass

def helper_function_1():
    # TODO: Implementar função auxiliar
    pass

def helper_function_2():
    # TODO: Implementar função auxiliar
    pass

# Estrutura de dados principal
class MainClass:
    def __init__(self):
        # TODO: Inicializar atributos
        pass
    
    def method_1(self):
        # TODO: Implementar método
        pass
```

**Dicas de implementação:**
- Use bibliotecas apropriadas para o nível de complexidade
- Implemente validação de dados robusta
- Considere tratamento de erros e casos extremos
- Documente bem o código para facilitar manutenção"""

def add_solutions_to_notebook(notebook_path, chapter_topic):
    """Add solutions to a notebook file"""
    
    print(f"Processing {notebook_path}...")
    
    # Load notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Track exercise numbers
    exercise_counter = 0
    nivel_counter = 0
    current_nivel = 1
    
    # Process cells
    new_cells = []
    
    for i, cell in enumerate(data['cells']):
        new_cells.append(cell)
        
        if cell['cell_type'] == 'markdown':
            source_text = ''.join(cell['source'])
            
            # Check if this is an exercise cell
            if re.search(r'Exercício \d+:', source_text) or re.search(r'\*\*\d+\.\*\*', source_text):
                exercise_counter += 1
                
                # Determine if this is a new nivel
                if 'Nível' in source_text and 'exercícios' in source_text:
                    nivel_match = re.search(r'Nível (\d+)', source_text)
                    if nivel_match:
                        current_nivel = int(nivel_match.group(1))
                
                # Determine solution type based on nivel
                solution_type = "conceptual" if current_nivel >= 4 else "full"
                
                # Create solution cell
                solution_content = create_solution_cell(exercise_counter, current_nivel, chapter_topic, solution_type)
                
                solution_cell = {
                    "cell_type": "markdown",
                    "id": f"solution-{exercise_counter}",
                    "metadata": {},
                    "source": [f"::: {{.callout-note title=\"Gabarito\" collapse=\"true\"}}\n\n{solution_content}\n\n:::"]
                }
                
                new_cells.append(solution_cell)
                print(f"  Added solution for exercise {exercise_counter} (Nível {current_nivel})")
    
    # Update notebook with new cells
    data['cells'] = new_cells
    
    # Save notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    
    print(f"Completed {notebook_path}")

# Process all chapters
chapters = [
    ("11-Modulos-Bibliotecas.ipynb", "modulos"),
    ("12-APIs-Parte1-Consumo.ipynb", "apis_consumo"),
    ("13-APIs-Parte2-Criacao.ipynb", "apis_criacao"),
    ("14-Web-Scraping.ipynb", "web_scraping"),
    ("15-Banco-Dados-SQL.ipynb", "sql"),
    ("16-Expressoes-Regulares.ipynb", "regex")
]

for notebook_path, chapter_topic in chapters:
    add_solutions_to_notebook(notebook_path, chapter_topic)

print("\nAll chapters processed!")
