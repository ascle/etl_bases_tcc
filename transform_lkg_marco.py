boolean = {
    True: 'Sim',
    False: 'Nao',
}
iboolean = {v: k for k, v in boolean.items()}

consultas = {
    0: 'Ignorado',
    1: 'Nenhuma',
    2: 'de_1_a_3',
    3: 'de_4_a_6',
    4: '7_e_mais'
}
iconsultas = {v: k for k, v in consultas.items()}

escmae = {
    0: 'Ignorado',
    1: '0',
    2: 'Nenhuma',
    3: '1_a_3_anos',
    4: '4_a_7_anos',
    5: '8_a_11_anos',
    6: '12_e_mais'
}
iescmae = {v: k for k, v in escmae.items()}

escmae2010 = {
    0: 'Ignorado',
    1: 'Sem_escolaridade',
    2: 'Fundamental_II_(5a_a_8a_serie)',
    3: 'Fundamental_I_(1a_a_4a_serie)',
    4: 'Medio_(antigo_2o_Grau)',
    5: 'Superior_incompleto',
    6: 'Superior_completo'
}
iescmae2010 = {v: k for k, v in escmae2010.items()}

escmaeagr1 = {
    0: 'Ignorado',
    1: 'Sem_Escolaridade',
    2: 'Fundamental_II_Incompleto_ou_Inespecifico',
    3: 'Fundamental_I_Incompleto',
    4: 'Ensinomedio_Incompleto_ou_Inespecifico',
    5: 'Fundamental_II_Completo',
    6: 'Fundamental_I_Incompleto_ou_Inespecifico',
    7: 'Ensino_Medio_Completo',
    8: 'Fundamental_II_Incompleto',
    9: 'Superior_Incompleto',
    10: 'Fundamental_I_Completo',
    11: 'Ensino_Medio_Incompleto',
    12: 'Superior_Completo'
}
iescmaeagr1 = {v: k for k, v in escmaeagr1.items()}

estcivmae = {
    0: 'Ignorado',
    1: 'Casada',
    2: 'Solteira',
    3: 'Uniao_consensual_(versoes_anteriores)',
    4: 'Separado_judicialmente/Divorciado',
    5: 'Viuva'
}
iestcivmae = {v: k for k, v in estcivmae.items()}

gestacao = {
    0: 'Ignorado',
    1: 'Menos_de_22_semanas',
    2: '22_a_27_semanas',
    3: '28_a_31_semanas',
    4: '32_a_36_semanas',
    5: '37_a_41_semanas',
    6: '42_semanas_e_mais'
}
igestacao = {v: k for k, v in gestacao.items()}

gravidez = {
    0: 'Ignorado',
    1: 'Unica',
    2: 'Dupla',
    3: 'Tripla_e_mais'
}
igravidez = {v: k for k, v in gravidez.items()}

idanomal = {
    0: 'Ignorado',
    1: 'Nao',
    2: 'Sim'
}
iidanomal = {v: k for k, v in idanomal.items()}

locnasc = {
    0: 'Ignorado',
    1: 'Outros',
    2: 'Outro_Estab_Saude',
    3: 'Hospital',
    4: 'Domicilio'
}
ilocnasc = {v: k for k, v in locnasc.items()}

parto = {
    0: 'Cesareo',
    1: 'Vaginal'
}
iparto = {v: k for k, v in parto.items()}

sexo = {
    0: 'Ignorado',
    1: 'Feminino',
    2: 'Masculino'
}
isexo = {v: k for k, v in sexo.items()}

stcesparto = {
    0: 'Ignorado',
    1: 'Nao_se_aplica',
    2: 'Nao',
    3: 'Sim'
}
istcesparto = {v: k for k, v in stcesparto.items()}

sttrabpart = {
    0: 'Ignorado',
    1: 'Nao',
    2: 'Sim',
}
isttrabpart = {v: k for k, v in sttrabpart.items()}

tpapresent = {
    0: 'Ignorado',
    1: 'Cefalico',
    2: 'Pelvica_ou_podalica',
    3: 'Transversa',
}
itpapresent = {v: k for k, v in tpapresent.items()}

tpdocresp = {
    0: 'Ignorado',
    1: 'RG',
    2: 'CPF',
    3: 'COREN',
    4: 'CNES',
    5: 'CRM',
}
itpdocresp = {v: k for k, v in tpdocresp.items()}

tpfuncresp = {
    0: 'Medico',
    1: 'Enfermeiro',
    2: 'Funcionario_do_cartorio',
    3: 'Parteira',
    4: 'Outros',
}
itpfuncresp = {v: k for k, v in tpfuncresp.items()}

tpmetestim = {
    0: 'Ignorado',
    1: 'Outro_metodo',
    2: 'Exame_fisico',
}
itpmetestim = {v: k for k, v in tpmetestim.items()}

tpnascassi = {
    0: 'Ignorado',
    1: 'Medico',
    2: 'Parteira',
    3: 'Enfermeira/obstetriz',
    4: 'Outros',
}
itpnascassi = {v: k for k, v in tpnascassi.items()}
