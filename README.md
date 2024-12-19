
# API de Gestão de Produtos 🛒

Este é um projeto FastAPI simples para gerenciar uma lista de produtos em uma loja. Ele fornece funcionalidades básicas de CRUD e recursos de pesquisa, sendo um excelente ponto de partida para aprender a usar o FastAPI.

## Características ✨
- 📋 Liste todos os produtos.
- 🔍 Recuperar um produto pelo ID.
- 📝 Pesquise produtos pelo nome.
- ➕ Adicione um novo produto.

## Pontos finais 🌐

### 1. Listar todos os produtos 📋
**GET** `/produtos`

Recupere a lista de todos os produtos.

**Resposta:**

```json
{
  "status": "sucesso",
  "mensagem": "Produtos recuperados com sucesso.",
  "dados": [...]
}
```

### 2. Recuperar produto por ID 🔍
**GET** `/produtos/{produto_id}`

Recupere os detalhes de um produto usando seu ID exclusivo.

**Resposta (se encontrado):**

```json
{
  "status": "sucesso",
  "mensagem": "Produto recuperado com sucesso.",
  "dados": {...}
}
```

### 3. Pesquisar produtos por nome 🔎
**GET** `/produtos_busca?nome={nome}`

Pesquise produtos cujo nome contenha a sequência fornecida (sem distinção entre maiúsculas e minúsculas).

**Resposta:**

```json
{
  "status": "sucesso",
  "mensagem": "Produtos recuperados com sucesso.",
  "dados": [...]
}
```

### 4. Adicionar um novo produto ➕
**POST** `/produtos`

Dados do formulário:
- `nome` (string, obrigatório)
- `descricao` (string, obrigatório)
- `preco` (float, obrigatório)
- `tamanho` (string, obrigatório)

**Resposta:**

```json
{
  "status": "sucesso",
  "mensagem": "Produto adicionado com sucesso.",
  "dados": {...}
}
```


## Como configurar e executar 🚀

### Pré-requisitos
- 🐍 Python 3.9 ou superior instalado.
- 📦 Dependências necessárias (FastAPI, Uvicorn, etc.)

### Passos
1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-repositorio-url.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual e ative-o (opcional):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use venv\Scripts\activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Inicie o servidor de desenvolvimento:

    ```bash
    uvicorn main:app --reload
    ```

5. Abra seu navegador e navegue até:

    - Documentação da API: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 📄
    - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) 📚

## Comandos do ambiente Conda ⚙️

Aqui estão alguns comandos úteis para gerenciar seus ambientes Conda:

- 🌱 Ver ambientes criados:

    ```bash
    conda info --envs
    ```

- ❌ Remover um ambiente:

    ```bash
    conda env remove --name nome_do_ambiente
    ```

- 🆕 Criar um novo ambiente:

    ```bash
    conda create --name nome_do_ambiente python=3.10
    ```

- 🔄 Ativar um ambiente:

    ```bash
    conda activate nome_do_ambiente
    ```

- 🚪 Desativar um ambiente:

    ```bash
    conda deactivate
    ```

---

### Contribuição 🤝

Se você tiver sugestões ou melhorias para este projeto, fique à vontade para abrir uma *issue* ou enviar um *pull request*! 

