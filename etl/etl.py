from . import extract as E
from . import transform as T
from . import load as L
import dao

def etl_sim_79(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    dao.executeScriptsFromFile('sql/ddl_sim_79.sql')
    T.transform_sim_79(dados)
    L.load_sim(dados, tabela='tb_sim_79')

def etl_sim_85(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    T.transform_sim_79(dados)
    T.transform_sim_85(dados)
    L.load_sim(dados, 'tb_sim_79')

def etl_sim_86(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    T.transform_sim_79(dados)
    T.transform_sim_86(dados)
    L.load_sim(dados, 'tb_sim_79')

def etl_sim_87(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    T.transform_sim_79(dados)
    T.transform_sim_87(dados)
    L.load_sim(dados, 'tb_sim_79')

def etl_sim_90(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    T.transform_sim_79(dados)
    T.transform_sim_87(dados)
    T.transform_sim_90(dados)
    L.load_sim(dados, 'tb_sim_79')

def etl_sim_91(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    T.transform_sim_79(dados)
    T.transform_sim_87(dados)
    T.transform_sim_90(dados)
    T.transform_sim_91(dados)
    L.load_sim(dados, 'tb_sim_79')

def etl_sim_92(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    T.transform_sim_92(dados)
    T.transform_sim_79(dados)
    T.transform_sim_87(dados)
    T.transform_sim_90(dados)
    T.transform_sim_91(dados)
    L.load_sim(dados, 'tb_sim_79')


def etl_sim_95(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    dao.executeScriptsFromFile('sql/ddl_sim_95.sql')
    T.transform_sim_92(dados)
    T.transform_sim_79(dados)
    T.transform_sim_87(dados)
    T.transform_sim_90(dados)
    T.transform_sim_91(dados)
    T.transform_sim_95(dados)

    L.load_sim(dados, 'tb_sim_95')

def etl_sim_96(ano):
    dados = E.extract_sim_96(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    print(dados.columns)
    #T.transform_sim_92(dados)
    #T.transform_sim_79(dados)
    #T.transform_sim_87(dados)
    #T.transform_sim_90(dados)
    T.transform_sim_91(dados)
    T.transform_sim_95(dados)

    #dados.rename(columns=str.lower, inplace=True)
    #dados.rename(columns={'dtobito':'dataobito', 'dtnasc':'datanasc'}, inplace=True)
    #dados.drop(columns=['contador', 'natural'], inplace=True)

    L.load_sim(dados, 'tb_sim_95')
