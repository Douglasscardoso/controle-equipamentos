# Controle de Equipamentos

Sistema em Python, executado no terminal, para controlar o empréstimo de equipamentos (ferramentas, notebooks, etc.): cadastro, saldo disponível, empréstimos e devoluções.

Projeto de estudo de **Programação Orientada a Objetos**, com classes de responsabilidades separadas, validação de regras de negócio e testes automatizados. Usa apenas a biblioteca padrão do Python (3.9+), sem dependências.

## Funcionalidades

- Cadastrar equipamentos com código, nome e quantidade total
- Registrar empréstimo para uma pessoa, baixando o saldo disponível
- Registrar devolução, repondo o saldo
- Listar equipamentos (com saldo) e empréstimos em aberto
- Validações: quantidade inválida ou maior que a disponível, código duplicado, equipamento inexistente e devolução repetida

## Como executar

```bash
git clone https://github.com/Douglasscardoso/controle-equipamentos.git
cd controle-equipamentos
python -m controle_equipamentos
```

## Exemplo de uso

```
=== Controle de Equipamentos ===
1 - Cadastrar equipamento
2 - Listar equipamentos
3 - Registrar empréstimo
4 - Registrar devolução
5 - Listar empréstimos em aberto
0 - Sair

Escolha uma opção: 3
Pessoa: Douglas
Código do equipamento: 001
Quantidade: 2
Registrado: #1 Douglas - 2x furadeira (17/10/2026 18:40, em aberto)

Escolha uma opção: 2
[001] furadeira - 3/5 disponíveis

Escolha uma opção: 4
Número do empréstimo: 1
Devolvido: #1 Douglas - 2x furadeira (17/10/2026 18:40, devolvido)

Escolha uma opção: 3
Pessoa: Ana
Código do equipamento: 001
Quantidade: 9
Erro: quantidade maior que a disponível
```

O programa já inicia com uma furadeira (código `001`, 5 unidades) cadastrada para facilitar o teste.

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

## Autor

**Douglas Cardoso**  
GitHub: [@Douglasscardoso](https://github.com/Douglasscardoso)  
LinkedIn: [Douglas Cardoso](www.linkedin.com/in/douglas-cardoso1)
