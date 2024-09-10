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
#Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
# garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
"""
try:
    celsius = float(input("Celsius °: "))
    F = (celsius * 1.8) + 32
    print(f"{celsius:.1f}°C para Fahrenheit: {F:.1f} °F")
except KeyboardInterrupt:
    print("Interrompido pelo usuário")
except ValueError:
    print("Você não digitou um número. Digite um número!")
"""
#Exercício 22: Verificador de Palíndromo
#Crie um programa que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. 
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.
"""
try:
    palavra = input("Digite uma palavra: ").strip().lower().replace(" ", "")
    if isinstance(palavra, str):
        if palavra == palavra[::-1]:
            print(f"A palavra {palavra} É palíndromo! {palavra[::-1]}")
        else:
            print(f"A palavra {palavra} não é Palíndromo!")
    else:
        print("Digite uma entrada válida")
except ValueError:
    print("Você não digitou uma entrada válida")
except KeyboardInterrupt:
    print("Abortado pelo usuário")
"""


#Exercício 23: Calculadora Simples
#Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. 
# Imprima o resultado ou uma mensagem de erro apropriada.
"""
print("~" * 25)
print("Somar [+]")
print("Subtrair [-]")
print("Multiplicar [*]")
print("Dividir [/]")
print("~" * 25)

try:
    escolha = input("Escolha: ").strip()

    if escolha == "+":
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        resultado = num1 + num2 
        print(f"Soma de {num1} + {num2} é: {resultado} ")

    if escolha == "-":
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        resultado = num1 - num2 
        print(f"Subtração de {num1} - {num2} é: {resultado} ")

    if escolha == "*":
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        resultado = num1 * num2 
        print(f"Multiplicação de {num1} * {num2} é: {resultado} ")

    if escolha == "/":
        try:
            num1 = int(input("Número 1: "))
            num2 = int(input("Número 2: "))
            resultado = num1 / num2 
            print(f"Divisão de {num1} / {num2} é: {resultado} ")
        except ZeroDivisionError:
            print("Você não pode dividir algo por 0. Tente novamente!")

    else:
        print("Você não selecionou nem uma das escolhas!")
    print("FIM")
except KeyboardInterrupt:
    print("Operação interrompida pelo usuario")
"""

#Exercício 24: Classificador de Números
#Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como 
# "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".
"""
try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero <0:
        print("Negativo ")
    else:
        print("Zero")

    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

except ValueError:
    print("Por favor, digite um número inteiro válido!")

except KeyboardInterrupt:
    print("Interrompido pelo usuário")
"""

#Exercício 25: Conversão de Tipo com Validação
#Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
#Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
"""
numeros = input("Digite uma lista de numeros separados por ',': ").split(",")
numeros_int = []
try:
    for numero in numeros:
        numeros_int.append(int(numero.strip()))
    print(numeros_int)
except ValueError:
    print("Alguma entrada foi inválida. Verifique!")

except KeyboardInterrupt:
    print("Usuário cancelou!")
"""


"""
Desafio - Refatorar o projeto da aula anterior evitando Bugs!
Para resolver os bugs identificados — tratamento de entradas inválidas que não podem ser convertidas para um 
número de ponto flutuante e prevenção de valores negativos para salário e bônus, você pode modificar o código diretamente. 
Isso envolve adicionar verificações adicionais após a tentativa de conversão para garantir que os valores sejam positivos.
"""
# Solicita ao usuário que digite seu nome
try:
    nome = input("Digite seu nome: ")

    # Verifica se o nome está vazio
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
    # Verifica se há números no nome
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
    else:
        print("Nome válido:", nome)
except ValueError as e:
    print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float

try:
    salario = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
try:
    bonus_recebido = float(input("Digite o valor do bônus recebido: "))
    if bonus_recebido < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")

# Assumindo uma lógica de cálculo para o bônus final e KPI
bonus_final = bonus_recebido * 1.2  # Exemplo, ajuste conforme necessário
kpi = (salario + bonus_final) / 1000  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"Seu KPI é: {kpi:.2f}")
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")