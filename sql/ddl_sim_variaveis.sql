-- Tabelas da estrutura do SIM.

-- SCHEMA: sim
CREATE SCHEMA sim AUTHORIZATION postgres;
COMMENT ON SCHEMA sim IS 'Tabelas da estrutura do SIM.';

-- ACIDTRAB
CREATE TABLE sim.TB_ACIDTRAB(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_ACIDTRAB IS 'Indica se o evento que desencadeou o óbito está relacionado ao processo de trabalho. (1 – sim; 2 – não; 9 – ignorado)';


-- ALTCAUSA
CREATE TABLE sim.TB_ALTCAUSA(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_ALTCAUSA IS 'Indica se houve correção ou alteração da causa do óbito após investigação. (1- Sim; 2 – Não)';


-- ASSISTMED
CREATE TABLE sim.TB_ASSISTMED(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_ASSISTMED IS 'Se refere ao atendimento médico continuado que o paciente recebeu, ou não,durante a enfermidade que ocasionou o óbito. (1 – sim; 2 – não; 9 – ignorado)';


-- ATESTANTE
CREATE TABLE sim.TB_ATESTANTE(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_ATESTANTE IS 'Indica se o medico que assina atendeu o paciente. 1: Sim, 2: Substituto, 3: IML, 4: SVO, 5: Outros';


-- CIRCOBITO
CREATE TABLE sim.TB_CIRCOBITO(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_CIRCOBITO IS 'Tipo de morte violenta ou circunstâncias em que se deu a morte não natural.(1 – acidente; 2 – suicídio; 3 – homicídio; 4 – outros; 9 – ignorado)';


-- CIRURGIA
CREATE TABLE sim.TB_CIRURGIA(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (8) NOT NULL
);
COMMENT ON TABLE sim.TB_CIRURGIA IS 'Realização de cirurgia. (1 – sim; 2 – não; 9 – ignorado)';


-- ESC
CREATE TABLE sim.TB_ESC(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (15) NOT NULL,
	in_anos_max INTEGER
);
COMMENT ON TABLE sim.TB_ESC IS 'Escolaridade em anos. (1 – Nenhuma; 2 – de 1 a 3 anos; 3 – de 4 a 7 anos; 4 – de 8 a 11 anos; 5 – 12 anos e mais; 9 – Ignorado)';


-- ESC2010
CREATE TABLE sim.TB_ESC2010(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (30) NOT NULL
);
COMMENT ON TABLE sim.TB_ESC2010 IS 'Escolaridade 2010. Nível da última série concluída pelo falecido. (0 – Sem escolaridade; 1 – Fundamental I (1ª a 4ª série); 2 – Fundamental II (5ª a 8ª série); 3 – Médio (antigo 2º Grau); 4 – Superior incompleto; 5 – Superior completo; 9 – Ignorado)';


-- ESCFALAGR1
CREATE TABLE sim.TB_ESCFALAGR1(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (50) NOT NULL
);
COMMENT ON TABLE sim.TB_ESCFALAGR1 IS 'Escolaridade do falecido agregada (formulário a partir de 2010). (00 – Sem Escolaridade; 01 – Fundamental I Incompleto; 02 – Fundamental I Completo; 03 – Fundamental II Incompleto; 04 – Fundamental II Completo; 05 – Ensino Médio Incompleto; 06 – Ensino Médio Completo; 07 – Superior Incompleto; 08 – Superior Completo; 09 – Ignorado; 10 – Fundamental I Incompleto ou Inespecífico; 11 – Fundamental II Incompleto ou Inespecífico; 12 – Ensino Médio Incompleto ou Inespecífico)';


--  ESCMAE
CREATE TABLE sim.TB_ESCMAE(
    id INTEGER PRIMARY KEY,
	in_esc_max INTEGER,
    cv_descricao VARCHAR (20) NOT NULL
);
COMMENT ON TABLE sim.TB_ESCMAE IS 'Escolaridade da mãe em anos. (1 – Nenhuma; 2 – de 1 a 3 anos; 3 – de 4 a 7 anos; 4 – de 8 a 11 anos; 5 – 12 anos e mais; 9 – Ignorado)';


--  ESCMAE2010
CREATE TABLE sim.TB_ESCMAE2010(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (30) NOT NULL
);
COMMENT ON TABLE sim.TB_ESCMAE2010 IS 'Escolaridade 2010. Nível da última série concluída pela mãe. (0 – Sem escolaridade; 1 – Fundamental I (1ª a 4ª série); 2 – Fundamental II (5ª a 8ª série); 3 – Médio (antigo 2º Grau); 4 – Superior incompleto; 5 – Superior completo; 9 – Ignorado)';


-- ESCMAEAGR1
CREATE TABLE sim.TB_ESCMAEAGR1(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (50) NOT NULL
);
COMMENT ON TABLE sim.TB_ESCMAEAGR1 IS 'Escolaridade da mãe agregada (formulário a partir de 2010). (00 – Sem Escolaridade; 01 – Fundamental I Incompleto; 02 – Fundamental I Completo; 03 – Fundamental II Incompleto; 04 – Fundamental II Completo; 05 – Ensino Médio Incompleto; 06 – Ensino Médio Completo; 07 – Superior Incompleto; 08 – Superior Completo; 09 – Ignorado; 10 – Fundamental I Incompleto ou Inespecífico; 11 – Fundamental II Incompleto ou Inespecífico; 12 – Ensino Médio Incompleto ou Inespecífico)';


-- ESTCIV
CREATE TABLE sim.TB_ESTCIV(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (40) NOT NULL
);
COMMENT ON TABLE sim.TB_ESTCIV IS 'Situação conjugal do falecido informada pelos familiares. (1 – Solteiro; 2 – Casado; 3 – Viúvo; 4 – Separado judicialmente/divorciado; 5 – União estável; 9 – Ignorado)';


-- ESTCIVIL
CREATE TABLE sim.TB_ESTCIVIL(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (40) NOT NULL
);
COMMENT ON TABLE sim.TB_ESTCIVIL IS 'Estado civil, conforme a tabela: 1: Solteiro 2: Casado 3: Viúvo 4: Separado judicialmente 5: União consensual (versões anteriores) 9: Ignorado';


-- EXAME
CREATE TABLE sim.TB_EXAME(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_EXAME IS 'Realização de exame. (1 – sim; 2 – não; 9 – ignorado)';


--  FONTE
CREATE TABLE sim.TB_FONTE(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (20) NOT NULL
);
COMMENT ON TABLE sim.TB_FONTE IS 'Fonte de informação utilizada para o preenchimento dos campos 48 e 49. (1 – ocorrência policial; 2 – hospital; 3 – família; 4 – outra; 9 – ignorado)';


--  FONTEINV
CREATE TABLE sim.TB_FONTEINV(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (40) NOT NULL
);
COMMENT ON TABLE sim.TB_FONTEINV IS 'Fonte de investigação. (1 – Comitê de Morte Materna e/ou Infantil; 2 – Visita domiciliar / Entrevista família; 3 – Estabelecimento de Saúde / Prontuário; 4 – Relacionado com outros bancos de dados; 5 – S V O; 6 – I M L; 7 – Outra fonte; 8 – Múltiplas fontes; 9 – Ignorado)';


-- GESTACAO
CREATE TABLE sim.TB_GESTACAO(
    id INTEGER PRIMARY KEY,
	int_sem_max INTEGER NOT NULL,
    cv_descricao VARCHAR (20) NOT NULL
);
COMMENT ON TABLE sim.TB_GESTACAO IS 'Faixas de semanas de gestação (1 - Menos de 22 semanas; 2 - 22 a 27 semanas; 3 - 28 a 31 semanas; 4 - 32 a 36 semanas; 5 - 37 a 41 semanas; 6 - 42 e + semanas)+';


--   GRAVIDEZ
CREATE TABLE sim.TB_GRAVIDEZ(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (15) NOT NULL
);
COMMENT ON TABLE sim.TB_GRAVIDEZ IS 'Tipo de gravidez. (1 – única; 2 – dupla; 3 – tripla e mais; 9 – ignorada)';


-- INSTRUCAO
CREATE TABLE sim.TB_INSTRUCAO(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (15) NOT NULL
);
COMMENT ON TABLE sim.TB_INSTRUCAO IS 'Instrução, conforme a tabela: 0: Ignorado 1: Nenhuma 2: Primeiro grau 3: Segundo grau 4: Superior';


-- LOCACID
CREATE TABLE sim.TB_LOCACID(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (20) NOT NULL
);
COMMENT ON TABLE sim.TB_LOCACID IS 'Indica o local do acidente, se cabivel, conforme a tabela: 0: Ignorado 1: Via Publica 2: Domicilio 3: Outro 4: Local de trabalho';


--  LOCOCOR
CREATE TABLE sim.TB_LOCOCOR(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (40) NOT NULL
);
COMMENT ON TABLE sim.TB_LOCOCOR IS 'Local de ocorrência do óbito. (1 – hospital; 2 – outros estabelecimentos de saúde; 3 – domicílio; 4 – via pública; 5 – outros; 6 - aldeia indígena; 9 – ignorado)';


-- MORTEPARTO
CREATE TABLE sim.TB_MORTEPARTO(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_MORTEPARTO IS 'Momento do óbito em relação ao parto. (1 - antes; 2– durante; 3–depois; 9–Ignorado)';


--  NECROPSIA
CREATE TABLE sim.TB_NECROPSIA(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_NECROPSIA IS 'Refere-se a execução ou não de necropsia para confirmação do diagnóstico. (1 – sim; 2 – não; 9 – ignorado)';


--  OBITOGRAV
CREATE TABLE sim.TB_OBITOGRAV(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_OBITOGRAV IS 'Óbito na gravidez. (1 – sim; 2 – não; 9 – ignorado)';


--  OBITOPARTO
CREATE TABLE sim.TB_OBITOPARTO(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_OBITOPARTO IS 'Momento do óbito em relação ao parto. (1 - antes; 2– durante; 3–depois; 9–Ignorado)';


-- OBITOPUERP
CREATE TABLE sim.TB_OBITOPUERP(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (30) NOT NULL
);
COMMENT ON TABLE sim.TB_OBITOPUERP IS 'Óbito no puerpério. (1 – Sim, até 42 dias após o parto; 2 – Sim, de 43 dias a 1 ano; 3 – Não; 9 – Ignorado)';


-- PARTO
CREATE TABLE sim.TB_PARTO(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_PARTO IS 'Tipo de parto. (1 – vaginal; 2 – cesáreo; 9 – ignorado)';


-- RACACOR
CREATE TABLE sim.TB_RACACOR(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_RACACOR IS 'Cor informada pelo responsável pelas informações do falecido. (1 – Branca; 2 – Preta; 3 – Amarela; 4 – Parda; 5 – Indígena)';


-- SEMANGEST
CREATE TABLE sim.TB_SEMANGEST(
    id INTEGER PRIMARY KEY,
	in_semanas_max INTEGER,
    cv_descricao VARCHAR (20) NOT NULL
);
COMMENT ON TABLE sim.TB_SEMANGEST IS 'Semanas de gestação, conforme as tabelas: Para os anos de 1979 a 1994: 0: Ignorado 1: Menos de 20 semanas 2: 20 a 27 semanas 3: 28 e mais semanas Para os anos a partir de 1995 0: Ignorado 4: Menos de 21 semanas 5: 22 a 27 semanas 6: 28 a 36 semanas 7: 37 a 41 semanas 8: 42 semanas e mais';


--  SEXO DROP TABLE sim.TB_SEXO
CREATE TABLE sim.TB_SEXO(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_SEXO IS 'Sexo do falecido. “Ignorado” selecionada em casos especiais como cadáveres mutilados, em estado avançado de decomposição, genitália indefinida ou ermafroditismo. (M – masculino; F – feminino; I - ignorado)';


--   TIPOACID
CREATE TABLE sim.TB_TIPOACID(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (30) NOT NULL
);
COMMENT ON TABLE sim.TB_TIPOACID IS 'Indica o tipo de acidente, se cabivel: 0: Ignorado 1: Atropelamento 2: Demais acidentes de transito 3: Queda 4: Afogamento 5: Outros tipos de acidente';


-- TIPOBITO
CREATE TABLE sim.TB_TIPOBITO(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_TIPOBITO IS 'Tipo do óbito Óbito fetal: morte antes da expulsão ou da extração completa do corpo da Mãe, independentemente da duração da gravidez. Indica o óbito o fato de o feto, depois da expulsão do corpo materno, não respirar nem apresentar nenhum outro sinal de vida, como batimentos do coração, pulsações do cordão umbilical ou movimentos efetivos dos músculos de contração voluntária. (1-Fetal; 2-Não Fetal)';


--  TIPOGRAV
CREATE TABLE sim.TB_TIPOGRAV(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_TIPOGRAV IS 'Tipo de gravidez, conforme a tabela:0: Ignorado 1: Unica 2: Dupla 3: Triplice 4: Mais de 3';


--  TIPOPARTO
CREATE TABLE sim.TB_TIPOPARTO(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_TIPOPARTO IS 'Tipo de parto, conforme a tabela: 0: Ignorado 1: Espontaneo 2: Operatorio 3: Forceps 4: Outro';


-- TIPOVIOL
CREATE TABLE sim.TB_TIPOVIOL(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (25) NOT NULL
);
COMMENT ON TABLE sim.TB_TIPOVIOL IS 'Indica o tipo de violencia, se cabivel, conforme a tabela: 0: Ignorado 1: Homicidio 2: Suicidio 3: Acidente 4: Outros tipos de violencia';


--   TPMORTEOCO
CREATE TABLE sim.TB_TPMORTEOCO(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (50) NOT NULL
);
COMMENT ON TABLE sim.TB_TPMORTEOCO IS 'Situação gestacional ou pósgestacional em que ocorreu o óbito. (1 – na gravidez; 2 – no parto; 3 – no abortamento; 4 – até 42 dias após o término do parto; 5 – de 43 dias a 1 ano após o término da gestação ; 8 – não ocorreu nestes períodos; 9 – ignorado)';


--  TPOBITOCOR
CREATE TABLE sim.TB_TPOBITOCOR(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (50) NOT NULL
);
COMMENT ON TABLE sim.TB_TPOBITOCOR IS 'Momento da ocorrência do óbito. (1-Durante a gestação, 2- Durante oabortamento, 3- Após o abortamento , 4- No parto ou até 1 hora após o parto,  5- No puerpério - até 42 dias após o parto, 6- Entre 43 dias e até 1 ano após o parto, 7- A investigação não identificou o momento do óbito, 8- Mais de um ano após o parto , 9- O óbito não ocorreu nas circunstancias anteriores, Branco - Não investigado)';


--  TPPOS
CREATE TABLE sim.TB_TPPOS(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (10) NOT NULL
);
COMMENT ON TABLE sim.TB_TPPOS IS 'Óbito investigado. (1 – sim; 2 – não)';


--   TPRESGINFO
CREATE TABLE sim.TB_TPRESGINFO(
    id INTEGER PRIMARY KEY,
    cv_descricao VARCHAR (70) NOT NULL
);
COMMENT ON TABLE sim.TB_TPRESGINFO IS 'Informa se a investigação permitiu o resgate de alguma causa de óbito não informado, ou a correção de alguma antes informada. (01 - Não acrescentou nem corrigiu informação; 02 - Sim, permitiu o resgate de novas informações; 03 - Sim, permitiu a correção de alguma das causas informadas riginalmente)';
