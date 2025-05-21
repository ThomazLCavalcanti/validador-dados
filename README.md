# Validador de Dados com Pydantic

Este projeto utiliza a biblioteca **Pydantic** para validar dados de entrada, como nome, e-mail, idade e CPF, garantindo que estão no formato correto.

## Funcionalidades

- Verificação de nome completo
- Validação de e-mail
- Faixa de idade permitida
- Validação de formato de CPF (11 dígitos)
- Validação opcional da data de nascimento

## Requisitos

Instale as dependências com:

```
pip install -r requirements.txt
```

## Como executar

Ative seu ambiente virtual (opcional) e execute:

```
python validador.py
```

## Exemplo de Entrada

```python
usuario = Usuario(
    nome="Maria Silva",
    email="maria@example.com",
    idade=30,
    cpf="12345678901",
    data_nascimento="1995-04-01"
)
```

## Licença

Este projeto está sob a licença MIT.

## 🤝 Contato
Feito por Thomaz — entre em contato pelo GitHub: [@ThomazLCavalcanti](https://github.com/ThomazLCavalcanti/)
