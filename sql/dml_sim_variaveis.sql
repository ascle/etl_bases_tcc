
-- Tabela sim.tb_acidtrab
INSERT INTO sim.tb_acidtrab(id, cv_descricao) VALUES (0, '???');
INSERT INTO sim.tb_acidtrab(id, cv_descricao) VALUES (1, 'Sim');
INSERT INTO sim.tb_acidtrab(id, cv_descricao) VALUES (2, 'Não');
INSERT INTO sim.tb_acidtrab(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_ALTCAUSA
INSERT INTO sim.TB_ALTCAUSA(id, cv_descricao) VALUES (1, 'Sim');
INSERT INTO sim.TB_ALTCAUSA(id, cv_descricao) VALUES (2, 'Não');

-- Tabela sim.TB_ASSISTMED
INSERT INTO sim.TB_ASSISTMED(id, cv_descricao) VALUES (0, '???');
INSERT INTO sim.TB_ASSISTMED(id, cv_descricao) VALUES (1, 'Sim');
INSERT INTO sim.TB_ASSISTMED(id, cv_descricao) VALUES (2, 'Não');
INSERT INTO sim.TB_ASSISTMED(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_ATESTANTE
INSERT INTO sim.TB_ATESTANTE(id, cv_descricao) VALUES (0, '???');
INSERT INTO sim.TB_ATESTANTE(id, cv_descricao) VALUES (1, 'Sim');
INSERT INTO sim.TB_ATESTANTE(id, cv_descricao) VALUES (2, 'Substituto');
INSERT INTO sim.TB_ATESTANTE(id, cv_descricao) VALUES (3, 'IML');
INSERT INTO sim.TB_ATESTANTE(id, cv_descricao) VALUES (4, 'SVO');
INSERT INTO sim.TB_ATESTANTE(id, cv_descricao) VALUES (5, 'Outros');

-- Tabela sim.TB_CIRCOBITO
INSERT INTO sim.TB_CIRCOBITO(id, cv_descricao) VALUES (1, 'Acidente');
INSERT INTO sim.TB_CIRCOBITO(id, cv_descricao) VALUES (2, 'Suicídio');
INSERT INTO sim.TB_CIRCOBITO(id, cv_descricao) VALUES (3, 'Homicídio');
INSERT INTO sim.TB_CIRCOBITO(id, cv_descricao) VALUES (4, 'Outros');
INSERT INTO sim.TB_CIRCOBITO(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_CIRURGIA
INSERT INTO sim.TB_CIRURGIA(id, cv_descricao) VALUES (0, '???');
INSERT INTO sim.TB_CIRURGIA(id, cv_descricao) VALUES (1, 'Sim');
INSERT INTO sim.TB_CIRURGIA(id, cv_descricao) VALUES (2, 'Não');
INSERT INTO sim.TB_CIRURGIA(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_ESC
INSERT INTO sim.TB_ESC(id, cv_descricao, in_anos_max) VALUES (1, 'Nenhuma', 0);
INSERT INTO sim.TB_ESC(id, cv_descricao, in_anos_max) VALUES (2, '1 a 3 anos', 3);
INSERT INTO sim.TB_ESC(id, cv_descricao, in_anos_max) VALUES (3, '4 a 7 anos', 7);
INSERT INTO sim.TB_ESC(id, cv_descricao, in_anos_max) VALUES (4, '8 a 11 anos', 11);
INSERT INTO sim.TB_ESC(id, cv_descricao, in_anos_max) VALUES (5, '12 anos e mais', 100);
INSERT INTO sim.TB_ESC(id, cv_descricao, in_anos_max) VALUES (9, 'Ignorado', NULL);

-- Tabela sim.TB_ESC2010
INSERT INTO sim.TB_ESC2010(id, cv_descricao) VALUES (0, 'Sem escolaridade');
INSERT INTO sim.TB_ESC2010(id, cv_descricao) VALUES (1, 'Fundamental I (1ª a 4ª série)');
INSERT INTO sim.TB_ESC2010(id, cv_descricao) VALUES (2, 'Fundamental II (5ª a 8ª série)');
INSERT INTO sim.TB_ESC2010(id, cv_descricao) VALUES (3, 'Médio (antigo 2º Grau)');
INSERT INTO sim.TB_ESC2010(id, cv_descricao) VALUES (4, 'Superior incompleto');
INSERT INTO sim.TB_ESC2010(id, cv_descricao) VALUES (5, 'Superior completo');
INSERT INTO sim.TB_ESC2010(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_ESCFALAGR1
INSERT INTO sim.TB_ESCFALAGR1(id, cv_descricao) VALUES (0, 'Sem Escolaridade');
INSERT INTO sim.TB_ESCFALAGR1(id, cv_descricao) VALUES (1, 'Fundamental I Incompleto');
INSERT INTO sim.TB_ESCFALAGR1(id, cv_descricao) VALUES (2, 'Fundamental I Completo');
INSERT INTO sim.TB_ESCFALAGR1(id, cv_descricao) VALUES (3, 'Fundamental II Incompleto');
INSERT INTO sim.TB_ESCFALAGR1(id, cv_descricao) VALUES (4, 'Fundamental II Completo');
INSERT INTO sim.TB_ESCFALAGR1(id, cv_descricao) VALUES (5, 'Ensino Médio Incompleto');
INSERT INTO sim.TB_ESCFALAGR1(id, cv_descricao) VALUES (6, 'Ensino Médio Completo');
INSERT INTO sim.TB_ESCFALAGR1(id, cv_descricao) VALUES (7, 'Superior Incompleto');
INSERT INTO sim.TB_ESCFALAGR1(id, cv_descricao) VALUES (8, 'Superior Completo');
INSERT INTO sim.TB_ESCFALAGR1(id, cv_descricao) VALUES (9, 'Ignorado');
INSERT INTO sim.TB_ESCFALAGR1(id, cv_descricao) VALUES (10, 'Fundamental I Incompleto ou Inespecífico');
INSERT INTO sim.TB_ESCFALAGR1(id, cv_descricao) VALUES (11, 'Fundamental II Incompleto ou Inespecífico');
INSERT INTO sim.TB_ESCFALAGR1(id, cv_descricao) VALUES (12, 'Ensino Médio Incompleto ou Inespecífico');

-- Tabela sim.TB_ESCMAE
INSERT INTO sim.TB_ESCMAE(id, in_esc_max, cv_descricao) VALUES (1, 0, 'Nenhuma');
INSERT INTO sim.TB_ESCMAE(id, in_esc_max, cv_descricao) VALUES (2, 3, '1 a 3 anos');
INSERT INTO sim.TB_ESCMAE(id, in_esc_max, cv_descricao) VALUES (3, 7, '4 a 7 anos');
INSERT INTO sim.TB_ESCMAE(id, in_esc_max, cv_descricao) VALUES (4, 11, '8 a 11 ano');
INSERT INTO sim.TB_ESCMAE(id, in_esc_max, cv_descricao) VALUES (5, 50, '5 – 12 anos e mais');
INSERT INTO sim.TB_ESCMAE(id, in_esc_max, cv_descricao) VALUES (9, NULL, 'Ignorado');

-- Tabela sim.TB_ESCMAE2010
INSERT INTO sim.TB_ESCMAE2010(id, cv_descricao) VALUES (0, 'Sem escolaridade');
INSERT INTO sim.TB_ESCMAE2010(id, cv_descricao) VALUES (1, 'Fundamental I (1ª a 4ª série)');
INSERT INTO sim.TB_ESCMAE2010(id, cv_descricao) VALUES (2, 'Fundamental II (5ª a 8ª série)');
INSERT INTO sim.TB_ESCMAE2010(id, cv_descricao) VALUES (3, 'Médio (antigo 2º Grau)');
INSERT INTO sim.TB_ESCMAE2010(id, cv_descricao) VALUES (4, 'Superior incompleto');
INSERT INTO sim.TB_ESCMAE2010(id, cv_descricao) VALUES (5, 'Superior completo');
INSERT INTO sim.TB_ESCMAE2010(id, cv_descricao) VALUES (9, 'Ignorado');


-- Tabela sim.TB_ESCMAEAGR1
INSERT INTO sim.TB_ESCMAEAGR1(id, cv_descricao) VALUES (0, 'Sem Escolaridade');
INSERT INTO sim.TB_ESCMAEAGR1(id, cv_descricao) VALUES (1, 'Fundamental I Incompleto');
INSERT INTO sim.TB_ESCMAEAGR1(id, cv_descricao) VALUES (2, 'Fundamental I Completo');
INSERT INTO sim.TB_ESCMAEAGR1(id, cv_descricao) VALUES (3, 'Fundamental II Incompleto');
INSERT INTO sim.TB_ESCMAEAGR1(id, cv_descricao) VALUES (4, 'Fundamental II Completo');
INSERT INTO sim.TB_ESCMAEAGR1(id, cv_descricao) VALUES (5, 'Ensino Médio Incompleto');
INSERT INTO sim.TB_ESCMAEAGR1(id, cv_descricao) VALUES (6, 'Ensino Médio Completo');
INSERT INTO sim.TB_ESCMAEAGR1(id, cv_descricao) VALUES (7, 'Superior Incompleto');
INSERT INTO sim.TB_ESCMAEAGR1(id, cv_descricao) VALUES (8, 'Superior Completo');
INSERT INTO sim.TB_ESCMAEAGR1(id, cv_descricao) VALUES (9, 'Ignorado');
INSERT INTO sim.TB_ESCMAEAGR1(id, cv_descricao) VALUES (10, 'Fundamental I Incompleto ou Inespecífico');
INSERT INTO sim.TB_ESCMAEAGR1(id, cv_descricao) VALUES (11, 'Fundamental II Incompleto ou Inespecífico');
INSERT INTO sim.TB_ESCMAEAGR1(id, cv_descricao) VALUES (12, 'Ensino Médio Incompleto ou Inespecífico');

-- Tabela sim.TB_ESTCIV
INSERT INTO sim.TB_ESTCIV(id, cv_descricao) VALUES (1, 'Solteiro');
INSERT INTO sim.TB_ESTCIV(id, cv_descricao) VALUES (2, 'Casado');
INSERT INTO sim.TB_ESTCIV(id, cv_descricao) VALUES (3, 'Viúvo');
INSERT INTO sim.TB_ESTCIV(id, cv_descricao) VALUES (4, 'Separado judicialmente/divorciado');
INSERT INTO sim.TB_ESTCIV(id, cv_descricao) VALUES (5, 'União estável');
INSERT INTO sim.TB_ESTCIV(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_ESTCIVIL
INSERT INTO sim.TB_ESTCIVIL(id, cv_descricao) VALUES (0, '???');
INSERT INTO sim.TB_ESTCIVIL(id, cv_descricao) VALUES (1, 'Solteiro');
INSERT INTO sim.TB_ESTCIVIL(id, cv_descricao) VALUES (2, 'Casado');
INSERT INTO sim.TB_ESTCIVIL(id, cv_descricao) VALUES (3, 'Viúvo');
INSERT INTO sim.TB_ESTCIVIL(id, cv_descricao) VALUES (4, 'Separado judicialmente');
INSERT INTO sim.TB_ESTCIVIL(id, cv_descricao) VALUES (5, 'União consensual (versões anteriores)');
INSERT INTO sim.TB_ESTCIVIL(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_EXAME
INSERT INTO sim.TB_EXAME(id, cv_descricao) VALUES (0, '???');
INSERT INTO sim.TB_EXAME(id, cv_descricao) VALUES (1, 'Sim');
INSERT INTO sim.TB_EXAME(id, cv_descricao) VALUES (2, 'Não');
INSERT INTO sim.TB_EXAME(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_FONTE
INSERT INTO sim.TB_FONTE(id, cv_descricao) VALUES (1, 'Ocorrência policial');
INSERT INTO sim.TB_FONTE(id, cv_descricao) VALUES (2, 'Hospital');
INSERT INTO sim.TB_FONTE(id, cv_descricao) VALUES (3, 'Família');
INSERT INTO sim.TB_FONTE(id, cv_descricao) VALUES (4, 'Outra');
INSERT INTO sim.TB_FONTE(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_FONTEINV
INSERT INTO sim.TB_FONTEINV(id, cv_descricao) VALUES (1, 'Comitê de Morte Materna e/ou Infantil');
INSERT INTO sim.TB_FONTEINV(id, cv_descricao) VALUES (2, 'Visita domiciliar / Entrevista família');
INSERT INTO sim.TB_FONTEINV(id, cv_descricao) VALUES (3, 'Estabelecimento de Saúde / Prontuário');
INSERT INTO sim.TB_FONTEINV(id, cv_descricao) VALUES (4, 'Relacionado com outros bancos de dados');
INSERT INTO sim.TB_FONTEINV(id, cv_descricao) VALUES (5, 'SVO');
INSERT INTO sim.TB_FONTEINV(id, cv_descricao) VALUES (6, 'IML');
INSERT INTO sim.TB_FONTEINV(id, cv_descricao) VALUES (7, 'Outra fonte');
INSERT INTO sim.TB_FONTEINV(id, cv_descricao) VALUES (8, 'Múltiplas fontes');
INSERT INTO sim.TB_FONTEINV(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_GESTACAO
INSERT INTO sim.TB_GESTACAO(id, int_sem_max, cv_descricao) VALUES (1, 21, 'Até 21 semanas');
INSERT INTO sim.TB_GESTACAO(id, int_sem_max, cv_descricao) VALUES (2, 27, '22 a 27 semanas');
INSERT INTO sim.TB_GESTACAO(id, int_sem_max, cv_descricao) VALUES (3, 31, '28 a 31 semanas');
INSERT INTO sim.TB_GESTACAO(id, int_sem_max, cv_descricao) VALUES (4, 36, '32 a 36 semanas');
INSERT INTO sim.TB_GESTACAO(id, int_sem_max, cv_descricao) VALUES (5, 41, '37 a 41 semanas');
INSERT INTO sim.TB_GESTACAO(id, int_sem_max, cv_descricao) VALUES (6, 50, '42 e + semanas');

-- Tabela sim.TB_GRAVIDEZ
INSERT INTO sim.TB_GRAVIDEZ(id, cv_descricao) VALUES (1, 'Única');
INSERT INTO sim.TB_GRAVIDEZ(id, cv_descricao) VALUES (2, 'Dupla');
INSERT INTO sim.TB_GRAVIDEZ(id, cv_descricao) VALUES (3, 'Tripla e mais');
INSERT INTO sim.TB_GRAVIDEZ(id, cv_descricao) VALUES (9, 'Ignorada');

-- Tabela sim.TB_INSTRUCAO
INSERT INTO sim.TB_INSTRUCAO(id, cv_descricao) VALUES (0, 'Ignorado');
INSERT INTO sim.TB_INSTRUCAO(id, cv_descricao) VALUES (1, 'Nenhuma');
INSERT INTO sim.TB_INSTRUCAO(id, cv_descricao) VALUES (2, 'Primeiro grau');
INSERT INTO sim.TB_INSTRUCAO(id, cv_descricao) VALUES (3, 'Segundo grau');
INSERT INTO sim.TB_INSTRUCAO(id, cv_descricao) VALUES (4, 'Superior');
INSERT INTO sim.TB_INSTRUCAO(id, cv_descricao) VALUES (9, '???');

-- Tabela sim.TB_LOCACID
INSERT INTO sim.TB_LOCACID(id, cv_descricao) VALUES (0, 'Ignorado');
INSERT INTO sim.TB_LOCACID(id, cv_descricao) VALUES (1, 'Via Publica');
INSERT INTO sim.TB_LOCACID(id, cv_descricao) VALUES (2, 'Domicilio');
INSERT INTO sim.TB_LOCACID(id, cv_descricao) VALUES (3, 'Outro');
INSERT INTO sim.TB_LOCACID(id, cv_descricao) VALUES (4, 'Local de trabalho');

-- Tabela sim.TB_LOCOCOR
INSERT INTO sim.TB_LOCOCOR(id, cv_descricao) VALUES (0, '???');
INSERT INTO sim.TB_LOCOCOR(id, cv_descricao) VALUES (1, 'Hospital');
INSERT INTO sim.TB_LOCOCOR(id, cv_descricao) VALUES (2, 'Outros estabelecimentos de saúde');
INSERT INTO sim.TB_LOCOCOR(id, cv_descricao) VALUES (3, 'Domicílio');
INSERT INTO sim.TB_LOCOCOR(id, cv_descricao) VALUES (4, 'Via pública');
INSERT INTO sim.TB_LOCOCOR(id, cv_descricao) VALUES (5, 'Outros');
INSERT INTO sim.TB_LOCOCOR(id, cv_descricao) VALUES (6, 'Aldeia indígena');
INSERT INTO sim.TB_LOCOCOR(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_MORTEPARTO
INSERT INTO sim.TB_MORTEPARTO(id, cv_descricao) VALUES (1, 'Antes');
INSERT INTO sim.TB_MORTEPARTO(id, cv_descricao) VALUES (2, 'Durante');
INSERT INTO sim.TB_MORTEPARTO(id, cv_descricao) VALUES (3, 'Depois');
INSERT INTO sim.TB_MORTEPARTO(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_NECROPSIA
INSERT INTO sim.TB_NECROPSIA(id, cv_descricao) VALUES (0, '???');
INSERT INTO sim.TB_NECROPSIA(id, cv_descricao) VALUES (1, 'Sim');
INSERT INTO sim.TB_NECROPSIA(id, cv_descricao) VALUES (2, 'Não');
INSERT INTO sim.TB_NECROPSIA(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_OBITOGRAV
INSERT INTO sim.TB_OBITOGRAV(id, cv_descricao) VALUES (1, 'Sim');
INSERT INTO sim.TB_OBITOGRAV(id, cv_descricao) VALUES (2, 'Não');
INSERT INTO sim.TB_OBITOGRAV(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_OBITOPARTO
INSERT INTO sim.TB_OBITOPARTO(id, cv_descricao) VALUES (1, 'Antes');
INSERT INTO sim.TB_OBITOPARTO(id, cv_descricao) VALUES (2, 'Durante');
INSERT INTO sim.TB_OBITOPARTO(id, cv_descricao) VALUES (3, 'Depois');
INSERT INTO sim.TB_OBITOPARTO(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_OBITOPUERP
INSERT INTO sim.TB_OBITOPUERP(id, cv_descricao) VALUES (1, 'Sim, até 42 dias após o parto');
INSERT INTO sim.TB_OBITOPUERP(id, cv_descricao) VALUES (2, 'Sim, de 43 dias a 1 ano');
INSERT INTO sim.TB_OBITOPUERP(id, cv_descricao) VALUES (3, 'Não');
INSERT INTO sim.TB_OBITOPUERP(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_PARTO
INSERT INTO sim.TB_PARTO(id, cv_descricao) VALUES (1, 'Vaginal');
INSERT INTO sim.TB_PARTO(id, cv_descricao) VALUES (2, 'Cesáreo');
INSERT INTO sim.TB_PARTO(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_RACACOR
INSERT INTO sim.TB_RACACOR(id, cv_descricao) VALUES (1, 'Branca');
INSERT INTO sim.TB_RACACOR(id, cv_descricao) VALUES (2, 'Preta');
INSERT INTO sim.TB_RACACOR(id, cv_descricao) VALUES (3, 'Amarela');
INSERT INTO sim.TB_RACACOR(id, cv_descricao) VALUES (4, 'Parda');
INSERT INTO sim.TB_RACACOR(id, cv_descricao) VALUES (5, 'Indígena');

-- Tabela sim.TB_SEMANGEST
INSERT INTO sim.TB_SEMANGEST(id, in_semanas_max, cv_descricao) VALUES (0, NULL, 'Ignorado');
INSERT INTO sim.TB_SEMANGEST(id, in_semanas_max, cv_descricao) VALUES (1, 19, 'Menos de 20 semanas');
INSERT INTO sim.TB_SEMANGEST(id, in_semanas_max, cv_descricao) VALUES (2, 27, '20 a 27 semanas');
INSERT INTO sim.TB_SEMANGEST(id, in_semanas_max, cv_descricao) VALUES (3, 50, '28 e mais semanas');
INSERT INTO sim.TB_SEMANGEST(id, in_semanas_max, cv_descricao) VALUES (4, 20, 'Menos de 21 semanas');
INSERT INTO sim.TB_SEMANGEST(id, in_semanas_max, cv_descricao) VALUES (5, 27, '22 a 27 semanas');
INSERT INTO sim.TB_SEMANGEST(id, in_semanas_max, cv_descricao) VALUES (6, 36, '28 a 36 semanas');
INSERT INTO sim.TB_SEMANGEST(id, in_semanas_max, cv_descricao) VALUES (7, 41, '37 a 41 semanas');
INSERT INTO sim.TB_SEMANGEST(id, in_semanas_max, cv_descricao) VALUES (8, 50, '42 semanas e mais');

-- Tabela sim.TB_SEXO
INSERT INTO sim.TB_SEXO(id, cv_descricao) VALUES (1, 'Masculino');
INSERT INTO sim.TB_SEXO(id, cv_descricao) VALUES (2, 'Feminino');

-- Tabela sim.TB_TIPOACID
INSERT INTO sim.TB_TIPOACID(id, cv_descricao) VALUES (0, 'Ignorado');
INSERT INTO sim.TB_TIPOACID(id, cv_descricao) VALUES (1, 'Atropelamento');
INSERT INTO sim.TB_TIPOACID(id, cv_descricao) VALUES (2, 'Demais acidentes de transito');
INSERT INTO sim.TB_TIPOACID(id, cv_descricao) VALUES (3, 'Queda');
INSERT INTO sim.TB_TIPOACID(id, cv_descricao) VALUES (4, 'Afogamento');
INSERT INTO sim.TB_TIPOACID(id, cv_descricao) VALUES (5, 'Outros tipos de acidente');

-- Tabela sim.TB_TIPOBITO
INSERT INTO sim.TB_TIPOBITO(id, cv_descricao) VALUES (1, 'Fetal');
INSERT INTO sim.TB_TIPOBITO(id, cv_descricao) VALUES (2, 'Não-fetal');

-- Tabela sim.TB_TIPOGRAV
INSERT INTO sim.TB_TIPOGRAV(id, cv_descricao) VALUES (0, '???');
INSERT INTO sim.TB_TIPOGRAV(id, cv_descricao) VALUES (1, 'Única');
INSERT INTO sim.TB_TIPOGRAV(id, cv_descricao) VALUES (2, 'Dupla');
INSERT INTO sim.TB_TIPOGRAV(id, cv_descricao) VALUES (3, 'Triplice');
INSERT INTO sim.TB_TIPOGRAV(id, cv_descricao) VALUES (4, 'Mais de 3');

-- Tabela sim.TB_TIPOPARTO
INSERT INTO sim.TB_TIPOPARTO(id, cv_descricao) VALUES (0, 'Ignorado');
INSERT INTO sim.TB_TIPOPARTO(id, cv_descricao) VALUES (1, 'Espontaneo');
INSERT INTO sim.TB_TIPOPARTO(id, cv_descricao) VALUES (2, 'Operatorio');
INSERT INTO sim.TB_TIPOPARTO(id, cv_descricao) VALUES (3, 'Forceps');
INSERT INTO sim.TB_TIPOPARTO(id, cv_descricao) VALUES (4, 'Outro');

-- Tabela sim.TB_TIPOVIOL
INSERT INTO sim.TB_TIPOVIOL(id, cv_descricao) VALUES (0, 'Ignorado');
INSERT INTO sim.TB_TIPOVIOL(id, cv_descricao) VALUES (1, 'Homicidio');
INSERT INTO sim.TB_TIPOVIOL(id, cv_descricao) VALUES (2, 'Suicidio');
INSERT INTO sim.TB_TIPOVIOL(id, cv_descricao) VALUES (3, 'Acidente');
INSERT INTO sim.TB_TIPOVIOL(id, cv_descricao) VALUES (4, 'Outros tipos de violencia');

-- Tabela sim.TB_TPMORTEOCO
INSERT INTO sim.TB_TPMORTEOCO(id, cv_descricao) VALUES (1, 'Na gravidez');
INSERT INTO sim.TB_TPMORTEOCO(id, cv_descricao) VALUES (2, 'No parto');
INSERT INTO sim.TB_TPMORTEOCO(id, cv_descricao) VALUES (3, 'No abortamento');
INSERT INTO sim.TB_TPMORTEOCO(id, cv_descricao) VALUES (4, 'Até 42 dias após o término do parto');
INSERT INTO sim.TB_TPMORTEOCO(id, cv_descricao) VALUES (5, 'De 43 dias a 1 ano após o término da gestação');
INSERT INTO sim.TB_TPMORTEOCO(id, cv_descricao) VALUES (8, 'Não ocorreu nestes períodos');
INSERT INTO sim.TB_TPMORTEOCO(id, cv_descricao) VALUES (9, 'Ignorado');

-- Tabela sim.TB_TPOBITOCOR
INSERT INTO sim.TB_TPOBITOCOR(id, cv_descricao) VALUES (1, 'Durante a gestação');
INSERT INTO sim.TB_TPOBITOCOR(id, cv_descricao) VALUES (2, 'Durante o abortamento');
INSERT INTO sim.TB_TPOBITOCOR(id, cv_descricao) VALUES (3, 'Após o abortamento');
INSERT INTO sim.TB_TPOBITOCOR(id, cv_descricao) VALUES (4, 'No parto ou até 1 hora após o parto');
INSERT INTO sim.TB_TPOBITOCOR(id, cv_descricao) VALUES (5, 'No puerpério - até 42 dias após o parto');
INSERT INTO sim.TB_TPOBITOCOR(id, cv_descricao) VALUES (6, 'Entre 43 dias e até 1 ano após o parto');
INSERT INTO sim.TB_TPOBITOCOR(id, cv_descricao) VALUES (7, 'A investigação não identificou o momento do óbito');
INSERT INTO sim.TB_TPOBITOCOR(id, cv_descricao) VALUES (8, 'Mais de um ano após o parto');
INSERT INTO sim.TB_TPOBITOCOR(id, cv_descricao) VALUES (9, 'O óbito não ocorreu nas circunstancias anteriores');

-- Tabela sim.TB_TPPOS
INSERT INTO sim.TB_TPPOS(id, cv_descricao) VALUES (1, 'Sim');
INSERT INTO sim.TB_TPPOS(id, cv_descricao) VALUES (2, 'Não');

-- Tabela sim.TB_TPRESGINFO
INSERT INTO sim.TB_TPRESGINFO(id, cv_descricao) VALUES (1, 'Não acrescentou nem corrigiu informação');
INSERT INTO sim.TB_TPRESGINFO(id, cv_descricao) VALUES (2, 'Sim, permitiu o resgate de novas informações');
INSERT INTO sim.TB_TPRESGINFO(id, cv_descricao) VALUES (3, 'Sim, permitiu a correção de alguma das causas informadas riginalmente');
