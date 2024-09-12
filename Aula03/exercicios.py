### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
"""
quantidade = int(input("Quantidade: "))
preco = int(input("Preço R$: "))

if quantidade <0 or preco <0:
    print("Dados inválidos!")
    print("Valores negativos não são aceitos, verifique!")

else:# quantidade >0 or preco >0:
    print('Dados Válidos!')
    print(f"Quantidade: {quantidade} - Preço R$ {preco}")
"""

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
"""
try:
    temp = float(input("Temperatura atual: "))
    if temp >= 0 and temp <18:
        print("Baixa!")
    elif temp >= 18 and temp <=26:
        print("Normal!")
    elif temp >26:
        print("Alta!")
    else:
        print("Erro na Analise!")
except ValueError:
    print("Entrada inválida!")
except KeyboardInterrupt:
    print("Interrompido pelo usuário!")
"""

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
"""
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == "ERROR":
    print(log['message'])
"""

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
"""
idade = int(input("Idade: "))
email = str(input("Email: "))

if idade <18 or idade >65:
    print("Idade fora do intervalo permitido!")

elif "@" not in email or "."  not in email:
    print("Email inválido")

else:
    print("Dados válidos!")
"""

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
"""
transacao = {'valor': 12000, 'hora': 20}

if transacao['valor'] > 10000 or transacao['hora'] <9 or transacao['hora'] >18:
    print("Transação suspeita")
else:
    print("Transação normal")
"""
### Exercícios com FOR

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
"""
try:
    txt = "a raposa marrom salta sobre o cachorro preguiçoso"

    palavra = str(input("Palavra: ")).lower().strip().split()
    contagem_palavras = {}

    for i in palavra:
        if i in contagem_palavras:
            contagem_palavras[i] += 1
        else:
            contagem_palavras[i] = 1

    print(contagem_palavras)
except KeyboardInterrupt:
    print("Interrompido pelo usuário!")
except ValueError:
    print("Entrada inválida")
"""


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

user_valido = [usuario for usuario in usuarios if usuario['email']]
print(user_valido)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
lista = [x for x in range(50)]

pares = [pares for pares in lista if pares % 2 ==0]
print(pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]



### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.