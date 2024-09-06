"""INTEIROS (int) """

#1.Escreva um programa que soma dois números inteiros inseridos pelo usuário.
"""
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Ditite o segundo número:"))
soma = num1 + num2
print(f"Soma: {soma}")
"""

#2.Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
"""
numero = int(input("Digite um numero: "))
print(f"Resto da divisão por 5: {numero % 5}")
"""

#3.Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
"""
num1 = int(input("Digite o número 1: "))
num2 = int(input("Digite o nymero 2: "))
print(f"Resultado: {num1 * num2}")
"""
#4.Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
"""
num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))
print(f"Resultado: {num1 // num2}")
"""
#5.Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
"""
num = int(input("Número: "))
print(f"Quadrado de {num} é {num * 2}")
"""

""" Números de Ponto Flutuante (float) """

#6.Escreva um programa que receba dois números flutuantes e realize sua adição.
"""
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
print(f"Resultado: {num1 + num2}")
"""

#7.Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
"""
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
print(f"Resultado: {(num1 + num2) / 2}")
"""

#8.Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
"""
base = float(input("Base: "))
expoente = float(input("Expoente: "))
potencia = base ** expoente
print(f"Resultado: {potencia:.0f}")
"""
#9.Faça um programa que converta a temperatura de Celsius para Fahrenheit.
"""
celsius = float(input("Celsius °: "))
F = (celsius * 1.8) + 32
print(f"{celsius:.1f}°C para Fahrenheit: {F:.1f} °F")
"""

#10.Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
"""
raio = float(input("Raio: "))
A = 3.14159*raio**2
print(f"Área: {A:.1f}")
"""

""" Strings (str) """

#11.Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
"""
string = str(input("Frase: "))
print(f"{string.upper()}")
"""

#12.Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
"""
nome = str(input("Nome completo: "))
print(f"{nome.lower()}")
"""

#13.Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
"""
frase = str(input("Frase: "))
print(frase)
print(f"{frase.strip()}")
"""

#14.Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
"""
data = str(input("Data: "))
data_nova = data.split("/")
print(f"Dia: {data_nova[0]}")
print(f"Mês: {data_nova[1]}")
print(f"Ano: {data_nova[2]}")
"""

#15.Escreva um programa que concatene duas strings fornecidas pelo usuário.
"""
stringa = str(input("String A: "))
stringb = str(input("String B: "))
print(f"{stringa + stringb}")
"""

""" Booleanos (bool) """

#16.Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
"""
print(True and False)
print(True and True)
print(False and False)
"""

#17.Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
print(True or False)
print(True or True)
print(False or False)
#18.Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
#19.Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
#20.Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.