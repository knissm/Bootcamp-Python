# Bootcamp Aula 02 - TypeError, Type Check, Type Conversion, try-execept e if

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=FINALIZADO&color=GREEN&style=for-the-badge)

# 1. Tipos primitivos
Variáveis são espaços de memória designados para armazenar dados que podem ser modificados durante a execução de um programa. Em Python, a declaração de variáveis é dinâmica, o que significa que o tipo de dado é inferido durante a atribuição.

Exemplo em Python:

Python suporta vários tipos de dados simples, tais como:

Inteiros (int): Representam números inteiros.
Ponto Flutuante (float): Representam números reais.
Strings (str): Representam sequências de caracteres.
Booleanos (bool): Representam valores verdadeiros (True) ou falsos (False).

## 1. Inteiros (int)
Métodos e operações:
+ (adição)
- (subtração)
* (multiplicação)
// (divisão inteira)
% (módulo - resto da divisão)

## 2. Números de Ponto Flutuante (float)
Métodos e operações:
+ (adição)
- (subtração)
* (multiplicação)
/ (divisão)
** (potenciação)

## 3. Strings (str)
Métodos e operações:
.upper() (converte para maiúsculas)
.lower() (converte para minúsculas)
.strip() (remove espaços em branco no início e no final)
.split(sep) (divide a string em uma lista, utilizando sep como delimitador)
+ (concatenação de strings)

## 4. Booleanos (bool)
Operações lógicas:
and (E lógico)
or (OU lógico)
not (NÃO lógico)
== (igualdade)
!= (diferença)

# TypeError, Type Check e Type Conversion em Python
Python é uma linguagem de programação dinâmica, mas fortemente tipada, o que significa que não é necessário declarar tipos de variáveis explicitamente, mas o tipo de uma variável é determinado pelo valor que ela armazena. Isso introduz a necessidade de compreender como Python lida com diferentes tipos de dados, especialmente quando se trata de operações que envolvem múltiplos tipos. Vamos explorar três conceitos importantes: TypeError, verificação de tipo (type check), e conversão de tipo (type conversion).

## TypeError
Um TypeError ocorre em Python quando uma operação ou função é aplicada a um objeto de tipo inadequado. Python não sabe como aplicar a operação porque os tipos de dados não são compatíveis.

## Exemplo de TypeError
Um exemplo clássico é tentar utilizar a função len() com um inteiro, o que resulta em TypeError, pois len() espera um objeto iterável, como uma string, lista, ou tupla, não um inteiro.

```
# Exemplo que causa TypeError
try:
    resultado = len(5)
except TypeError as e:
    print(e)  # Imprime a mensagem de erro
```
O código acima tenta obter o comprimento de um inteiro, o que não faz sentido, resultando na mensagem de erro: "object of type 'int' has no len()"

## Type Check
Verificação de tipo (type check) é o processo de verificar o tipo de uma variável. Isso pode ser útil para garantir que operações ou funções sejam aplicadas apenas a tipos de dados compatíveis, evitando erros em tempo de execução.

### Exemplo de Type Check
Para verificar o tipo de uma variável em Python, você pode usar a função type() ou isinstance().

```
numero = 10
if isinstance(numero, int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")

```
Este código verifica se numero é uma instância de int e imprime uma mensagem apropriada.

## Type Conversion
Conversão de tipo (type conversion), também conhecida como casting, é o processo de converter o valor de uma variável de um tipo para outro. Python oferece várias funções integradas para realizar conversões explícitas de tipo, como int(), float(), str(), etc.

### Exemplo de Type Conversion
Se você quiser somar um inteiro e um número flutuante, pode ser necessário converter o inteiro para flutuante ou vice-versa para garantir que a operação de soma seja realizada corretamente.

```
numero_inteiro = 5
numero_flutuante = 2.5
# Converte o inteiro para flutuante e realiza a soma
soma = float(numero_inteiro) + numero_flutuante
print(soma)  # Resultado: 7.5
```

## try-except
A estrutura try-except é usada para tratamento de exceções em Python. Uma exceção é um erro que ocorre durante a execução do programa e que, se não tratado, interrompe o fluxo normal do programa e termina sua execução. O tratamento de exceções permite que o programa lide com erros de maneira elegante, permitindo que continue a execução ou falhe de forma controlada.

### try: Este bloco é o primeiro na estrutura de tratamento de exceções. Python tenta executar o código dentro deste bloco.
except: Se uma exceção ocorrer no bloco try, a execução imediatamente salta para o bloco except. Você pode especificar tipos de exceção específicos para capturar e tratar apenas essas exceções. Se nenhum tipo de exceção for especificado, ele captura todas as exceções.

### Exemplo de try-except

```
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que executa se a exceção ZeroDivisionError for levantada
    print("Divisão por zero não é permitida.")
```

## if
O if é uma estrutura de controle de fluxo que permite ao programa executar diferentes ações com base em diferentes condições. Se a condição avaliada pelo if for verdadeira (True), o bloco de código indentado sob ele será executado. Se a condição for falsa (False), o bloco de código será ignorado.

### if: Avalia uma condição. Se a condição for verdadeira, executa o bloco de código associado.
### elif: Abreviação de "else if". Permite verificar múltiplas condições em sequência.
### else: Executa um bloco de código se todas as condições anteriores no if e elif forem falsas.

### Exemplo de if

```
idade = 20
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Exatamente 18 anos")
else:
    print("Maior de idade")
```

Ambas as estruturas, try-except e if, são fundamentais para a criação de programas em Python que são capazes de lidar com situações inesperadas (como erros de execução) e tomar decisões com base em condições, permitindo assim que você construa programas mais robustos, flexíveis e seguros.
