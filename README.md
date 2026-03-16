# Cadastro-de-insumos-BASF
Projeto focado em cadastro de insumos para a empresa BASF (resolvi fazer pois estou me candidatando para uma vaga de estágio).

 Sistema de Controle de Insumos

Este projeto é um pequeno sistema desenvolvido em **Python** para ajudar no controle de insumos de forma simples.
A ideia principal é permitir cadastrar materiais, visualizar o estoque atual e gerar um relatório com os itens registrados.

Ele utiliza **SQLite** como banco de dados, o que significa que não é necessário instalar um servidor de banco separado — o próprio sistema cria o arquivo de banco automaticamente.

## O que o sistema faz

O sistema funciona através de um **menu no terminal**, onde é possível escolher algumas opções:

1. **Cadastrar insumo**
   Permite registrar um novo item no estoque informando:

   * Nome
   * Tipo
   * Quantidade
   * Unidade de medida (kg, L, unidade, etc.)

2. Listar estoque
   Mostra todos os insumos cadastrados e suas respectivas quantidades.

3. Gerar relatório
   Exibe um relatório mais detalhado com as informações dos insumos cadastrados, incluindo a data de registro.

4. Sair do sistema

## Tecnologias utilizadas

* **Python**
* **SQLite**
* Biblioteca `datetime` para registrar a data de cadastro
* Estrutura modular com arquivos separados para organização do código

## Estrutura do projeto

O projeto está dividido em alguns arquivos para deixar o código mais organizado:

```
projeto_controle_insumos/

main.py
database.py
relatorios.py
estoque.db
```

**main.py**
Arquivo principal que executa o sistema e apresenta o menu.

**database.py**
Responsável por criar o banco de dados e realizar operações como inserir e listar insumos.

**relatorios.py**
Responsável por gerar o relatório de estoque com base nos dados cadastrados.

**estoque.db**
Arquivo do banco de dados SQLite que armazena os insumos.

## Como executar o projeto

1. Certifique-se de ter o **Python instalado**.
2. Baixe ou clone este repositório.
3. Execute o arquivo principal:

```
```

Ao executar, o sistema criará automaticamente o banco de dados caso ele ainda não exista.

## Objetivo do projeto

Este projeto foi desenvolvido como forma de **praticar conceitos de programação em Python**, incluindo:

* Organização de código em múltiplos arquivos
* Manipulação de banco de dados com SQLite
* Estrutura de menus no terminal
* Funções e modularização

Apesar de ser um sistema simples, ele representa a base para aplicações maiores de controle de estoque.

## Possíveis melhorias futuras

Algumas ideias que podem ser adicionadas no futuro:

* Interface gráfica
* Exportação de relatórios em PDF ou Excel
* Controle de entrada e saída de estoque
* Sistema de login
* Dashboard com estatísticas do estoque

---

Projeto desenvolvido para fins de estudo e prática em programação.
