-- === Concessionária BLV Motors ===

-- create database concessionaria;


-- ===================== CLIENTES =====================

create table clientes (
	id_cliente serial primary key,
	nome varchar(250) not null,
	cpf varchar(11) unique not null
		check (cpf ~ '^[0-9]{11}$'),
	telefone varchar(15) not null,
	data_nascimento date not null,
	email varchar(150) unique,
	logradouro varchar(150) not null,
	numero varchar(10) not null,
	complemento varchar(100),
	bairro varchar(100) not null,
	cidade varchar(100) not null,
	uf varchar(2) not null
		check (uf in ('AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO')),
	cep varchar(8) not null
		check (cep ~ '^[0-9]{8}$')
);

-- ===================== FUNCIONÁRIOS =====================

create table cargo_funcionario (
	id_cargo serial primary key,
	nome varchar(50) unique not null
);

insert into cargo_funcionario (nome) values
	('Mecânico'),
	('Vendedor'),
	('Gerente');

create table funcionarios (
	id_funcionario serial primary key,
	id_cargo int not null,
	nome varchar(250) not null,
	cpf varchar(11) unique not null
		check (cpf ~ '^[0-9]{11}$'),
	telefone varchar(15) not null,
	data_nascimento date not null,
	email varchar(150) unique not null,
	data_admissao date not null,
	logradouro varchar(150) not null,
	numero varchar(10) not null,
	complemento varchar(100),
	bairro varchar(100) not null,
	cidade varchar(100) not null,
	uf varchar(2) not null
		check (uf in ('AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO')),
	cep varchar(8) not null
		check (cep ~ '^[0-9]{8}$'),

	check (data_admissao > data_nascimento),

	foreign key (id_cargo) references cargo_funcionario(id_cargo)
);

-- ===================== CATÁLOGO =====================

create table marcas (
	id_marca serial primary key,
	nome varchar(50) unique not null
);

insert into marcas (nome) values
	('Fiat'),
	('Volkswagen'),
	('Chevrolet'),
	('Toyota'),
	('Hyundai');

create table categorias (
	id_categoria serial primary key,
	nome varchar(50) unique not null
);

insert into categorias (nome) values
	('Hatch'),
	('Sedan'),
	('SUV'),
	('Picape'),
	('Utilitário');

create table modelos (
	id_modelo serial primary key,
	id_marca int not null,
	id_categoria int not null,
	nome varchar(100) not null,
	motorizacao varchar(30) not null,
	tipo_combustivel varchar(20) not null
		check (tipo_combustivel in ('gasolina', 'etanol', 'flex', 'diesel', 'eletrico', 'hibrido')),

	foreign key (id_marca) references marcas(id_marca),
	foreign key (id_categoria) references categorias(id_categoria)
);


-- ===================== FORNECEDORES =====================

create table fornecedores (
	id_fornecedor serial primary key,
	razao_social varchar(250) not null,
	cnpj varchar(14) unique not null
		check (cnpj ~ '^[0-9]{14}$'),
	telefone varchar(15) not null,
	email varchar(150) unique not null,
	logradouro varchar(150) not null,
	numero varchar(10) not null,
	complemento varchar(100),
	bairro varchar(100) not null,
	cidade varchar(100) not null,
	uf varchar(2) not null
		check (uf in ('AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO')),
	cep varchar(8) not null
		check (cep ~ '^[0-9]{8}$')
);

-- ===================== VEÍCULOS =====================

create table veiculos (
	id_veiculo serial primary key,
	id_modelo int not null,
	chassi varchar(17) unique not null
		check (chassi ~ '^[A-HJ-NPR-Z0-9]{17}$'),
	placa varchar(7) unique
		check (placa ~ '^[A-Z]{3}[0-9]{4}$' or placa ~ '^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$'),
	ano_fabricacao int not null check (ano_fabricacao >= 1900),
	ano_modelo int not null,
	cor varchar(30) not null,

	check (ano_modelo between ano_fabricacao and ano_fabricacao + 1),

	foreign key (id_modelo) references modelos(id_modelo)
);


-- ===================== ENTRADAS NO ESTOQUE =====================

create table entradas_estoque (
	id_entrada serial primary key,
	id_veiculo int not null,
	id_fornecedor int,
	id_pagamento int unique,
	data_entrada date not null default current_date,
	quilometragem_entrada int not null
		check (quilometragem_entrada >= 0),
	condicao_entrada varchar(10) not null
		check (condicao_entrada in ('novo', 'seminovo')),
	preco_tabela numeric(10,2) not null
		check (preco_tabela > 0),
	valor_aquisicao_fornecedor numeric(10,2)
		check (valor_aquisicao_fornecedor > 0),
	observacoes_conservacao text,

	check (condicao_entrada = 'novo' or quilometragem_entrada > 0),

	check (
		(id_fornecedor is not null and id_pagamento is null)
		or
		(id_fornecedor is null and id_pagamento is not null)
	),

	check ((id_fornecedor is not null) = (valor_aquisicao_fornecedor is not null)),

	foreign key (id_veiculo) references veiculos(id_veiculo),
	foreign key (id_fornecedor) references fornecedores(id_fornecedor)
);


-- ===================== VENDAS =====================

create table vendas (
	id_venda serial primary key,
	id_entrada int not null unique,
	id_cliente int not null,
	id_funcionario int not null,
	data_venda date not null default current_date,
	valor_venda numeric(10,2) not null
		check (valor_venda > 0),

	foreign key (id_entrada) references entradas_estoque(id_entrada),
	foreign key (id_cliente) references clientes(id_cliente),
	foreign key (id_funcionario) references funcionarios(id_funcionario)
);


-- ===================== PAGAMENTOS =====================

create table pagamentos (
	id_pagamento serial primary key,
	id_venda int not null,
	tipo varchar(15) not null
		check (tipo in ('dinheiro', 'pix', 'cartao', 'financiamento', 'troca')),
	valor numeric(10,2) not null
		check (valor > 0),
	data_pagamento date not null,

	foreign key (id_venda) references vendas(id_venda)
);

alter table entradas_estoque
	add foreign key (id_pagamento) references pagamentos(id_pagamento);

create table financiamentos (
	id_pagamento int primary key,
	instituicao_financeira varchar(150) not null,
	numero_contrato varchar(100) not null,
	quantidade_parcelas int not null
		check (quantidade_parcelas > 0),
	taxa_juros_mensal numeric(6,3) not null
		check (taxa_juros_mensal >= 0),
	valor_financiado numeric(10,2) not null
		check (valor_financiado > 0),
	valor_total_parcelas numeric(12,2) not null
		check (valor_total_parcelas >= valor_financiado),

	unique (instituicao_financeira, numero_contrato),

	foreign key (id_pagamento) references pagamentos(id_pagamento)
);


-- ===================== AVALIAÇÕES =====================

create table avaliacoes (
	id_avaliacao serial primary key,
	id_entrada int not null unique,
	id_funcionario int not null,
	data_avaliacao date not null default current_date,
	quilometragem_apurada int not null
		check (quilometragem_apurada >= 0),
	valor_atribuido numeric(10,2) not null
		check (valor_atribuido > 0),
	observacoes_conservacao text not null,

	foreign key (id_entrada) references entradas_estoque(id_entrada),
	foreign key (id_funcionario) references funcionarios(id_funcionario)
);


-- ===================== HISTÓRICO DE ESTOQUE =====================

create table historico_estoque (
	id_historico serial primary key,
	id_entrada int not null,
	situacao varchar(20) not null
		check (situacao in ('disponivel', 'reservado', 'em_manutencao', 'vendido')),
	data_inicial date not null default current_date,
	data_final date
		check (data_final is null or data_final >= data_inicial),

	foreign key (id_entrada) references entradas_estoque(id_entrada)
);


-- ===================== MANUTENÇÕES =====================

create table manutencoes (
	id_manutencao serial primary key,
	id_entrada int not null,
	data_entrada date not null default current_date,
	data_saida date
		check (data_saida is null or data_saida >= data_entrada),
	descricao_servico text not null,
	custo numeric(10,2) not null
		check (custo > 0),

	foreign key (id_entrada) references entradas_estoque(id_entrada)
);