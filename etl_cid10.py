import extract as E
import load as L

if __name__ == '__main__':
    dados = E.extract_cid10()
    #dados.rename(columns=str.lower, inplace=True)
    #print(dados.columns)
    #L.load(dados, 'tb_cid_10')
