import json
import re

# Fix content labels in notebooks
notebooks_to_fix = [
    "01-Introducao-Ambiente.ipynb",
    "02-Introducao-Algoritmos.ipynb",
    "03-Variaveis-IO.ipynb",
]

for notebook_path in notebooks_to_fix:
    print(f"Processing {notebook_path}...")

    # Load notebook
    with open(notebook_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Find and fix the content labels
    for cell in data["cells"]:
        if cell["cell_type"] == "markdown":
            source = cell["source"]
            new_source = []

            for i, line in enumerate(source):
                # Check if this line is a content label
                if re.match(r"^\(content:[^)]+\)=\s*$", line.strip()):
                    # Convert to proper Quarto label format
                    label_match = re.match(r"^\(content:([^)]+)\)=\s*$", line.strip())
                    if label_match:
                        label_name = label_match.group(1)
                        # Convert to proper Quarto label format
                        new_line = f"{{#{label_name}}}\n"
                        new_source.append(new_line)
                        print(f"  Fixed label: {line.strip()} -> {new_line.strip()}")
                    else:
                        new_source.append(line)
                else:
                    new_source.append(line)

            cell["source"] = new_source

    # Save notebook
    with open(notebook_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)

print("\nDone!")
