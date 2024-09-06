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
"""
print(True or False)
print(True or True)
print(False or False)
"""
#18.Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
"""
inverte = str(input("Valor: ")).title()
print(not inverte)
"""

#19.Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
"""
num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))
print(num1 == num2)
"""
#20.Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
"""
num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))
print(num1 != num2)
"""

#Exercício 21: Conversor de Temperatura
#Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

#Exercício 22: Verificador de Palíndromo
#Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

#Exercício 23: Calculadora Simples
#Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

#Exercício 24: Classificador de Números
#Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

#Exercício 25: Conversão de Tipo com Validação
#Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
#Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.