produto_01 = {
    "nome":"sapato",
    "quantidade":39,
    "preco":13.38,
    "disponibilidade":True
}

produto_02 = {
    "nome":"TV",
    "quantidade":630,
    "preco":1999,
    "disponibilidade":False
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

print(carrinho)