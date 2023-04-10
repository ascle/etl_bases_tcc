import os
import dao

# ************** Extract **************
def extract(path_origem, name_file):
    path_completo = os.path.join(path_origem, name_file)
    return dao.openFile(path_completo)

def extract_ibge_municipio():
    path_origem = dao.get_path_ibge()
    base_file_name = 'RELATORIO_DTB_BRASIL_MUNICIPIO.csv'
    return extract(path_origem, base_file_name)

def extract_cbo2002():
    path_origem = dao.get_path_cbo()
    base_file_name = 'CBO2002 - Ocupacao.csv'
    return extract(path_origem, base_file_name)

def extract_cbo2002_subGrupo():
    path_origem = dao.get_path_cbo()
    base_file_name = 'CBO2002 - SubGrupo.csv'
    return extract(path_origem, base_file_name)

def extract_cbo2002_grandeGrupo():
    path_origem = dao.get_path_cbo()
    base_file_name = 'CBO2002 - Grande Grupo.csv'
    return extract(path_origem, base_file_name)

def extract_cid10():
    path_origem = dao.get_path_cid10()
    base_file_name = ''
    return extract(path_origem, base_file_name)

def extract_linkage_marco():
    path_origem = dao.get_path_lkg_marco()
    base_file_name = 'dn.csv'
    return extract(path_origem, base_file_name)

def extract_sim(ano):
    path_origem = dao.get_path_sim()
    name_file = 'Mortalidade_Geral_'+ ano+'.csv'
    path_completo = os.path.join(path_origem, name_file)
    return dao.openFileSim79(path_completo)

def extract_sim_96(ano):
    path_origem = dao.get_path_sim()
    name_file = 'Mortalidade_Geral_'+ ano+'.csv'
    path_completo = os.path.join(path_origem, name_file)
    return dao.openFileSim96(path_completo)