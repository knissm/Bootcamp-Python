from etl import ler_csv,filtrar_produtos_entregues,somar_valores_dos_produtos

path_arquivo = "Aula07/vendas.csv"

lista_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_entregues(lista_produtos)
valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)

#print(valor_dos_produtos_entregues)