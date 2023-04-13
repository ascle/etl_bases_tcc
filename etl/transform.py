import numpy as np


def convert_float64_to_Int64(dados):
    for column in dados:
        if dados[column].dtypes == np.float64 and ~str(column).__eq__('PESONASC'):
            # print('{}:{}'.format(column, dados[column].dtypes))
            dados[column] = dados[column].astype('Int64')