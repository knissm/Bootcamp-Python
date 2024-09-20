is_nome_aluno: bool = False

while is_nome_aluno is not True:
    nome_aluno = input("Digite uma classe: ")
    if isinstance(nome_aluno, str):
        nome_aluno_maiusculo = nome_aluno.upper()
        print(nome_aluno_maiusculo)
        is_nome_aluno = True
    else:
        print('Você digitou uma classe incorreta, precisa ser STR')