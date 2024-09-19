
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
"""
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))
print(emails_unicos )
"""

#7. Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
"""
idades = [22, 15, 30, 17, 18]

maiores_ou_iguais_a_18 = [x for x in idades if x >= 18]
print(maiores_ou_iguais_a_18)
"""

#8. Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
"""
pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]

pessoas.sort(key = lambda pessoas:pessoas['nome'])
print(pessoas)
"""

#9. Dado um conjunto de números, calcular a média.
"""
numeros = [10, 20, 30, 40, 50]

media_de_numeros = (sum(numeros) / len(numeros))
print(media_de_numeros)
"""

#10. Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

valores:list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares:list = []
impares:list = []

""" Primeira forma 
for numero in valores:
    if numero % 2 ==0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Pares: {pares}")
print((f"Ímpares: {impares}"))
"""

""" Segunda forma 
pares = [valor for valor in valores if valor % 2 == 0 ]
impares = [valor for valor in valores if valor % 2 != 0]

print(pares)
print(impares)
"""

# 11. Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
"""
produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 0},
    {"id": 3, "nome": "Monitor", "preço": 300}
]
for x in produtos:
    if x['preço'] == 0:
        x['preço'] = 66.79

for x in produtos:
    print(f"ID: {x['id']}")
    print(f"Nome: {x['nome']}")
    print(f"Preço: {x['preço']}")
    print('~~'*6)
"""

# 12. Dados dois dicionários, fundi-los em um único dicionário.
"""
dicionario1 = {"A":1,"B":2,"C":3}
dicionario2 = {"D":4,"E":-1,"F":15}

dicionario_fundido = {**dicionario1, **dicionario2}

print(dicionario_fundido)
"""

# 13. Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
""" Uma forma 
for produto, valor in estoque.items():
    if valor > 0:
        print(f"Produto: {produto} - Valor R$ {valor}")
"""
""" Segunda forma
estoque_positivo = {produto:quantidade for produto, quantidade in estoque.items() if quantidade > 0}
print(estoque_positivo)
"""

# 14. Dado um dicionário, criar listas separadas para suas chaves e valores.
"""
dicionario = {"a": 1, "b": 2, "c": 3}

chaves = list(dicionario.keys())
valores = list(dicionario.values())

print(chaves, valores)
"""

# 15.  Dada uma string, contar a frequência de cada caractere usando um dicionário.
"""
frase = "The quick brown fox jumps over the lazy fox".split()

frequencia = {}

for palavra in frase:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print(frequencia)
"""

# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas