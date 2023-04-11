from etl import extract as E, load as L


def etl_uf():
    df_ibge = E.extract_ibge_municipio()
    df_ibge.drop(columns=['Regiao_Geografica_Intermediaria','Nome_Regiao_Geografica_Intermediaria','Codigo_Municipio_Completo', 'Regiao_Geografica_Imediata','Nome_Regiao_Geografica_Imediata','Mesorregiao_Geografica','Nome_Municipio', 'Nome_Microrregiao', 'Municipio', 'Nome_Mesorregiao', 'Microrregiao_Geografica'], inplace=True)
    df_ibge.drop_duplicates(subset='UF', inplace=True)
    df_ibge.rename(columns=str.lower, inplace=True)
    L.load(df_ibge, 'tb_ibge_uf')

def etl_municipios():
    df_ibge = E.extract_ibge_municipio()
    df_ibge.rename(columns=str.lower, inplace=True)
    df_ibge.drop(columns=['nome_uf'], inplace=True)
    #print(df_ibge)
    L.load(df_ibge, 'tb_ibge_municipios')

if __name__ == '__main__':
    etl_uf()
    etl_municipios()
