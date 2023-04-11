from . import extract as E
from . import transform as T
from . import load as L
import dao


def etl_sim_79(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    dao.executeScriptsFromFile('sql/ddl_sim_79.sql')
    T.convert_float64_to_Int64(dados)
    T.transform_sim_79(dados)
    L.load_sim(dados, tabela='tb_sim_79')


def etl_sim_85(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    T.convert_float64_to_Int64(dados)
    T.transform_sim_79(dados)
    T.transform_sim_85(dados)
    L.load_sim(dados, 'tb_sim_79')


def etl_sim_86(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    T.convert_float64_to_Int64(dados)
    T.transform_sim_79(dados)
    L.load_sim(dados, 'tb_sim_79')


def etl_sim_87(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    T.convert_float64_to_Int64(dados)
    T.transform_sim_79(dados)
    T.transform_sim_87(dados)
    L.load_sim(dados, 'tb_sim_79')


def etl_sim_90(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    T.convert_float64_to_Int64(dados)
    T.transform_sim_79(dados)
    T.transform_sim_87(dados)
    L.load_sim(dados, 'tb_sim_79')


def etl_sim_91(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    T.convert_float64_to_Int64(dados)
    T.transform_sim_79(dados)
    T.transform_sim_87(dados)
    L.load_sim(dados, 'tb_sim_79')


def etl_sim_92(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    T.convert_float64_to_Int64(dados)
    T.transform_sim_92(dados)
    T.transform_sim_79(dados)
    T.transform_sim_87(dados)
    L.load_sim(dados, 'tb_sim_79')


def etl_sim_95(ano):
    dados = E.extract_sim(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    dao.executeScriptsFromFile('sql/ddl_sim_95.sql')
    T.convert_float64_to_Int64(dados)
    T.transform_sim_92(dados)
    T.transform_sim_79(dados)
    T.transform_sim_87(dados)
    T.transform_sim_95(dados)

    L.load_sim(dados, 'tb_sim_95')


def etl_sim_96(ano):
    dados = E.extract_sim_96(str(ano))
    dados.rename(columns=str.lower, inplace=True)
    dados['ano'] = ano
    T.convert_float64_to_Int64(dados)
    T.transform_sim_96(dados)
    L.load_sim(dados, 'tb_sim_95')


def etl_linkage():
    dao.executeScriptsFromFile('sql/ddl_linkage.sql')
    dao.executeScriptsFromFile('sql/dml_linkage.sql')
    dados = E.extract_linkage_marco()
    dados.rename(columns=str.lower, inplace=True)
    T.transform_linkage(dados)
    T.convert_float64_to_Int64(dados)
    L.load(dados, "tb_linkage")
