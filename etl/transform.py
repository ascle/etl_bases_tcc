import numpy as np

def transform_sim_79(dados):
    dados.drop(columns=['contador', 'codigo', 'areares', 'natural', 'obitofe1',
                        'obitofe2', 'fontinfo', 'numexport', 'crsocor', 'crsres',
                        'munires'], inplace=True)

    dados['ocuppai'] = dados['ocuppai'].replace('.', None)
    dados['ocuppai'] = dados['ocuppai'].astype('Int64')
    dados['instrpai'] = dados['instrpai'].astype('Int64')
    dados['ocupmae'] = dados['ocupmae'].astype('Int64')
    dados['idademae'] = dados['idademae'].astype('Int64')
    dados['instrmae'] = dados['instrmae'].astype('Int64')
    dados['semangest'] = dados['semangest'].astype('Int64')
    dados['tipograv'] = dados['tipograv'].astype('Int64')
    dados['tipoparto'] = dados['tipoparto'].astype('Int64')
    dados['filhmort'] = dados['filhmort'].replace('XX', 0)
    dados['filhvivos'] = dados['filhvivos'].replace('XX', 0)

def transform_sim_85(dados):
    dados['filhvivos'] = dados['filhvivos'].replace(0, str(0))
    dados['filhvivos'] = dados['filhvivos'].astype('Int64')

def transform_sim_86(dados):
    dados['filhvivos'] = dados['filhvivos'].astype('Int64')

def transform_sim_87(dados):
    dados['filhvivos'] = dados['filhvivos'].replace(0, str(0))
    dados['filhvivos'] = dados['filhvivos'].astype('Int64')

def transform_sim_90(dados):
    dados['estcivil'] = dados['estcivil'].astype('Int64')
    dados['lococor'] = dados['lococor'].astype('Int64')
    dados['ocupacao'] = dados['ocupacao'].astype('Int64')
    dados['instrucao'] = dados['instrucao'].astype('Int64')
    dados['assistmed'] = dados['assistmed'].astype('Int64')
    dados['atestante'] = dados['atestante'].astype('Int64')
    dados['exame'] = dados['exame'].astype('Int64')
    dados['cirurgia'] = dados['cirurgia'].astype('Int64')
    dados['necropsia'] = dados['necropsia'].astype('Int64')
    dados['tipoviol'] = dados['tipoviol'].astype('Int64')
    dados['acidtrab'] = dados['acidtrab'].astype('Int64')
    dados['locacid'] = dados['locacid'].astype('Int64')

def transform_sim_91(dados):
    dados['sexo'] = dados['sexo'].astype('Int64')
    dados['idade'] = dados['idade'].astype('Int64')
    dados['registro'] = dados['registro'].astype('Int64')
    dados['critica'] = dados['critica'].astype('Int64')


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
            #print('{}:{}'.format(column, dados[column].dtypes))
            dados[column] = dados[column].astype('Int64')
