from etl import pipeline_calcular_kpi_de_vendas_consolidado
from pathlib import Path

if __name__ == "__main__":
    pasta_raiz = Path(__file__).parent
    pasta_entrada = pasta_raiz / 'data'
    formato_de_saida: list = ['csv']

pipeline_calcular_kpi_de_vendas_consolidado(pasta_entrada,formato_de_saida)