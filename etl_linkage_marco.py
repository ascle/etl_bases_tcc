from etl import etl_linkage as etl

def print_coluna_valores(dados):
    for column in dados:
        print(column)
        print(dados[column].unique())


if __name__ == '__main__':
    #etl.etl_linkage_cru_to_DB()
    etl.etl_linkage_limpeza()




