from . import extract as E
from . import transform_linkage as T
from . import load as L
from . import transform
import dao
import os


def etl_linkage_cru_to_DB():
    dao.executeScriptsFromFile('sql/ddl_linkage.sql')
    dao.executeScriptsFromFile('sql/dml_linkage.sql')
    L.load(get_etl_linkage_cru(), "tb_linkage")


def get_etl_linkage_cru():
    dados = E.extract_linkage_marco()
    dados.rename(columns=str.lower, inplace=True)
    T.transform_linkage(dados)
    transform.convert_float64_to_Int64(dados)
    return dados


def etl_linkage_limpeza():
    dados = get_etl_linkage_cru()
    T.transform_linkage_codanormal(dados)
    T.transform_linkage_apgar1(dados)
    T.transform_linkage_apgar5(dados)
    T.transform_linkage_ESCMAEETL(dados)
    # T.transform_linkage_prenatal(dados)
    T.transform_linkage_semanas_gestacao(dados)
    T.transform_linkage_raca_mae(dados)
    path = os.path.join(dao.get_path_lkg_marco(), 'dn_etl.csv')
    dao.salvar_csv(dados, path)

