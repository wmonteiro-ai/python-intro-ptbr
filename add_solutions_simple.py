import json
import re


def add_solution_to_notebook(notebook_path, exercise_num, solution_text):
    """Add a single solution to a notebook"""

    # Load notebook
    with open(notebook_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Find the exercise cell and add solution after it
    new_cells = []
    exercise_found = False

    for i, cell in enumerate(data["cells"]):
        new_cells.append(cell)

        if cell["cell_type"] == "markdown" and not exercise_found:
            source_text = "".join(cell["source"])

            # Look for exercise pattern
            if re.search(rf"\*\*{exercise_num}\.\*\*", source_text):
                exercise_found = True

                # Create solution cell
                solution_cell = {
                    "cell_type": "markdown",
                    "id": f"solution-{exercise_num}",
                    "metadata": {},
                    "source": [
                        f'::: {{.callout-note title="Gabarito" collapse="true"}}\n\n{solution_text}\n\n:::'
                    ],
                }

                new_cells.append(solution_cell)
                print(f"Added solution for exercise {exercise_num}")

    # Update notebook
    data["cells"] = new_cells

    # Save notebook
    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)


# Add solutions for Chapter 11
notebook_path = "11-Modulos-Bibliotecas.ipynb"

# Solution 1
solution_1 = """**Solução:** Módulo básico com funções simples

```python
# cumprimentos.py
def dizer_oi():
    return "Olá!"

def dizer_tchau():
    return "Tchau!"

if __name__ == "__main__":
    print(dizer_oi())
```

**Conceitos-chave:** Definição de funções, `if __name__ == "__main__"`"""

add_solution_to_notebook(notebook_path, 1, solution_1)

# Solution 2
solution_2 = """**Solução:** Importação e uso de módulo

```python
# teste_cumprimentos.py
import cumprimentos

mensagem = cumprimentos.dizer_oi()
print(mensagem)
```

**Conceitos-chave:** Importação de módulos, uso de funções externas"""

add_solution_to_notebook(notebook_path, 2, solution_2)

# Solution 3
solution_3 = """**Solução:** Uso da biblioteca random

```python
import random

numero_sorteado = random.randint(1, 100)
print(f"Número sorteado: {numero_sorteado}")
```

**Conceitos-chave:** Biblioteca random, função randint"""

add_solution_to_notebook(notebook_path, 3, solution_3)

print("Added first 3 solutions to Chapter 11")
