from etl import etl_sim as etl


def executar_etl_sim_79_84():
    for ano in range(1979, 1984 + 1):
        etl.etl_sim_79(ano)


def executar_etl_sim_85_92():
    etl.etl_sim_85(1985)
    etl.etl_sim_86(1986)
    etl.etl_sim_87(1987)
    etl.etl_sim_87(1988)
    etl.etl_sim_87(1989)
    etl.etl_sim_90(1990)
    etl.etl_sim_91(1991)
    etl.etl_sim_92(1992)


if __name__ == '__main__':
    executar_etl_sim_79_84()
    executar_etl_sim_85_92()
    # etl.etl_sim_92(1993) # Erro!!!
    etl.etl_sim_92(1994)
    etl.etl_sim_95(1995)
    etl.etl_sim_96(1996)
