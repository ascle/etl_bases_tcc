import numpy as np


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


