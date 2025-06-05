# auth-flask
API em Flask para gerenciamento de usuários e autenticação

## Descrição

Este projeto é uma API RESTful construída com Flask para gerenciamento de usuários e autenticação. Ele fornece endpoints para registro de usuários, login, e gerenciamento de perfis de usuário.

## Tecnologias Utilizadas

- Python 3.13+
- Flask 3.1.1
- Flask-SQLAlchemy 3.1.1
- Flask-Login 0.6.3
- Flask-Migrate 4.1.0
- Bcrypt 4.3.0
- SQLite (padrão) / Banco de dados configurável
- Python-dotenv 1.1.0

## Estrutura do Projeto

.
├── app.py
├── infrastructure
│   ├── __init__.py
│   ├── config.py
│   └── database.py
├── init_db.py
├── instance
│   └── database.db
├── models
│   ├── __init__.py
│   └── user.py
├── routes
│   ├── __init__.py
│   ├── register.py
│   ├── auth
│   │   ├── __init__.py
│   │   └── routes.py
│   └── user
│       ├── __init__.py
│       └── routes.py
├── pyproject.toml
├── README.md
├── uv.lock

## Instalação

### Pré-requisitos

- Python 3.13 ou superior
- uv

### Configuração do Ambiente

1. Clone o repositório:

   ```bash
   git clone https://github.com/fonsecach/auth-flask.git
   cd auth-flask
   ```

2. Instale as dependências

   ```bash
   uv sync --no-cache
   ```

3. Atualize o .env

   ```text
   DATABASE_URL=""
   ```

4. Inicie o banco de dados

   ```bash
   uv run init_db.py
   ```

### Executando a aplicacao

   ```bash
   uv run app.py
   ```
