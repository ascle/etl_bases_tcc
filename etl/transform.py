import numpy as np
from utils import dicionario_lkg as dic


def transform_linkage(dados):
    dados.rename(columns=str.lower, inplace=True)
    # print_coluna_valores(dados)

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
    #
    # dados['estcivmae'] = dados['estcivmae'].astype("Int64")
    # dados['escmae'] = dados['escmae'].astype("Int64")
    # dados['gestacao'] = dados['gestacao'].astype("Int64")
    # dados['gravidez'] = dados['gravidez'].astype("Int64")
    # dados['parto'] = dados['parto'].astype("Int64")
    # dados['sexo'] = dados['sexo'].astype("Int64")
    # dados['idanomal'] = dados['idanomal'].astype("Int64")
    # dados['qtdgestant'] = dados['qtdgestant'].astype("Int64")
    # dados['qtdpartnor'] = dados['qtdpartnor'].astype("Int64")
    # dados['qtdpartces'] = dados['qtdpartces'].astype("Int64")
    # dados['consprenat'] = dados['consprenat'].astype("Int64")
    # dados['apgar1'] = dados['apgar1'].astype("Int64")
    # dados['apgar5'] = dados['apgar5'].astype("Int64")
    # dados['semagestac'] = dados['semagestac'].astype("Int64")
    # dados['escmae2010'] = dados['escmae2010'].astype("Int64")
    # dados['racacormae'] = dados['racacormae'].astype("Int64")
    # dados['tpapresent'] = dados['tpapresent'].astype("Int64")
    # dados['sttrabpart'] = dados['sttrabpart'].astype("Int64")
    # dados['tpnascassi'] = dados['tpnascassi'].astype("Int64")
    # dados['tpfuncresp'] = dados['tpfuncresp'].astype("Int64")
    # dados['tpdocresp'] = dados['tpdocresp'].astype("Int64")
    # dados['escmaeagr1'] = dados['escmaeagr1'].astype("Int64")
    # dados['idade_obt'] = dados['idade_obt'].astype("Int64")
    # dados['tpmetestim'] = dados['tpmetestim'].astype("Int64")
    # dados['idadepai'] = dados['idadepai'].astype("Int64")
    # dados['seriescmae'] = dados['seriescmae'].astype("Int64")
    # dados['stcesparto'] = dados['stcesparto'].astype("Int64")




def transform_sim_79(dados):
    dados.drop(columns=['contador', 'codigo', 'areares', 'natural', 'obitofe1',
                        'obitofe2', 'fontinfo', 'numexport', 'crsocor', 'crsres',
                        'munires'], inplace=True)

    dados['ocuppai'] = dados['ocuppai'].replace('.', None)
    dados['filhmort'] = dados['filhmort'].replace('XX', 0)
    dados['filhvivos'] = dados['filhvivos'].replace('XX', 0)


def transform_sim_85(dados):
    dados['filhvivos'] = dados['filhvivos'].replace(0, str(0))


def transform_sim_87(dados):
    dados['filhvivos'] = dados['filhvivos'].replace(0, str(0))


def transform_sim_92(dados):
    dados['ocupmae'] = dados['ocupmae'].replace('0.0', str(0))
    dados['ocupmae'] = dados['ocupmae'].replace('0 0', str(0))
    dados['ocupmae'] = dados['ocupmae'].replace('x80', None)
    dados['ocuppai'] = dados['ocuppai'].replace(0.0, None)
    dados['ocuppai'] = dados['ocuppai'].replace('0.0', None)
    dados['ocuppai'] = dados['ocuppai'].replace('X80', None)
    dados['idademae'] = dados['idademae'].replace('0.', str(0))
    dados['idademae'] = dados['idademae'].replace('.', None)
    dados['idademae'] = dados['idademae'].replace('..', None)
    dados['ocupacao'] = dados['ocupacao'].replace('+', None)
    dados['ocupacao'] = dados['ocupacao'].replace('+++', None)
    dados['ocupacao'] = dados['ocupacao'].replace('.', None)
    dados['ocupacao'] = dados['ocupacao'].replace('00.', None)
    dados['ocupacao'] = dados['ocupacao'].replace('.0.', None)
    dados['ocupacao'] = dados['ocupacao'].replace('.0', None)
    dados['ocupacao'] = dados['ocupacao'].replace(.0, None)
    dados['ocupacao'] = dados['ocupacao'].replace('0.0', None)
    dados['ocupacao'] = dados['ocupacao'].replace('x90', None)
    dados['ocupacao'] = dados['ocupacao'].replace('x20', None)
    dados['ocupacao'] = dados['ocupacao'].replace('x60', None)
    dados['ocupacao'] = dados['ocupacao'].replace('x70', None)
    dados['filhvivos'] = dados['filhvivos'].replace('0.', str(0))
    dados['filhvivos'] = dados['filhvivos'].replace(0., None)
    dados['pesonasc'] = dados['pesonasc'].replace('0 00', None)
    dados['registro'] = dados['registro'].replace('00)740', None)
    dados['registro'] = dados['registro'].replace('0#7535', None)


def transform_sim_95(dados):
    dados['tipoacid'] = dados['tipoacid'].astype('Int64')


def transform_sim_96(dados):
    dados['ocup'] = dados['ocup'].replace('--700', 700)
    dados['ocup'] = dados['ocup'].replace('.0000', None)
    dados['ocup'] = dados['ocup'].replace('0.000', None)
    dados['ocup'] = dados['ocup'].replace('.0', None)
    dados['ocup'] = dados['ocup'].replace('...00', None)
    dados['ocup'] = dados['ocup'].replace('00.00', None)
    dados['idademae'] = dados['idademae'].replace('.0', None)
    dados['idademae'] = dados['idademae'].replace('..', None)
    dados['idademae'] = dados['idademae'].replace('--', None)
    dados['qtdfilmort'] = dados['qtdfilmort'].replace('XX', None)
    dados['gestacao'] = dados['gestacao'].replace('A', None)
    dados['peso'] = dados['peso'].replace('0 00', None)

    dados.rename(columns={'dtobito': 'dataobito', 'dtnasc': 'datanasc'}, inplace=True)
    dados.drop(columns=['contador', 'natural', 'obitopuerp', 'linhaa', 'linhab',
                        'linhac', 'linhad', 'linhaii', 'circobito', 'fonte'], inplace=True)


def convert_float64_to_Int64(dados):
    for column in dados:
        if dados[column].dtypes == np.float64 and ~str(column).__eq__('PESONASC'):
            # print('{}:{}'.format(column, dados[column].dtypes))
            dados[column] = dados[column].astype('Int64')
