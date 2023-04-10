import extract as E
import load as L

if __name__ == '__main__':
    dados_ocupacao = E.extract_cbo2002()
    dados_ocupacao.rename(columns=str.lower, inplace=True)
    L.load(dados_ocupacao, 'tb_cbo_2002')

    dados_sub = E.extract_cbo2002_subGrupo()
    dados_sub.rename(columns=str.lower, inplace=True)
    L.load(dados_sub, 'tb_cbo_2002')

    dados_grande = E.extract_cbo2002_grandeGrupo()
    dados_grande.rename(columns=str.lower, inplace=True)
    L.load(dados_grande, 'tb_cbo_2002')
