from etl import extract as E

if __name__ == '__main__':
    dados = E.extract_cid10()
    #dados.rename(columns=str.lower, inplace=True)
    #print(dados.columns)
    #L.load(dados, 'tb_cid_10')
