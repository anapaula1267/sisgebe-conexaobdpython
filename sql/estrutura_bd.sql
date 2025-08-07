-- Criação do banco de dados paragerenciar uma biblioteca escolar - SGB
CREATE DATABASE IF NOT EXISTS SGB;
USE SGB;

-- Tabela Categoria
CREATE TABLE Categoria (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    descricao TEXT
):

-- Tabela Livro
CREATE TABLE Livro(
    id int PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    sinopse TEXT,
    capa TEXT,
    quantidade INT DEFAULT 1,
    Categoria_id INT,
    FOREING KEY(Categoria_id) REFERENCES Categoria(id)
);

-- Tabela Aluno
CREATE TABLE Aluno(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    serio VARCHAR(20) NOT NULL,
    satus ENUM('ativo', 'bloqueado') DEFAULT 'ativo'
);

-- Tabela Professor
CREATE TABLE Professor(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    disciplina VARCHAR(50),
    satus ENUM('ativo', 'inativo') DEFAULT 'ativo'
);

--Tabela BIbliotecario
CREATE TABLE BIbliotecario(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    satus ENUM('ativo', 'inativo') DEFAULT 'ativo'
);

--Tabela Diretor
CREATE TABLE Diretor(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    satus ENUM('ativo', 'inativo') DEFAULT 'ativo'
);

--Tabela Supervisor
CREATE TABLE Supervisor(
    id INT PRIMARY KEY AUTO_INCREMENT,
    aluno_id INT,
    Livro_id INT
    data_emprestimo DATE NOT NULL,
    data_devolucao_prevista DATE,
    data_devolucao_real DATE,
);