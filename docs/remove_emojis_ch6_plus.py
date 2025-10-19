import json
import re

# Remove emojis from headers in chapters 6 and beyond
chapters_to_fix = [
    '06-Funcoes.ipynb',
    '07-Listas-Dicionarios-Tuplas.ipynb',
    '08-Manipulacao-Arquivos.ipynb',
    '09-POO.ipynb',
    '10-Erros-Comuns.ipynb',
    '11-Modulos-Bibliotecas.ipynb',
    '12-APIs-Parte1-Consumo.ipynb',
    '13-APIs-Parte2-Criacao.ipynb',
    '14-Web-Scraping.ipynb',
    '15-Banco-Dados-SQL.ipynb',
    '16-Expressoes-Regulares.ipynb'
]

# Emoji pattern - comprehensive list of common emojis
emoji_pattern = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U00002702-\U000027B0"   # dingbats
    "\U000024C2-\U0001F251"   # enclosed characters
    "\U0001F900-\U0001F9FF"   # supplemental symbols
    "\U0001FA70-\U0001FAFF"   # symbols and pictographs extended-A
    "\U00002600-\U000026FF"   # miscellaneous symbols
    "\U00002700-\U000027BF"   # dingbats
    "]+", flags=re.UNICODE)

total_changes = 0

for notebook_path in chapters_to_fix:
    print(f"Processing {notebook_path}...")
    
    # Load notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    changes_in_file = 0
    
    # Process each cell
    for cell in data['cells']:
        if cell['cell_type'] == 'markdown':
            source = cell['source']
            new_source = []
            
            for line in source:
                # Check if this line is a header (starts with #)
                if re.match(r'^#+\s*', line.strip()):
                    # Remove emojis from the line
                    cleaned_line = emoji_pattern.sub('', line)
                    # Clean up extra spaces
                    cleaned_line = re.sub(r'\s+', ' ', cleaned_line).strip()
                    # Ensure it still starts with the right number of #
                    if not cleaned_line.startswith('#'):
                        # Find the original number of # symbols
                        original_hashes = re.match(r'^(#+)', line.strip())
                        if original_hashes:
                            cleaned_line = original_hashes.group(1) + ' ' + cleaned_line
                    
                    if cleaned_line != line:
                        changes_in_file += 1
                        print(f"  Fixed: {line.strip()} -> {cleaned_line}")
                    
                    new_source.append(cleaned_line + '\n')
                else:
                    new_source.append(line)
            
            cell['source'] = new_source
    
    # Save notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    
    print(f"  Total changes in {notebook_path}: {changes_in_file}")
    total_changes += changes_in_file

print(f"\nTotal changes across all chapters: {total_changes}")
print("Done!")

