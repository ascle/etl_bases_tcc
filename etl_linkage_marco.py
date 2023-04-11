from etl import etl

def print_coluna_valores(dados):
    for column in dados:
        print(column)
        print(dados[column].unique())


if __name__ == '__main__':
    etl.etl_linkage()
    #dados.info()



