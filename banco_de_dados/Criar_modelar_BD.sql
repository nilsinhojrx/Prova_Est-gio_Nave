/* Criar banco de dados Navers */
create database Navers;
use Navers;

/* Criar a tabela navers */
create table navers(
id int NOT NULL AUTO_INCREMENT,
Nome varchar(255) NOT NULL,
Cargo varchar(255) NOT NULL,
Data_nascimento datetime,
Admissão datetime,
criação timestamp,
atualização timestamp,
PRIMARY KEY (id)
);

/* Criando a tabela projects */
create table projects(
id int NOT NULL AUTO_INCREMENT, /* coluna id */
Nome varchar(255) NOT NULL,
criação timestamp,
atualização timestamp,
PRIMARY KEY (id)
);

/* Criando a tabela que relaciona projetos e navers */
create table projects_navers(
id int not null  AUTO_INCREMENT,
PRIMARY KEY(id)
);

/* Estabelecendo a relação */

/* adicionando a coluna project_id */
alter table projects_navers add project_id int;
 
 /* colocando project_id como chave estrangeira */
alter table projects_navers
add foreign key(project_id)
references projects(id);

/* adicionando a coluna navers_id */
alter table projects_navers add navers_id int;

/* colocando navers_id como chave estrageira */
alter table projects_navers
add foreign key(navers_id)
references navers(id);

