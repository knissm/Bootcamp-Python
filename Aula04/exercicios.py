
#1.Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
"""
numeros = list(range(1,11))
for numero in numeros:
    print(numero**2)
""" 

#2.Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
"""
lista = ["Python", "Java", "C++", "JavaScript"]
lista.remove("C++")
lista.append("Ruby")
print(lista)
"""

#3.Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
"""
from typing import Dict, Any

livro = {}

livro['Titulo'] = str(input("Título: "))
livro['Autor'] = str(input("Autor: "))
livro['Ano Publicacao'] = int(input("Ano de Publicação: "))

for i, j in livro.items():
    print(i, j)
"""

#4.Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
"""
texto = str(input("Digite o texto: ")).split()
ocorrencia = {}

for palavra in texto:
    if palavra in ocorrencia:
        ocorrencia[palavra] += 1
    else:
        ocorrencia[palavra] = 1
print(ocorrencia)
"""

#5.Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
"""
lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

total = sum(precos.values())

print(total)
"""

#6: Objetivo: Dada uma lista de emails, remover todos os duplicados.
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))
print(emails_unicos )