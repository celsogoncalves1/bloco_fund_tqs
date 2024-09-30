
from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "Gemini"
    produto2 = "Llama"
    produto3 = "Gpt4"

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

  