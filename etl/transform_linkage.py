import numpy as np

from utils import dicionario_lkg as dic


def transform_linkage(dados):
    dados.rename(columns=str.lower, inplace=True)
    # print_coluna_valores(dados)

    # dados['consultas'] = dados['consultas'].map(dic.iconsultas)
    # dados['escmae'] = dados['escmae'].map(dic.iescmae)
    # dados['escmae2010'] = dados['escmae2010'].map(dic.iescmae2010)
    # dados['escmaeagr1'] = dados['escmaeagr1'].map(dic.iescmaeagr1)
    # dados['estcivmae'] = dados['estcivmae'].map(dic.iestcivmae)
    # dados['gestacao'] = dados['gestacao'].map(dic.igestacao)
    # dados['gravidez'] = dados['gravidez'].map(dic.igravidez)
    # dados['idanomal'] = dados['idanomal'].map(dic.iidanomal)
    # dados['locnasc'] = dados['locnasc'].map(dic.ilocnasc)
    # dados['parto'] = dados['parto'].map(dic.iparto)
    # dados['sexo'] = dados['sexo'].map(dic.isexo)
    # dados['stcesparto'] = dados['stcesparto'].map(dic.istcesparto)
    # dados['sttrabpart'] = dados['sttrabpart'].map(dic.isttrabpart)
    # dados['tpapresent'] = dados['tpapresent'].map(dic.itpapresent)
    # dados['tpdocresp'] = dados['tpdocresp'].map(dic.itpdocresp)
    # dados['tpfuncresp'] = dados['tpfuncresp'].map(dic.itpfuncresp)
    # dados['tpmetestim'] = dados['tpmetestim'].map(dic.itpmetestim)
    # dados['tpnascassi'] = dados['tpnascassi'].map(dic.itpnascassi)
    # dados['obt_neonatal'] = dados['obt_neonatal'].map(dic.iboolean)
    # dados['stdnnova'] = dados['stdnnova'].map(dic.iboolean)


def transform_linkage_codanormal(dados):
    # Criando o campo CODANOMAL_QTD com a quantidade de anomalias
    dados['codanomal_qtd'] = dados['codanomal']
    dados.drop(columns=['codanomal'], inplace=True)
    dados['codanomal_qtd'] = dados['codanomal_qtd'].apply(
        lambda x: x.count('Q') if (x != None and type(x) != float) else None)
    # Verificando os 0's
    selecao = (dados['codanomal_qtd'] == 0)
    dados['codanomal_qtd'] = dados['codanomal_qtd'].apply(lambda x: 1 if (x == 0) else x)
    dados['codanomal_qtd'].fillna(0, inplace=True)


def transform_linkage_apgar1(dados):
    selecao = dados['apgar1'] > 10
    dados.drop(dados[selecao].index, inplace=True)


def transform_linkage_apgar5(dados):
    selecao = dados['apgar5'] > 10
    dados.drop(dados[selecao].index, inplace=True)


def transform_linkage_ESCMAEETL(dados):
    # Tratando SERIESCMAE
    seriesmae = {
        0: 'Sem_Escolaridade',
        1: 'Fundamental_1',
        2: 'Fundamental_1',
        3: 'Fundamental_1',
        4: 'Fundamental_1',
        5: 'Fundamental_2',
        6: 'Fundamental_2',
        7: 'Fundamental_2',
        8: 'Fundamental_2',
    }
    dados['seriescmae'] = dados['seriescmae'].map(seriesmae)

    # Tratando ESCMAE
    escmae = {
        'Ignorado': 'Ignorado',
        '0': 'Ignorado',
        'Nenhuma': 'Sem_Escolaridade',
        '1_a_3_anos': 'Fundamental_1',
        '4_a_7_anos': 'Fundamental_2',
        '8_a_11_anos': 'Medio',
        '12_e_mais': 'Superior'
    }
    dados['escmae'] = dados['escmae'].map(escmae)

    # Tratando ESCMAEAGR1
    escmaeagr1 = {
        'Ignorado': 'Ignorado',
        'Sem_Escolaridade': 'Sem_Escolaridade',
        'Fundamental_I_Incompleto_ou_Inespecifico': 'Fundamental_1',
        'Fundamental_I_Incompleto': 'Fundamental_1',
        'Fundamental_I_Completo': 'Fundamental_1',
        'Fundamental_II_Incompleto_ou_Inespecifico': 'Fundamental_2',
        'Fundamental_II_Incompleto': 'Fundamental_2',
        'Fundamental_II_Completo': 'Fundamental_2',
        'Ensinomedio_Incompleto_ou_Inespecifico': 'Medio',
        'Ensino_Medio_Incompleto': 'Medio',
        'Ensino_Medio_Completo': 'Medio',
        'Superior_Incompleto': 'Superior',
        'Superior_Completo': 'Superior'
    }
    dados['escmaeagr1'] = dados['escmaeagr1'].map(escmaeagr1)

    # Tratando ESCMAE2010
    escmae2010 = {
        'Ignorado': 'Ignorado',
        'Sem_escolaridade': 'Sem_Escolaridade',
        'Fundamental_I_(1a_a_4a_serie)': 'Fundamental_1',
        'Fundamental_II_(5a_a_8a_serie)': 'Fundamental_2',
        'Ensinomedio_Incompleto_ou_Inespecifico': 'Medio',
        'Medio_(antigo_2o_Grau)': 'Medio',
        'Superior_incompleto': 'Superior',
        'Superior_completo': 'Superior'
    }
    dados['escmae2010'] = dados['escmae2010'].map(escmae2010)

    dados['escmaeetl'] = np.nan
    dados['escmaeetl'] = dados['escmaeagr1']
    dados['escmaeetl'].fillna(dados['escmae2010'], inplace=True)
    dados['escmaeetl'].fillna(dados['escmae'], inplace=True)
    dados['escmaeetl'].fillna(dados['seriescmae'], inplace=True)
    dados.drop(columns=['escmaeagr1', 'escmae2010', 'escmae', 'seriescmae'], inplace=True)


def transform_linkage_prenatal(dados):
    dados['consprenat'].fillna(dados['consultas'], inplace=True)
    dados['consprenat'].replace('Nenhuma', 0, inplace=True)
    dados['consprenat'].replace('de_4_a_6', 5, inplace=True)

    dados.drop(columns=['consultas'])

def transform_linkage_semanas_gestacao(dados):
    print('Método não implementado')
    # print(dados['GESTACAO'].value_counts(dropna=False))
    # print()
    # print(dados['SEMAGESTAC'].value_counts(dropna=False))


def transform_linkage_raca_mae(dados):
    racacormae = {
        1: 'Branca',
        2: 'Preta',
        3: 'amarela',
        4: 'Parda',
        5: 'Indigena',
        9: 'Ignorado',
    }
    dados['racacormae'] = dados['racacormae'].map(racacormae)
