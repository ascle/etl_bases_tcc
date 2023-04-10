import numpy as np

import extract as E
import load as L
import transform_lkg_marco as dic

def print_coluna_valores(dados):
    for column in dados:
        print(column)
        print(dados[column].unique())

def etl_lkg():
    dados = E.extract_linkage_marco()
    dados.rename(columns=str.lower, inplace=True)
    #print_coluna_valores(dados)

    dados['consultas'] = dados['consultas'].map(dic.iconsultas)
    dados['escmae'] = dados['escmae'].map(dic.iescmae)
    dados['escmae2010'] = dados['escmae2010'].map(dic.iescmae2010)
    dados['escmaeagr1'] = dados['escmaeagr1'].map(dic.iescmaeagr1)
    dados['estcivmae'] = dados['estcivmae'].map(dic.iestcivmae)
    dados['gestacao'] = dados['gestacao'].map(dic.igestacao)
    dados['gravidez'] = dados['gravidez'].map(dic.igravidez)
    dados['idanomal'] = dados['idanomal'].map(dic.iidanomal)
    dados['locnasc'] = dados['locnasc'].map(dic.ilocnasc)
    dados['parto'] = dados['parto'].map(dic.iparto)
    dados['sexo'] = dados['sexo'].map(dic.isexo)
    dados['stcesparto'] = dados['stcesparto'].map(dic.istcesparto)
    dados['sttrabpart'] = dados['sttrabpart'].map(dic.isttrabpart)
    dados['tpapresent'] = dados['tpapresent'].map(dic.itpapresent)
    dados['tpdocresp'] = dados['tpdocresp'].map(dic.itpdocresp)
    dados['tpfuncresp'] = dados['tpfuncresp'].map(dic.itpfuncresp)
    dados['tpmetestim'] = dados['tpmetestim'].map(dic.itpmetestim)
    dados['tpnascassi'] = dados['tpnascassi'].map(dic.itpnascassi)
    dados['obt_neonatal'] = dados['obt_neonatal'].map(dic.iboolean)
    dados['stdnnova'] = dados['stdnnova'].map(dic.iboolean)

    dados['estcivmae'] = dados['estcivmae'].astype("Int64")
    dados['escmae'] = dados['escmae'].astype("Int64")
    dados['gestacao'] = dados['gestacao'].astype("Int64")
    dados['gravidez'] = dados['gravidez'].astype("Int64")
    dados['parto'] = dados['parto'].astype("Int64")
    dados['sexo'] = dados['sexo'].astype("Int64")
    dados['idanomal'] = dados['idanomal'].astype("Int64")
    dados['qtdgestant'] = dados['qtdgestant'].astype("Int64")
    dados['qtdpartnor'] = dados['qtdpartnor'].astype("Int64")
    dados['qtdpartces'] = dados['qtdpartces'].astype("Int64")
    dados['consprenat'] = dados['consprenat'].astype("Int64")
    dados['apgar1'] = dados['apgar1'].astype("Int64")
    dados['apgar5'] = dados['apgar5'].astype("Int64")
    dados['semagestac'] = dados['semagestac'].astype("Int64")
    dados['escmae2010'] = dados['escmae2010'].astype("Int64")
    dados['racacormae'] = dados['racacormae'].astype("Int64")
    dados['tpapresent'] = dados['tpapresent'].astype("Int64")
    dados['sttrabpart'] = dados['sttrabpart'].astype("Int64")
    dados['tpnascassi'] = dados['tpnascassi'].astype("Int64")
    dados['tpfuncresp'] = dados['tpfuncresp'].astype("Int64")
    dados['tpdocresp'] = dados['tpdocresp'].astype("Int64")
    dados['escmaeagr1'] = dados['escmaeagr1'].astype("Int64")
    dados['idade_obt'] = dados['idade_obt'].astype("Int64")
    dados['tpmetestim'] = dados['tpmetestim'].astype("Int64")
    dados['idadepai'] = dados['idadepai'].astype("Int64")
    dados['seriescmae'] = dados['seriescmae'].astype("Int64")
    dados['stcesparto'] = dados['stcesparto'].astype("Int64")

    #L.load(dados, "linkage")
    return dados

if __name__ == '__main__':
    dados = etl_lkg()
    #dados.info()



