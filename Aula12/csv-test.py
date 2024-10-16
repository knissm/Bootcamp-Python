import pandas as pd

df = pd.read_csv(r"G:/Meu Drive/Estudos/Jornada de Dados/Bootcamp_Python/Aula12/exemplo.csv")

df_filtrado = df[df['estado'] == 'SC']

print(df_filtrado)


"""
Código simples, sem usar clase
"""