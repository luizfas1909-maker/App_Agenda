# App Agenda (Desktop + PostgreSQL)

Aplicativo desktop para gerenciamento de compromissos, desenvolvido em Python com interface grafica em Tkinter e persistencia em PostgreSQL.

## Visao Geral

O projeto permite cadastrar, listar, atualizar e remover compromissos com:

- `nome` do compromisso
- `descricao` livre
- `data_limite` no formato `AAAA-MM-DD`

A interface e desktop (janela grafica), entao nao e necessario usar menus no terminal para operar o sistema.

## Funcionalidades

- Cadastro de compromissos
- Listagem em tabela (Treeview)
- Edicao de compromisso selecionado
- Remocao com confirmacao
- Validacao de campos obrigatorios
- Validacao de data no formato ISO (`AAAA-MM-DD`)
- Criacao automatica da tabela no banco (`CREATE TABLE IF NOT EXISTS`)
- Reorganizacao de IDs apos remocao (IDs sequenciais sem lacunas)

## Tecnologias Utilizadas

- Python 3.11+
- Tkinter (GUI nativa do Python)
- psycopg2 (conexao com PostgreSQL)
- PostgreSQL

## Estrutura do Projeto

Arquivos principais:

- `main.py`: ponto de entrada da aplicacao
- `agenda_gui.py`: interface grafica e interacoes de tela
- `agenda_db.py`: acesso ao banco e operacoes CRUD

> O fluxo atual recomendado usa `main.py` + `agenda_gui.py` + `agenda_db.py`.

## Pre-requisitos

Antes de rodar, garanta:

1. Python instalado (recomendado 3.11 ou superior)
2. PostgreSQL instalado e rodando
3. Banco de dados `agendador` criado
4. Usuario/senha do banco configurados conforme o arquivo `agenda_db.py`

Configuracao atual no projeto:

- host: `localhost`
- port: `5432`
- database: `agendador`
- user: `postgres`
- password: `123456`

## Instalacao e Execucao

### 1) Clonar o repositorio

```bash
git clone <URL_DO_REPOSITORIO>
cd app_agenda
```

### 2) Criar e ativar ambiente virtual (opcional, recomendado)

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3) Instalar dependencia

```bash
pip install psycopg2
```

Se preferir a versao binaria:

```bash
pip install psycopg2-binary
```

### 4) Criar banco no PostgreSQL (se ainda nao existir)

No `psql`:

```sql
CREATE DATABASE agendador;
```

Nao precisa criar a tabela manualmente: o projeto cria automaticamente ao iniciar.

### 5) Executar aplicacao

```bash
python main.py
```

## Como Usar (Passo a Passo)

1. Abra o app com `python main.py`.
2. Preencha:
   - Nome
   - Descricao
   - Data limite no formato `AAAA-MM-DD` (ex.: `2026-05-01`)
3. Clique em `Adicionar`.
4. Para editar:
   - selecione uma linha na tabela
   - altere os campos
   - clique em `Atualizar`
5. Para remover:
   - selecione uma linha
   - clique em `Remover`
   - confirme na janela
6. Use `Recarregar` para atualizar a lista manualmente.
7. Use `Limpar selecao` para resetar o formulario.

## Modelo de Dados

Tabela `compromissos`:

- `id` `SERIAL PRIMARY KEY`
- `nome` `VARCHAR(150) NOT NULL`
- `descricao` `TEXT`
- `data_limite` `DATE NOT NULL`

## Reorganizacao de IDs

Apos remocao de um compromisso, o sistema:

1. renumera os IDs existentes para manter sequencia continua (`1, 2, 3...`)
2. ajusta a sequence do PostgreSQL para o proximo insert

Isso e util para apps pequenos e didaticos. Em sistemas com relacoes entre tabelas (chaves estrangeiras), essa pratica geralmente nao e recomendada.

## Solucao de Problemas

### Erro de conexao no banco

Revise host, porta, usuario, senha e nome do banco em `agenda_db.py`.

### Erro `UndefinedTable: relacao "compromissos" nao existe`

Execute o app via `python main.py` para disparar a criacao automatica da tabela.

### Data invalida

Use sempre `AAAA-MM-DD`, por exemplo: `2026-12-31`.

### Dependencia `psycopg2` falhando no Windows

Tente:

```bash
pip install psycopg2-binary
```

## Melhorias Futuras (Sugestoes)

- Busca/filtro por nome e data
- Ordenacao clicavel na tabela
- Exportacao para CSV
- Notificacoes de compromissos proximos
- Empacotamento em `.exe` com PyInstaller

## Licenca

Defina a licenca desejada para o projeto (ex.: MIT).
