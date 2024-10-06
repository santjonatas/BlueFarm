from datetime import datetime 
from typing import Optional 

class CreateProdutoItemInputDto: 
    def __init__(self, 
        nome: Optional[str] = None, 
        descricao: Optional[str] = None, 
        preco: Optional[str] = None, 
        nome_insumo: Optional[str] = None, 
        descricao_insumo: Optional[str] = None, 
        preco_insumo: Optional[str] = None, 
        comprado_em: Optional[str] = None, 
        quantidade_disponivel_insumo: Optional[int] = None, 
        quantidade_disponivel: Optional[int] = None, 
        ultima_atualizacao: Optional[datetime] = None, 
        ) -> None: 
        
        # Atributos de CreateProdutoInputDto 
        self.nome = nome 
        self.descricao = descricao 
        self.preco = preco 
        
        # Atributos de CreateInsumoInputDto 
        self.nome_insumo = nome_insumo 
        self.descricao_insumo = descricao_insumo 
        self.preco_insumo = preco_insumo 
        self.comprado_em = comprado_em 
        self.quantidade_disponivel_insumo = quantidade_disponivel_insumo
        
        # Atributos de CreateEstoqueInputDto 
        self.quantidade_disponivel = quantidade_disponivel 
        self.ultima_atualizacao = ultima_atualizacao