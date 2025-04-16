from fastapi import FastAPI, Query
from pydentic import Basemodel
from typing import List, Optional
import pandas as pd

app = FastAPI(title="Api de dados de vendas")


df = pd.DataFrame({
    "id": range(1,12),
    "produto": ['Macbook', 'Iphone', 'Monitor', 'Teclado', 'Mouse', 'CPU',
                'Impressora','MousePad', 'SSD', 'RAM', 'WebCam', 'Microfone'                 
                ],
    "categoria": ['informática'],
    "preco":    [18000, 8000, 600, 120, 79.90, 900, 350, 39.90, 220, 139, 99, 199],
    "quantidade": [4, 20, 7, 8, 14, 3, 1, 40, 30, 15, 5, 9]
    
})

class Produto(Basemodel):
    id: int
    produto: str
    categoria: str
    preco: float
    quantidade_vendida: int
    
class ProductCreate(Basemodel):
    produto: str
    categoria: str
    preco: float
    quantidade_vendida: int
    
@app.get("/")
def read_root():
    return {"mensagem": "Api de Dados de Vendas"}

@app.get("/produtos", response_model=List[Produto])
def get_produtos(
    categoria: Optional[str]= Query(None, descriptio="Filtrar por categoria"),
    min_preco: Optional[float]= Query(None, description="Preço mínimo"),
    max_preco: Optional[float]= Query(None, description="Preço máximo")
):
    df = df.copy()
    
    if categoria:
        df = df[df["categoria"] == categoria]
        
    if min_preco is not None:
        df = df[df['preco']>= min_preco]
        
    if max_preco is not None:
        df = df[df['preco'] <= max_preco]
        
    return df.to_dict(orient='records')

@app.get("/produtos/{produto_id}", response_model=Produto)
def getproduto(produto_id: int):
    produto = df[df["id"] == produto_id]
    if not produto.empty:
        return produto.iloc[0].to_dict()
    return
