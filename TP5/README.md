# Titulo

TPC 4 - Analisador Léxico para Querie

# Autor

Gonçalo Daniel Machado Costa, A100824


# Explicação

Foram criados vários tokens para cada operação possível na máquina de vendas:

1. `LISTAR`
2. `MOEDA`
3. `SELECIONAR`
3. `ADICIONAR`
4. `SAIR`
5. `Saldo`

Cada token tem associado uma expressão regular associada permitindo identificar e classificar corretamente as entradas do utilizador.

O programa carrega os dados a partir de um ficheiro JSON do seguinte formato: ID do produto, nome, quantidade e preço.

# Utilização da Vending Machine

- **LISTAR:** Exibe todos os produtos em stock atual na máquina de vendas.
- **MOEDA:** Adiciona saldo à máquina, separando por `,` as várias moedas que se quer introduzir.
  - Exemplo: Moedas 1e,50c
- **SELECIONAR:** Seleciona um produto à escolha para compra.
  - Exemplo: Selecionar 1
- **ADICIONAR:** Adiciona produtos ao stock da máquina. (Caso o produto não exista é necessário indicar o preço do mesmo)
  - Exemplo: Adicionar Compal 10 0.9
- **Saldo:** Exibe o saldo atual disponivel.
- **SAIR:** Sair da Vending Machine e recebe o devido troco.


# Execução do programa


Execute o programa a partir do terminal ou prompt de comando, fornecendo o arquivo JSON como argumento.

```
python3 vending_machine.py stock.json
```

# Recursos

[Documentação Ply](https://www.dabeaz.com/ply/ply.html)
