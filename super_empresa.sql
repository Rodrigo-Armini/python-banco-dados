drop database if exists super_empresa;
create database super_empresa;
use super_empresa;

create table produtos(
    id int primary key auto_increment,
    nome varchar(50)
);