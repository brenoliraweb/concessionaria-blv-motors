CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(250) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL
      CHECK(cpf ~ '^[0-9]{11}$'),
    telefone VARCHAR(15) NOT NULL,
    email VARCHAR(150) UNIQUE
);

CREATE TABLE funcionarios (
    id_funcionario SERIAL PRIMARY KEY,
    nome VARCHAR(250) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL
      CHECK(cpf ~ '^[0-9]{11}$'),
    telefone VARCHAR(15) NOT NULL,
    cargo VARCHAR(10) NOT NULL
      CHECK(cargo IN ('admin', 'vendedor')),
    login VARCHAR(50) UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL
);

CREATE TABLE marcas (
    id_marca SERIAL PRIMARY KEY,
    nome VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE modelos (
    id_modelo SERIAL PRIMARY KEY,
    id_marca INT NOT NULL,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(20) NOT NULL
      CHECK(categoria IN ('hatch', 'sedan', 'suv', 'picape')),

    UNIQUE(id_marca, nome),

    FOREIGN KEY (id_marca) REFERENCES marcas(id_marca)
      ON DELETE RESTRICT ON UPDATE RESTRICT
);

CREATE TABLE veiculos (
    id_veiculo SERIAL PRIMARY KEY,
    id_modelo INT NOT NULL,
    chassi VARCHAR(17) UNIQUE NOT NULL
      CHECK(chassi ~ '^[A-HJ-NPR-Z0-9]{17}$'),
    placa VARCHAR(7) UNIQUE
      CHECK(placa ~ '^[A-Z]{3}[0-9]{4}$' OR placa ~ '^[A-Z]{3}[0-9][A-Z][0-9]{2}$'),
    ano_fabricacao INT NOT NULL
      CHECK(ano_fabricacao >= 1900),
    cor VARCHAR(30) NOT NULL,
    preco_anunciado NUMERIC(10, 2) NOT NULL
      CHECK(preco_anunciado > 0),

    FOREIGN KEY (id_modelo) REFERENCES modelos(id_modelo)
      ON DELETE RESTRICT ON UPDATE RESTRICT
);

CREATE TABLE vendas (
    id_venda SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_funcionario INT NOT NULL,
    id_veiculo INT NOT NULL UNIQUE,
    data_venda DATE NOT NULL DEFAULT CURRENT_DATE,
    valor_venda NUMERIC(10, 2) NOT NULL
      CHECK(valor_venda > 0),
    forma_pagamento VARCHAR(15) NOT NULL
      CHECK(forma_pagamento IN ('dinheiro', 'pix', 'cartao', 'financiamento')),

    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
      ON DELETE RESTRICT ON UPDATE RESTRICT,
    FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id_funcionario)
      ON DELETE RESTRICT ON UPDATE RESTRICT,
    FOREIGN KEY (id_veiculo) REFERENCES veiculos(id_veiculo)
      ON DELETE RESTRICT ON UPDATE RESTRICT
);
