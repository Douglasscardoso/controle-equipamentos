# Controle de Equipamentos

Sistema em Python, executado no terminal, para controlar o empréstimo de equipamentos (ferramentas, notebooks, etc.): cadastro, saldo disponível, empréstimos e devoluções.

Projeto de estudo de **Programação Orientada a Objetos** — classes com responsabilidades separadas, validação de regras de negócio e testes automatizados. Usa apenas a biblioteca padrão do Python (3.9+), sem dependências.

## Funcionalidades

- Cadastrar equipamentos com código, nome e quantidade total
- Registrar empréstimo para uma pessoa, baixando o saldo disponível
- Registrar devolução, repondo o saldo
- Listar equipamentos (com saldo) e empréstimos em aberto
- Validações: quantidade inválida ou maior que a disponível, código duplicado, equipamento inexistente, devolução repetida

## Como executar

```bash
python -m controle_equipamentos
```

## Como rodar os testes

```bash
python -m unittest
```

## Estrutura

```
controle_equipamentos/
├── equipamento.py   # Equipamento: saldo, emprestar() e devolver()
├── emprestimo.py    # Emprestimo: quem pegou, quanto, quando e se foi devolvido
├── controle.py      # ControleEquipamentos: cadastro e regras de empréstimo/devolução
├── cli.py           # Menu interativo no terminal
└── __main__.py      # Ponto de entrada (python -m controle_equipamentos)
tests/               # Testes unitários (unittest)
```

A lógica de negócio (`equipamento`, `emprestimo`, `controle`) não depende do terminal: toda a interação com o usuário fica em `cli.py`, o que facilita testar e, no futuro, trocar a interface.

## Próximos passos

- Persistir os dados em arquivo (JSON) ou banco SQLite
- Data prevista de devolução e alerta de atraso
- Interface web (Flask/FastAPI)
