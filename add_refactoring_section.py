import json

# Add refactoring section to Chapter 6
notebook_path = "06-Funcoes.ipynb"

# Load notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Find the references cell (should be around cell 26)
refactoring_content = """## Refatoração: Melhorando o Código Existente

### O que é Refatoração?

**Refatoração** é o processo de melhorar a estrutura interna do código sem alterar seu comportamento externo. É como reformar uma casa: você melhora a organização, a eficiência e a manutenibilidade, mas a casa continua funcionando da mesma forma para quem mora nela.

> 💡 **Analogia:** Imagine que você tem uma receita de bolo que funciona, mas está desorganizada. Refatorar seria reorganizar os ingredientes por categoria, simplificar os passos e tornar a receita mais clara - mas o bolo final continua o mesmo!

### Por que Refatorar?

**Problemas comuns que a refatoração resolve:**

- 🔄 **Código duplicado:** Mesmo código repetido em vários lugares
- 🧩 **Funções muito grandes:** Funções que fazem muitas coisas diferentes
- 📝 **Nomes confusos:** Variáveis e funções com nomes que não explicam o que fazem
- 🏗️ **Estrutura confusa:** Código difícil de entender e manter

### Exemplo Prático: Antes e Depois

**❌ Código antes da refatoração (problemático):**

```python
# Código repetitivo e confuso
nome1 = input("Digite o primeiro nome: ")
idade1 = int(input("Digite a primeira idade: "))
print(f"O primeiro usuário é {nome1} e tem {idade1} anos")

nome2 = input("Digite o segundo nome: ")
idade2 = int(input("Digite a segunda idade: "))
print(f"O segundo usuário é {nome2} e tem {idade2} anos")

nome3 = input("Digite o terceiro nome: ")
idade3 = int(input("Digite a terceira idade: "))
print(f"O terceiro usuário é {nome3} e tem {idade3} anos")
```

**✅ Código após refatoração (melhorado):**

```python
# Código organizado e reutilizável
def coletar_dados_usuario():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    return nome, idade

def exibir_usuario(nome, idade):
    print(f"O usuário é {nome} e tem {idade} anos")

# Usando as funções
for i in range(3):
    nome, idade = coletar_dados_usuario()
    exibir_usuario(nome, idade)
```

### Benefícios da Refatoração

**1. Reutilização de Código**
- Evita repetição desnecessária
- Facilita manutenção e correção de bugs

**2. Legibilidade**
- Código mais fácil de entender
- Nomes descritivos e estrutura clara

**3. Manutenibilidade**
- Mudanças futuras são mais simples
- Menos chance de introduzir erros

**4. Testabilidade**
- Funções pequenas são mais fáceis de testar
- Comportamento isolado e previsível

### Técnicas de Refatoração Comuns

**1. Extrair Função (Extract Function)**
```python
# Antes: código misturado
def processar_pedido():
    nome = input("Nome: ")
    # ... código longo ...
    total = calcular_total()
    print(f"Pedido de {nome}: R$ {total}")

# Depois: função extraída
def coletar_nome():
    return input("Nome: ")

def processar_pedido():
    nome = coletar_nome()
    total = calcular_total()
    print(f"Pedido de {nome}: R$ {total}")
```

**2. Renomear Variáveis**
```python
# Antes: nomes confusos
x = input("Digite sua idade: ")
y = int(x)

# Depois: nomes claros
idade_texto = input("Digite sua idade: ")
idade_numero = int(idade_texto)
```

**3. Simplificar Condições**
```python
# Antes: condição complexa
if idade >= 18 and idade <= 65 and tem_carteira == True:
    print("Pode dirigir")

# Depois: condição clara
def pode_dirigir(idade, tem_carteira):
    return idade >= 18 and idade <= 65 and tem_carteira

if pode_dirigir(idade, tem_carteira):
    print("Pode dirigir")
```

### Quando Refatorar?

**✅ Boas oportunidades para refatorar:**
- Quando você encontra código duplicado
- Antes de adicionar uma nova funcionalidade
- Quando o código está difícil de entender
- Quando você precisa corrigir um bug

**⚠️ Cuidados:**
- Sempre teste o código antes e depois da refatoração
- Faça mudanças pequenas e incrementais
- Mantenha o comportamento externo inalterado

### Ferramentas que Ajudam

**1. IDEs Modernas**
- PyCharm, VS Code detectam código duplicado
- Sugerem renomeações e extrações

**2. Testes Automatizados**
- Garantem que a refatoração não quebrou nada
- Permitem refatorar com confiança

**3. Controle de Versão**
- Git permite desfazer mudanças se algo der errado
- Facilita comparação antes/depois

### Exemplo Completo: Refatoração Passo a Passo

**Situação:** Você tem um programa que calcula estatísticas de notas, mas está todo misturado em uma função gigante.

**Passo 1: Identificar o problema**
```python
def programa_notas():
    # 50 linhas de código misturado
    notas = []
    for i in range(5):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)
    
    soma = 0
    for nota in notas:
        soma += nota
    media = soma / len(notas)
    
    maior = notas[0]
    for nota in notas:
        if nota > maior:
            maior = nota
    
    print(f"Média: {media}")
    print(f"Maior nota: {maior}")
```

**Passo 2: Extrair funções específicas**
```python
def coletar_notas(quantidade):
    notas = []
    for i in range(quantidade):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)
    return notas

def calcular_media(notas):
    return sum(notas) / len(notas)

def encontrar_maior_nota(notas):
    return max(notas)

def exibir_resultados(media, maior_nota):
    print(f"Média: {media}")
    print(f"Maior nota: {maior_nota}")

def programa_notas():
    notas = coletar_notas(5)
    media = calcular_media(notas)
    maior_nota = encontrar_maior_nota(notas)
    exibir_resultados(media, maior_nota)
```

**Resultado:** Código mais organizado, testável e reutilizável!

### Dicas Finais

1. **Refatore frequentemente:** Não espere o código ficar muito bagunçado
2. **Faça mudanças pequenas:** Uma refatoração por vez
3. **Teste sempre:** Garanta que nada quebrou
4. **Use nomes descritivos:** O código deve ser autoexplicativo
5. **Mantenha funções pequenas:** Uma função, uma responsabilidade

> 🎯 **Lembre-se:** Refatoração não é sobre escrever código novo, é sobre tornar o código existente melhor. É uma habilidade essencial para qualquer programador profissional!"""

# Create new cell for refactoring section
new_cell = {
    "cell_type": "markdown",
    "id": "refactoring-section",
    "metadata": {},
    "source": refactoring_content.split("\n"),
}

# Insert the new cell before the references (around cell 26)
# Find the references cell
for i, cell in enumerate(data["cells"]):
    if cell["cell_type"] == "markdown" and "source" in cell:
        source_text = "".join(cell["source"])
        if "Referências bibliográficas" in source_text:
            # Insert before this cell
            data["cells"].insert(i, new_cell)
            print(f"Added refactoring section before cell {i}")
            break

# Save notebook
with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print("Done!")
