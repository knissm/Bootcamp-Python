lista_de_numeros: list = [40,50,60,70,0,-4089246,1,50]


def ordenar_lista_de_numeros(numeros: list) -> list:
    lista = numeros.copy()

    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

    return lista

lista_nova = ordenar_lista_de_numeros(lista_de_numeros)
print(lista_nova)
