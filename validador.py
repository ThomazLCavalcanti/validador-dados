# Importações principais do Pydantic para validação de dados e tipos úteis
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import date
import re

# Modelo de dados que representa um usuário e faz validações automáticas
class Usuario(BaseModel):
    nome: str                      # Nome completo (deve conter nome e sobrenome)
    email: EmailStr                # E-mail validado (usa padrão de e-mail real)
    idade: int                     # Idade, será validada para estar entre 0 e 120
    cpf: str                       # CPF no formato numérico com 11 dígitos
    data_nascimento: Optional[date] = None  # Data de nascimento opcional

    # Validador: verifica se o nome contém ao menos um espaço (nome e sobrenome)
    @field_validator('nome')
    def nome_deve_ter_espaco(cls, v):
        if " " not in v.strip():
            raise ValueError('O nome deve conter nome e sobrenome')
        return v

    # Validador: restringe a idade para o intervalo de 0 a 120
    @field_validator('idade')
    def idade_valida(cls, v):
        if v < 0 or v > 120:
            raise ValueError('Idade inválida')
        return v

    # Validador: garante que o CPF tenha exatamente 11 dígitos numéricos
    @field_validator('cpf')
    def cpf_valido(cls, v):
        if not re.fullmatch(r'\d{11}', v):
            raise ValueError('CPF deve conter 11 dígitos numéricos')
        return v

# Função principal que instancia o modelo e imprime os dados validados
def main():
    try:
        # Criação de um usuário com dados válidos
        usuario = Usuario(
            nome="Maria Silva",
            email="maria@example.com",
            idade=30,
            cpf="12345678901",
            data_nascimento="1995-04-01"  # Aceita string no formato ISO
        )
        print("✅ Dados validados com sucesso!")

        # Exibe os dados validados em formato JSON formatado (Pydantic v2)
        print(usuario.model_dump_json(indent=4))
    except Exception as e:
        # Em caso de falha de validação, exibe o erro
        print("❌ Erro de validação:", e)

# Executa o código somente se o script for chamado diretamente
if __name__ == "__main__":
    main()
