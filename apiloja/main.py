from fastapi import FastAPI, Form, HTTPException

app = FastAPI()

# Armazenamento em memória para produtos
produtos = []

@app.get("/")
async def home():
    return {"message": "Bem-vindo à API de Produtos!"}

@app.get("/produtos")
async def listar_produtos():
    """
    Recuperar a lista de produtos.
    """
    return {
        "status": "sucesso",
        "mensagem": "Produtos recuperados com sucesso.",
        "dados": produtos
    }

@app.get("/produtos/{produto_id}")
async def obter_produto_por_id(produto_id: int):
    """
    Recuperar um produto pelo seu ID.
    """
    for produto in produtos:
        if produto["id"] == produto_id:
            return {
                "status": "sucesso",
                "mensagem": "Produto recuperado com sucesso.",
                "dados": produto
            }
    raise HTTPException(status_code=404, detail="Produto não encontrado.")

@app.get("/produtos_busca")
async def buscar_produtos_por_nome(nome: str):
    """
    Buscar produtos pelo nome.
    """
    produtos_correspondentes = [produto for produto in produtos if nome.lower() in produto["nome"].lower()]
    if produtos_correspondentes:
        return {
            "status": "sucesso",
            "mensagem": "Produtos recuperados com sucesso.",
            "dados": produtos_correspondentes
        }
    raise HTTPException(status_code=404, detail="Nenhum produto encontrado com o nome informado.")

@app.post("/produtos")
async def criar_produto(
    nome: str = Form(...),
    descricao: str = Form(...),
    preco: float = Form(...),
    tamanho: str = Form(...)
):
    """
    Adicionar um novo produto à lista.
    """
    if not nome or not descricao or preco <= 0 or not tamanho:
        raise HTTPException(status_code=422, detail="Todos os campos são obrigatórios e preço deve ser positivo.")

    produto = {
        "id": len(produtos) + 1,  # Gerar um ID simples
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
        "tamanho": tamanho
    }
    produtos.append(produto)
    return {
        "status": "sucesso",
        "mensagem": "Produto adicionado com sucesso.",
        "dados": produto
    }
