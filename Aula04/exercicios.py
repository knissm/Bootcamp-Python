# Crie um dicionario para armazenar informações de um livro,
# incluindo titulo, autor e ano de publicação. Imprima cada informação.
from typing import Dict, Any

livro = {}

livro['Titulo'] = str(input("Título: "))
livro['Autor'] = str(input("Autor: "))
livro['Ano Publicacao'] = int(input("Ano de Publicação: "))

for i, j in livro.items():
    print(i, j)