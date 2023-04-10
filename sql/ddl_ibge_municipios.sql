CREATE TABLE tb_ibge_uf(
	uf INTEGER NOT NULL PRIMARY KEY,
	nome_uf VARCHAR(20)
);

CREATE TABLE tb_ibge_municipios(
	Codigo_Municipio_Completo INTEGER primary key,
	uf INTEGER,
	CONSTRAINT fk_UF FOREIGN KEY(uf) REFERENCES tb_ibge_uf(uf),
	Regiao_Geografica_Intermediaria INTEGER,
	Nome_Regiao_Geografica_Intermediaria character varying,
	Regiao_Geografica_Imediata INTEGER,
	Nome_Regiao_Geografica_Imediata character varying,
	Mesorregiao_Geografica INTEGER,
	Nome_Mesorregiao character varying,
	Microrregiao_Geografica INTEGER,
	Nome_Microrregiao character varying,
	Municipio INTEGER,
	Nome_Municipio character varying
);
