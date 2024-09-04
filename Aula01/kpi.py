"""
Questão: Cálculo de Bônus com Entrada do Usuário.
Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
o valor do seu salário mensal e o valor do bônus que recebeu. 
O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e 
informando o valor do salário em comparação com o bônus recebido.
"""
"""
Instruções:
O programa deve começar solicitando ao usuário que insira seu nome.
Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
"""
from time import sleep

nome = input("Digite seu nome: ").title()
salario = float(input("Salario Mensal R$: "))
bonus = float(input("Qual a '%' do Bônus R$: "))

calculo_kpi = 1000 + salario * 1.5

print(f"Bem vindo {nome}!")
print(f'Seu salário é de {salario:.0f}, levando em conta que o seu bônus foi de {bonus}%, seu salario final foi de ...')
sleep(2)
print("CALCULANDO")
sleep(2)
print(f"R${calculo_kpi:.2f}")
print("Até mais!")


