import pandas as pd
import os
import psycopg2

# ************** Constantes **************
date_parser = lambda c: pd.to_datetime(c, format='%d%m%Y', errors='coerce')

# ************** PATHs **************
def get_path_bases():
    return os.path.join('H:\\', 'Meu Drive', 'UFS', 'tcc-2-ascle-ufs', 'bases')

def get_path_ibge():
    return os.path.join(get_path_bases(), 'ibge_municipios')

def get_path_cbo():
    return os.path.join(get_path_bases(), 'cbo_20002')

def get_path_cid10():
    return os.path.join(get_path_bases(), 'cid_10')

def get_path_lkg_marco():
    return os.path.join(get_path_bases(), 'linkage_marco')

def get_path_sim():
    return os.path.join(get_path_bases(), 'sim')

def get_adrs_conn():
    return dict(
        host='localhost',
        port='5432',
        database='tcc',
        user='postgres',
        password='123456'
    )

# ************** Banco de Dados **************
def get_conn(adrs_conn):
    return psycopg2.connect(host=adrs_conn['host'], port=adrs_conn['port'], database=adrs_conn['database'],
                            user=adrs_conn['user'], password=adrs_conn['password'])

# https://pt.stackoverflow.com/questions/262867/o-que-s%C3%A3o-as-siglas-ddl-dml-dql-dtl-e-dcl
# ************** Manipula Arquivos **************
def openFile(name_file):
    if get_path_lkg_marco() in name_file:
        return pd.read_csv(name_file, delimiter=',', low_memory=False)
    else:
        return pd.read_csv(name_file, delimiter=';', low_memory=False)

def openFileSim79(name_file):
        return pd.read_csv(name_file, delimiter=';', low_memory=False,
                       parse_dates=['DATAREG', 'DATAOBITO', 'DATANASC'], date_parser=date_parser)

def openFileSim96(name_file):
    return pd.read_csv(name_file, delimiter=';', low_memory=False,
                       parse_dates=['DTOBITO', 'DTNASC'], date_parser=date_parser)

# https://stackoverflow.com/questions/19472922/reading-external-sql-script-in-python
def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r', encoding='utf-8')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')
    conn = get_conn(get_adrs_conn())
    cur = conn.cursor()
    # Execute every command from the input file
    for command in sqlCommands:
        if command:
            try:
                cur.execute(str(command))
                conn.commit()
            except psycopg2.Error as errorMsg:
                print('Erro: ')
                print(errorMsg)
                conn.rollback()
