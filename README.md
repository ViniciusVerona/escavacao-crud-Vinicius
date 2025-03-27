# escavacao-crud-vinicius

CRUD em Python para catalogação e registro de escavações relacionadas a antigas comunidades indígenas da Amazônia.

## 📌 Funcionalidades

- ✅ Cadastrar novos pontos de escavação
- ✅ Listar pontos salvos
- ✅ Atualizar informações de um ponto existente
- ✅ Remover registros inválidos
- ✅ Persistência via SQLite
- ✅ Validação com Pydantic
- ✅ Terminal interativo

## 📁 Estrutura

- `main.py` – Menu principal (linha de comando)
- `crud.py` – Funções de criação, leitura, atualização e remoção
- `models.py` – Modelo ORM da tabela
- `schemas.py` – Pydantic para validação
- `database.py` – Conexão e criação do banco
- `sample_data.json` – Exemplo de dados para teste
- `test_insert_json.py` – Script para popular dados via JSON
- `requirements.txt` – Dependências do projeto

## 🚀 Como rodar

1. Clone o repositório:

```bash
git clone https://github.com/viniciusverona/escavacao-crud-vinicius.git
cd escavacao-crud-vinicius

