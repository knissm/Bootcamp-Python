"""
try:
    numero01 = int(input("Inserir um número inteiro: "))
    numero02 = int(input("Inserir outro número inteiro: "))
    resultado = numero01 // numero02
    print(resultado)
except ZeroDivisionError:
    print('integer division or modulo by zero')
except:
    print('KeyboardInterrupt')
"""

try:
    resultado = len(2)
    print(resultado)
except TypeError as e:
    print(e)
else:
    print("Tudo deu certo!")
finally:
    print("Independente do que acontecer, eu sou executado")
