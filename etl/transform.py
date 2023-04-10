
def transform_sim_79(dados):
    dados.drop(columns=['CONTADOR', 'CODIGO', 'AREARES', 'NATURAL', 'OBITOFE1',
                        'OBITOFE2', 'FONTINFO', 'NUMEXPORT', 'CRSOCOR', 'CRSRES',
                        'MUNIRES'], inplace=True)

    dados.rename(columns=str.lower, inplace=True)
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
    dados['OCUPMAE'] = dados['OCUPMAE'].replace('0.0', str(0))
    dados['OCUPMAE'] = dados['OCUPMAE'].replace('0 0', str(0))
    dados['OCUPMAE'] = dados['OCUPMAE'].replace('x80', None)
    dados['OCUPPAI'] = dados['OCUPPAI'].replace(0.0, None)
    dados['OCUPPAI'] = dados['OCUPPAI'].replace('0.0', None)
    dados['OCUPPAI'] = dados['OCUPPAI'].replace('X80', None)
    dados['IDADEMAE'] = dados['IDADEMAE'].replace('0.', str(0))
    dados['IDADEMAE'] = dados['IDADEMAE'].replace('.', None)
    dados['IDADEMAE'] = dados['IDADEMAE'].replace('..', None)
    dados['OCUPACAO'] = dados['OCUPACAO'].replace('+', None)
    dados['OCUPACAO'] = dados['OCUPACAO'].replace('+++', None)
    dados['OCUPACAO'] = dados['OCUPACAO'].replace('.', None)
    dados['OCUPACAO'] = dados['OCUPACAO'].replace('00.', None)
    dados['OCUPACAO'] = dados['OCUPACAO'].replace('.0.', None)
    dados['OCUPACAO'] = dados['OCUPACAO'].replace('.0', None)
    dados['OCUPACAO'] = dados['OCUPACAO'].replace(.0, None)
    dados['OCUPACAO'] = dados['OCUPACAO'].replace('0.0', None)
    dados['OCUPACAO'] = dados['OCUPACAO'].replace('x90', None)
    dados['OCUPACAO'] = dados['OCUPACAO'].replace('x20', None)
    dados['OCUPACAO'] = dados['OCUPACAO'].replace('x60', None)
    dados['OCUPACAO'] = dados['OCUPACAO'].replace('x70', None)
    dados['FILHVIVOS'] = dados['FILHVIVOS'].replace('0.', str(0))
    dados['FILHVIVOS'] = dados['FILHVIVOS'].replace(0., None)
    dados['PESONASC'] = dados['PESONASC'].replace('0 00', None)
    dados['REGISTRO'] = dados['REGISTRO'].replace('00)740', None)
    dados['REGISTRO'] = dados['REGISTRO'].replace('0#7535', None)


def transform_sim_95(dados):
    dados['tipoacid'] = dados['tipoacid'].astype('Int64')
