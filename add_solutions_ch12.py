import json
import re


def add_solutions_chapter_12():
    """Add solutions for Chapter 12 - APIs Parte 1 - Consumo"""

    notebook_path = "12-APIs-Parte1-Consumo.ipynb"
    print(f"Processing {notebook_path}...")

    # Solutions for Chapter 12 exercises
    solutions = {
        1: """**Solução:** Informações básicas do GitHub

```python
import requests

def info_github_basica(username):
    url = f'https://api.github.com/users/{username}'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            print(f"Nome: {dados['name']}")
            print(f"Seguidores: {dados['followers']}")
            return dados
        else:
            print(f"Usuário não encontrado: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None

# Testando
info_github_basica('octocat')
```

**Conceitos-chave:** requests.get(), tratamento de erros, status codes""",
        2: """**Solução:** Buscar CEP específico

```python
def buscar_cep_especifico():
    cep = '20040-020'
    url = f'https://viacep.com.br/ws/{cep}/json/'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()
            print(f"📍 {dados['logradouro']}, {dados['bairro']}")
            print(f"📍 {dados['localidade']} - {dados['uf']}")
            return dados
        else:
            print(f"Erro: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None

# Testando
buscar_cep_especifico()
```

**Conceitos-chave:** API ViaCEP, formatação de URLs, tratamento de dados""",
        3: """**Solução:** Preço do Bitcoin

```python
def preco_bitcoin():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {'ids': 'bitcoin', 'vs_currencies': 'usd,brl'}
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            dados = response.json()
            preco_usd = dados['bitcoin']['usd']
            preco_brl = dados['bitcoin']['brl']
            
            print(f"💰 Bitcoin")
            print(f"💵 USD: ${preco_usd:,.2f}")
            print(f"🇧🇷 BRL: R$ {preco_brl:,.2f}")
            return dados
        else:
            print(f"Erro: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None

# Testando
preco_bitcoin()
```

**Conceitos-chave:** Parâmetros de URL, formatação de números, múltiplas moedas""",
        4: """**Solução:** Listar posts do JSONPlaceholder

```python
def listar_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            posts = response.json()
            
            print(f"Total de posts: {len(posts)}")
            print("\\nPrimeiros 3 posts:")
            
            for i, post in enumerate(posts[:3]):
                print(f"{i+1}. {post['title']}")
                print(f"   ID: {post['id']}, User: {post['userId']}")
                print()
            
            return posts
        else:
            print(f"Erro: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None

# Testando
listar_posts()
```

**Conceitos-chave:** Lista de dados, iteração, formatação de saída""",
        5: """**Solução:** Buscar post específico

```python
def buscar_post_especifico(post_id):
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            post = response.json()
            
            print(f"📝 Título: {post['title']}")
            print(f"👤 Autor ID: {post['userId']}")
            print(f"📄 Conteúdo: {post['body']}")
            
            return post
        else:
            print(f"Post não encontrado: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None

# Testando
buscar_post_especifico(1)
```

**Conceitos-chave:** URLs dinâmicas, dados específicos, formatação de conteúdo""",
        6: """**Solução:** API de clima com tratamento de erros

```python
def consultar_clima(cidade, api_key):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': cidade,
        'appid': api_key,
        'units': 'metric',
        'lang': 'pt_br'
    }
    
    try:
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            dados = response.json()
            
            print(f"🌤️ Clima em {dados['name']}")
            print(f"🌡️ Temperatura: {dados['main']['temp']}°C")
            print(f"💧 Umidade: {dados['main']['humidity']}%")
            print(f"🌬️ Vento: {dados['wind']['speed']} m/s")
            
            return dados
        elif response.status_code == 404:
            print("Cidade não encontrada")
            return None
        else:
            print(f"Erro da API: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None

# Exemplo de uso (substitua pela sua API key)
# clima = consultar_clima('São Paulo', 'sua_api_key_aqui')
```

**Conceitos-chave:** Parâmetros múltiplos, tratamento de diferentes status codes""",
        7: """**Solução:** Buscar múltiplos usuários do GitHub

```python
def buscar_multiplos_usuarios(usernames):
    resultados = {}
    
    for username in usernames:
        url = f'https://api.github.com/users/{username}'
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                dados = response.json()
                resultados[username] = {
                    'nome': dados['name'],
                    'seguidores': dados['followers'],
                    'repositorios': dados['public_repos']
                }
            else:
                resultados[username] = {'erro': f'Status {response.status_code}'}
                
        except requests.exceptions.RequestException as e:
            resultados[username] = {'erro': str(e)}
    
    return resultados

# Testando
usuarios = ['octocat', 'torvalds', 'gvanrossum']
resultados = buscar_multiplos_usuarios(usuarios)

for usuario, dados in resultados.items():
    if 'erro' in dados:
        print(f"❌ {usuario}: {dados['erro']}")
    else:
        print(f"✅ {usuario}: {dados['nome']} - {dados['seguidores']} seguidores")
```

**Conceitos-chave:** Loop através de múltiplas requisições, dicionários de resultados""",
        8: """**Solução:** Salvar dados de API em arquivo

```python
import json

def salvar_dados_api():
    # Buscar dados
    url = 'https://jsonplaceholder.typicode.com/users'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            usuarios = response.json()
            
            # Processar dados
            dados_processados = []
            for usuario in usuarios:
                dados_processados.append({
                    'nome': usuario['name'],
                    'email': usuario['email'],
                    'cidade': usuario['address']['city'],
                    'empresa': usuario['company']['name']
                })
            
            # Salvar em arquivo
            with open('usuarios_api.json', 'w', encoding='utf-8') as f:
                json.dump(dados_processados, f, ensure_ascii=False, indent=2)
            
            print(f"✅ Dados salvos: {len(dados_processados)} usuários")
            return dados_processados
            
        else:
            print(f"Erro: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None

# Testando
salvar_dados_api()
```

**Conceitos-chave:** Processamento de dados, salvamento em JSON, estruturação de dados""",
        9: """**Solução:** API com autenticação básica

```python
def api_com_auth():
    # Exemplo com API que requer autenticação
    url = 'https://httpbin.org/basic-auth/user/pass'
    
    try:
        # Autenticação básica
        response = requests.get(url, auth=('user', 'pass'))
        
        if response.status_code == 200:
            dados = response.json()
            print("✅ Autenticação bem-sucedida!")
            print(f"Dados: {dados}")
            return dados
        else:
            print(f"❌ Falha na autenticação: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None

# Testando
api_com_auth()
```

**Conceitos-chave:** Autenticação básica, headers de autorização""",
        10: """**Solução:** Monitorar status de sites

```python
import time

def monitorar_sites(sites):
    resultados = {}
    
    for site in sites:
        try:
            inicio = time.time()
            response = requests.get(site, timeout=10)
            fim = time.time()
            
            tempo_resposta = fim - inicio
            
            resultados[site] = {
                'status': response.status_code,
                'tempo_resposta': round(tempo_resposta, 2),
                'online': response.status_code == 200
            }
            
        except requests.exceptions.RequestException as e:
            resultados[site] = {
                'status': 'erro',
                'tempo_resposta': None,
                'online': False,
                'erro': str(e)
            }
    
    return resultados

# Testando
sites = [
    'https://httpbin.org/status/200',
    'https://httpbin.org/status/404',
    'https://httpbin.org/delay/2'
]

resultados = monitorar_sites(sites)

for site, dados in resultados.items():
    if dados['online']:
        print(f"✅ {site}: {dados['status']} ({dados['tempo_resposta']}s)")
    else:
        print(f"❌ {site}: {dados.get('erro', 'Erro desconhecido')}")
```

**Conceitos-chave:** Múltiplas requisições, medição de tempo, timeout""",
        11: """**Solução:** Sistema de monitoramento de preços

```python
import time
import json
from datetime import datetime

def monitorar_precos():
    # URLs de APIs de criptomoedas
    apis = {
        'bitcoin': 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd',
        'ethereum': 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
    }
    
    precos = {}
    
    for moeda, url in apis.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                dados = response.json()
                preco = dados[moeda]['usd']
                precos[moeda] = preco
            else:
                precos[moeda] = None
                
        except requests.exceptions.RequestException:
            precos[moeda] = None
    
    return precos

def salvar_historico_precos():
    precos = monitorar_precos()
    timestamp = datetime.now().isoformat()
    
    registro = {
        'timestamp': timestamp,
        'precos': precos
    }
    
    # Carregar histórico existente
    try:
        with open('historico_precos.json', 'r') as f:
            historico = json.load(f)
    except FileNotFoundError:
        historico = []
    
    # Adicionar novo registro
    historico.append(registro)
    
    # Salvar histórico atualizado
    with open('historico_precos.json', 'w') as f:
        json.dump(historico, f, indent=2)
    
    print(f"📊 Preços salvos às {timestamp}")
    return registro

# Testando
salvar_historico_precos()
```

**Conceitos-chave:** Monitoramento contínuo, histórico de dados, timestamp""",
        12: """**Solução:** Extrair dados de perfis de usuários

```python
def extrair_perfil_completo(username):
    # Buscar dados do usuário
    url_usuario = f'https://api.github.com/users/{username}'
    url_repos = f'https://api.github.com/users/{username}/repos'
    
    perfil = {}
    
    try:
        # Dados básicos do usuário
        response = requests.get(url_usuario)
        if response.status_code == 200:
            dados_usuario = response.json()
            
            perfil['basico'] = {
                'nome': dados_usuario['name'],
                'login': dados_usuario['login'],
                'bio': dados_usuario['bio'],
                'seguidores': dados_usuario['followers'],
                'seguindo': dados_usuario['following'],
                'repositorios_publicos': dados_usuario['public_repos']
            }
        
        # Repositórios do usuário
        response_repos = requests.get(url_repos)
        if response_repos.status_code == 200:
            repos = response_repos.json()
            
            repos_info = []
            for repo in repos[:5]:  # Top 5 repositórios
                repos_info.append({
                    'nome': repo['name'],
                    'descricao': repo['description'],
                    'stars': repo['stargazers_count'],
                    'linguagem': repo['language']
                })
            
            perfil['repositorios'] = repos_info
        
        return perfil
        
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")
        return None

# Testando
perfil = extrair_perfil_completo('octocat')
if perfil:
    print(f"👤 {perfil['basico']['nome']}")
    print(f"📊 {perfil['basico']['seguidores']} seguidores")
    print("\\n📁 Top repositórios:")
    for repo in perfil['repositorios']:
        print(f"  - {repo['nome']} ({repo['stars']} ⭐)")
```

**Conceitos-chave:** Múltiplas APIs, estruturação de dados complexos""",
        13: """**Solução:** Scraper de dados de imóveis

```python
def buscar_imoveis_api():
    # Exemplo usando API fictícia (substitua por API real)
    url = 'https://jsonplaceholder.typicode.com/posts'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            posts = response.json()
            
            # Simular dados de imóveis usando os posts
            imoveis = []
            for post in posts[:10]:  # Primeiros 10
                imovel = {
                    'id': post['id'],
                    'titulo': post['title'],
                    'descricao': post['body'][:100] + '...',
                    'preco': f"R$ {post['id'] * 10000:,}",
                    'area': f"{post['id'] * 50} m²",
                    'quartos': post['id'] % 4 + 1,
                    'banheiros': post['id'] % 3 + 1
                }
                imoveis.append(imovel)
            
            return imoveis
            
        else:
            print(f"Erro: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")
        return None

def salvar_imoveis_csv(imoveis):
    import csv
    
    with open('imoveis.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=imoveis[0].keys())
        writer.writeheader()
        writer.writerows(imoveis)
    
    print(f"✅ {len(imoveis)} imóveis salvos em imoveis.csv")

# Testando
imoveis = buscar_imoveis_api()
if imoveis:
    salvar_imoveis_csv(imoveis)
```

**Conceitos-chave:** Simulação de dados, salvamento em CSV, estruturação de dados""",
        14: """**Solução:** API de dados de filmes/séries

```python
def buscar_filmes_api():
    # Exemplo usando API pública de filmes
    url = 'https://jsonplaceholder.typicode.com/posts'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            posts = response.json()
            
            # Simular dados de filmes
            filmes = []
            generos = ['Ação', 'Comédia', 'Drama', 'Ficção Científica', 'Terror']
            
            for post in posts[:15]:
                filme = {
                    'id': post['id'],
                    'titulo': post['title'],
                    'sinopse': post['body'][:150] + '...',
                    'genero': generos[post['id'] % len(generos)],
                    'ano': 2000 + (post['id'] % 24),
                    'avaliacao': round(5 + (post['id'] % 5), 1),
                    'duracao': f"{90 + (post['id'] % 60)} min"
                }
                filmes.append(filme)
            
            return filmes
            
        else:
            print(f"Erro: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")
        return None

def filtrar_filmes_por_genero(filmes, genero):
    return [f for f in filmes if f['genero'] == genero]

# Testando
filmes = buscar_filmes_api()
if filmes:
    print(f"🎬 Total de filmes: {len(filmes)}")
    
    filmes_acao = filtrar_filmes_por_genero(filmes, 'Ação')
    print(f"\\n🎯 Filmes de ação: {len(filmes_acao)}")
    
    for filme in filmes_acao[:3]:
        print(f"  - {filme['titulo']} ({filme['ano']}) - ⭐ {filme['avaliacao']}")
```

**Conceitos-chave:** Simulação de dados, filtragem, estruturação de dados""",
        15: """**Solução:** Sistema de vagas de emprego

```python
def buscar_vagas_api():
    # Simular API de vagas usando JSONPlaceholder
    url = 'https://jsonplaceholder.typicode.com/posts'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            posts = response.json()
            
            # Simular dados de vagas
            vagas = []
            empresas = ['TechCorp', 'Inovação Ltda', 'Digital Solutions', 'StartupXYZ', 'MegaTech']
            cargos = ['Desenvolvedor Python', 'Analista de Dados', 'Engenheiro de Software', 'Cientista de Dados', 'DevOps']
            
            for post in posts[:20]:
                vaga = {
                    'id': post['id'],
                    'titulo': cargos[post['id'] % len(cargos)],
                    'empresa': empresas[post['id'] % len(empresas)],
                    'descricao': post['body'][:200] + '...',
                    'salario': f"R$ {5000 + (post['id'] * 500):,}",
                    'localizacao': 'São Paulo, SP',
                    'tipo': 'CLT' if post['id'] % 2 == 0 else 'PJ',
                    'nivel': 'Júnior' if post['id'] % 3 == 0 else 'Pleno' if post['id'] % 3 == 1 else 'Sênior'
                }
                vagas.append(vaga)
            
            return vagas
            
        else:
            print(f"Erro: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Erro: {e}")
        return None

def filtrar_vagas_por_cargo(vagas, cargo):
    return [v for v in vagas if cargo.lower() in v['titulo'].lower()]

# Testando
vagas = buscar_vagas_api()
if vagas:
    print(f"💼 Total de vagas: {len(vagas)}")
    
    vagas_python = filtrar_vagas_por_cargo(vagas, 'python')
    print(f"\\n🐍 Vagas Python: {len(vagas_python)}")
    
    for vaga in vagas_python[:3]:
        print(f"  - {vaga['titulo']} na {vaga['empresa']}")
        print(f"    💰 {vaga['salario']} - {vaga['nivel']}")
```

**Conceitos-chave:** Simulação de dados, filtragem por texto, estruturação de dados""",
        16: """**Abordagem conceitual:**

1. **Análise do problema:** Criar sistema que navega por múltiplas páginas de API
2. **Estrutura de dados:** Usar paginação para buscar todos os dados
3. **Arquitetura modular:** Separar lógica de paginação, busca e processamento
4. **Otimização:** Implementar cache e controle de rate limiting

**Estrutura do código:**
```python
# scraper_paginacao.py
import requests
import time

class ScraperPaginacao:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.dados_coletados = []
    
    def buscar_pagina(self, pagina):
        # TODO: Implementar busca de página específica
        pass
    
    def buscar_todas_paginas(self, max_paginas=10):
        # TODO: Implementar loop de paginação
        pass
    
    def processar_dados(self, dados):
        # TODO: Implementar processamento
        pass
```

**Dicas de implementação:**
- Use parâmetros de paginação (page, offset, limit)
- Implemente delay entre requisições
- Adicione tratamento de erros de paginação""",
        17: """**Abordagem conceitual:**

1. **Análise do problema:** Extrair dados de gráficos e visualizações
2. **Estrutura de dados:** Identificar APIs que fornecem dados brutos
3. **Arquitetura modular:** Separar extração, processamento e visualização
4. **Processamento:** Converter dados para formatos utilizáveis

**Estrutura do código:**
```python
# extrator_graficos.py
import requests
import json

class ExtratorGraficos:
    def __init__(self, api_url):
        self.api_url = api_url
        self.dados_extraidos = []
    
    def extrair_dados_grafico(self, grafico_id):
        # TODO: Implementar extração
        pass
    
    def processar_dados_grafico(self, dados):
        # TODO: Implementar processamento
        pass
    
    def salvar_dados_processados(self, dados):
        # TODO: Implementar salvamento
        pass
```

**Dicas de implementação:**
- Identifique APIs que fornecem dados brutos
- Use bibliotecas como matplotlib para visualização
- Implemente cache para dados processados""",
        18: """**Abordagem conceitual:**

1. **Análise do problema:** Monitorar mudanças em páginas web ao longo do tempo
2. **Estrutura de dados:** Sistema de versionamento de conteúdo
3. **Arquitetura modular:** Separar monitoramento, comparação e alertas
4. **Persistência:** Banco de dados para histórico de mudanças

**Estrutura do código:**
```python
# monitor_mudancas.py
import requests
import hashlib
import sqlite3
from datetime import datetime

class MonitorMudancas:
    def __init__(self, url):
        self.url = url
        self.db = sqlite3.connect('mudancas.db')
        self.setup_database()
    
    def verificar_mudancas(self):
        # TODO: Implementar verificação
        pass
    
    def comparar_conteudo(self, conteudo_atual, conteudo_anterior):
        # TODO: Implementar comparação
        pass
    
    def enviar_alerta(self, mudancas):
        # TODO: Implementar alertas
        pass
```

**Dicas de implementação:**
- Use hash para detectar mudanças
- Implemente sistema de alertas (email, webhook)
- Adicione agendamento de verificações""",
        19: """**Abordagem conceitual:**

1. **Análise do problema:** Extrair dados estruturados de páginas HTML usando regex
2. **Estrutura de dados:** Padrões regex para diferentes tipos de dados
3. **Arquitetura modular:** Separar extração, validação e processamento
4. **Flexibilidade:** Sistema de padrões configuráveis

**Estrutura do código:**
```python
# extrator_regex.py
import requests
import re

class ExtratorRegex:
    def __init__(self):
        self.padroes = {
            'email': r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b',
            'telefone': r'\\(?\\d{2}\\)?\\s?\\d{4,5}-?\\d{4}',
            'cpf': r'\\d{3}\\.?\\d{3}\\.?\\d{3}-?\\d{2}'
        }
    
    def extrair_dados(self, html, tipo_dado):
        # TODO: Implementar extração
        pass
    
    def validar_dados(self, dados):
        # TODO: Implementar validação
        pass
```

**Dicas de implementação:**
- Use regex compiladas para performance
- Implemente validação de dados extraídos
- Adicione tratamento de casos especiais""",
        20: """**Abordagem conceitual:**

1. **Análise do problema:** Criar sistema de busca avançada em textos
2. **Estrutura de dados:** Índices de texto para busca eficiente
3. **Arquitetura modular:** Separar indexação, busca e ranking
4. **Algoritmos:** Implementar diferentes algoritmos de busca

**Estrutura do código:**
```python
# sistema_busca.py
import re
from collections import defaultdict

class SistemaBusca:
    def __init__(self):
        self.indice = defaultdict(list)
        self.documentos = {}
    
    def indexar_documento(self, doc_id, texto):
        # TODO: Implementar indexação
        pass
    
    def buscar(self, consulta):
        # TODO: Implementar busca
        pass
    
    def rankear_resultados(self, resultados):
        # TODO: Implementar ranking
        pass
```

**Dicas de implementação:**
- Use TF-IDF para ranking
- Implemente busca por proximidade
- Adicione suporte a operadores booleanos""",
        21: """**Abordagem conceitual:**

1. **Análise do problema:** Sistema completo de análise de sentimentos usando APIs
2. **Estrutura de dados:** Pipeline de processamento de texto
3. **Arquitetura modular:** Separar coleta, análise e visualização
4. **Integração:** Múltiplas APIs para diferentes aspectos da análise

**Estrutura do código:**
```python
# sistema_sentimentos.py
import requests
import json
from datetime import datetime

class SistemaSentimentos:
    def __init__(self):
        self.apis_sentimento = []
        self.dados_coletados = []
    
    def coletar_dados_sociais(self):
        # TODO: Implementar coleta
        pass
    
    def analisar_sentimento(self, texto):
        # TODO: Implementar análise
        pass
    
    def gerar_relatorio(self):
        # TODO: Implementar relatório
        pass
```

**Dicas de implementação:**
- Use APIs de análise de sentimento
- Implemente agregação de resultados
- Adicione visualização de tendências""",
        22: """**Abordagem conceitual:**

1. **Análise do problema:** Bot de Telegram que responde com informações de APIs
2. **Estrutura de dados:** Sistema de comandos e respostas
3. **Arquitetura modular:** Separar bot, APIs e processamento
4. **Integração:** Webhook do Telegram com APIs externas

**Estrutura do código:**
```python
# bot_telegram.py
import requests
import json

class BotTelegram:
    def __init__(self, token):
        self.token = token
        self.base_url = f'https://api.telegram.org/bot{token}'
    
    def processar_comando(self, comando, chat_id):
        # TODO: Implementar processamento
        pass
    
    def enviar_resposta(self, chat_id, texto):
        # TODO: Implementar envio
        pass
    
    def webhook_handler(self, update):
        # TODO: Implementar webhook
        pass
```

**Dicas de implementação:**
- Use webhook do Telegram
- Implemente sistema de comandos
- Adicione tratamento de erros""",
        23: """**Abordagem conceitual:**

1. **Análise do problema:** Sistema de recomendação baseado em APIs de dados
2. **Estrutura de dados:** Algoritmos de recomendação e perfis de usuário
3. **Arquitetura modular:** Separar coleta, processamento e recomendação
4. **Algoritmos:** Implementar filtragem colaborativa e baseada em conteúdo

**Estrutura do código:**
```python
# sistema_recomendacao.py
import requests
import json
from collections import defaultdict

class SistemaRecomendacao:
    def __init__(self):
        self.perfis_usuarios = {}
        self.dados_filmes = {}
        self.matriz_preferencias = defaultdict(dict)
    
    def coletar_dados_apis(self):
        # TODO: Implementar coleta
        pass
    
    def calcular_similaridade(self, usuario1, usuario2):
        # TODO: Implementar cálculo
        pass
    
    def gerar_recomendacoes(self, usuario):
        # TODO: Implementar recomendação
        pass
```

**Dicas de implementação:**
- Use algoritmos de similaridade
- Implemente cache de recomendações
- Adicione feedback do usuário""",
        24: """**Abordagem conceitual:**

1. **Análise do problema:** Dashboard web que exibe dados de múltiplas APIs
2. **Estrutura de dados:** Sistema de cache e atualização de dados
3. **Arquitetura modular:** Separar backend, frontend e APIs
4. **Tempo real:** WebSockets para atualizações em tempo real

**Estrutura do código:**
```python
# dashboard_apis.py
from flask import Flask, render_template
import requests
import threading
import time

class DashboardAPIs:
    def __init__(self):
        self.app = Flask(__name__)
        self.dados_cache = {}
        self.apis_config = {}
    
    def coletar_dados_apis(self):
        # TODO: Implementar coleta
        pass
    
    def atualizar_cache(self):
        # TODO: Implementar atualização
        pass
    
    def criar_dashboard(self):
        # TODO: Implementar dashboard
        pass
```

**Dicas de implementação:**
- Use Flask ou FastAPI para backend
- Implemente sistema de cache
- Adicione WebSockets para tempo real""",
        25: """**Abordagem conceitual:**

1. **Análise do problema:** Sistema de automação que integra várias APIs
2. **Estrutura de dados:** Workflow de automação com dependências
3. **Arquitetura modular:** Separar automação, APIs e monitoramento
4. **Orquestração:** Sistema de filas e agendamento

**Estrutura do código:**
```python
# sistema_automacao.py
import requests
import json
import schedule
import time
from datetime import datetime

class SistemaAutomacao:
    def __init__(self):
        self.workflows = {}
        self.apis_config = {}
        self.logs = []
    
    def definir_workflow(self, nome, passos):
        # TODO: Implementar definição
        pass
    
    def executar_workflow(self, nome):
        # TODO: Implementar execução
        pass
    
    def monitorar_execucao(self):
        # TODO: Implementar monitoramento
        pass
```

**Dicas de implementação:**
- Use Celery para filas de tarefas
- Implemente sistema de logs
- Adicione alertas de falha""",
    }

    # Process cells and add solutions
    new_cells = []
    exercise_counter = 0

    # Load notebook
    with open(notebook_path, "r", encoding="utf-8") as f:
        data = json.load(f)

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


# Run for Chapter 12
add_solutions_chapter_12()
