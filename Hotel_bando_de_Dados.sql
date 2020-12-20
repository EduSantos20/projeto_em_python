Create schema hotel;
use hotel;
CREATE TABLE Cadastro_hospede(
    NOME TEXT NOT NULL,
	CPF VARCHAR(11) NOT NULL,
    primary key(CPF),
    EMAIL TEXT NOT NULL,
	TELEFONE TEXT NOT NULL
);
create table Detalhe_hospedagem(
	NUMERO_QUARTO int NOT NULL,
    primary key(NUMERO_QUARTO),
	TIPO_QUARTO text not null,
    QUANTIDADE_DIARIA TEXT NOT NULL,
    ALIMENTACAO TEXT NOT NULL,
    VALOR_QUARTO TEXT NOT NULL,
    VALOR_TOTAL TEXT NOT NULL,
    CHECK_IN date
);

create TABLE Produto(
	CODIGO_PRODUTO varchar(3) NOT NULL,
    primary key(CODIGO_PRODUTO),
    NOME_PRODUTRO TEXT NOT NULL,
    VALOR_PRODUTO TEXT NOT NULL
);

CREATE table Cadastro_consumo(
	ID INT NOT null auto_increment,
    primary key(ID),
	NUMERO_QUARTO_CONSUMO int NOT NULL,
    foreign key(NUMERO_QUARTO_CONSUMO) REFERENCES Detalhe_hospedagem(NUMERO_QUARTO),
    CODIGO_PRODUTO_CONSUMO varchar(3) NOT NULL,
    foreign key (CODIGO_PRODUTO_CONSUMO) REFERENCES Produto (CODIGO_PRODUTO),
    QUANTIDADE_CONSUMO TEXT NOT NULL
);
