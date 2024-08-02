from dataclasses import dataclass
from categoria import Categoria

@dataclass
class Transacao:
    descricao: str
    valor: float
    categoria: Categoria

    def __str__(self):
        return f"Descrição: {self.descricao} | Valor: {self.valor} | Categoria: {self.categoria.nome}"