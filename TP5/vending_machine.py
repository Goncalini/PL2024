from ply import lex, yacc
import sys
import json


tokens = [
    "SELECIONAR",  
    "ADICIONAR",
    "MOEDA",
    "SAIR",
    "LISTAR",
    "SALDO",
]

def t_SELECIONAR(t):
    r"(selecionar|SELECIONAR|Selecionar)[ ]\d+"
    return t

def t_ADICIONAR(t):
    r"(adicionar|ADICIONAR|Adicionar)[ ][\w-]+[ ]\d([ ]\d+(\.\d+)?)?" #adicionar [produto] [quantidade] [valor]
    return t

def t_MOEDA(t):
    r"(moeda|Moeda|MOEDA)[ ]([2e|1e|5c|10c|20c|50c],?)+"
    return t

def t_SAIR(t):
    r"sair|SAIR|Sair"
    return t

def t_LISTAR(t):
    r"listar|LISTAR|Listar"
    return t

def t_SALDO(t):
    r"saldo|SALDO|Saldo"
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def calctroco(saldo):
    troco = {}
    values = [2, 1, 0.5, 0.2, 0.1, 0.05]
    for value in values:
        troco[value] = int(saldo // value)
        saldo = round(saldo % value, 2)
    return troco


def main(argv):
    if (len(argv) < 2):
        print("Stock File is missing")
        return

    input_file = argv[1]
    with open(input_file, "r") as file:
        data = json.load(file)
    
    produtos = data["stock"]
    itens = {}
    for produto in produtos:
        itens[produto["id"]] = produto

    lexer = lex.lex()

    saldo = 0
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")
    for line in sys.stdin:
        lexer.input(line)
        for token in lexer:
            if not token: print("maq: Comando inválido")
            if token.type == "LISTAR":
                print ("maq:\n")
                print('     Número     |            Nome                             |      Preço      |   Quantidade')
                for produto in produtos:
                    print(f'       {produto["id"]}        |        {produto["nome"]: <30}       |       {produto["preco"]}       |       {produto["quantidade"]}')
            elif token.type == "MOEDA":
                moedas = token.value.split(" ")[1].split(",")
                for moeda in moedas:
                    if moeda[-1] == "e":
                        saldo += float(moeda[:-1])
                    else:
                        saldo += round(float(moeda[:-1]) / 100,2)
                print(f"maq: Saldo Disponivel = {saldo}€")
            
            elif token.type == "SAIR":
                print(f"maq: Troco = {round(saldo,2)}")
                troco = calctroco(saldo)
                for value in troco:
                    if troco[value] > 0:
                        print(f"Recebeu {troco[value]} moeda(s) de {value}€:")
                return
            
            elif token.type == "SELECIONAR":
                id = int(token.value.split(" ")[1])
                if id in itens:
                    if itens[id]["quantidade"] > 0:    
                        produto = itens[id]
                        if saldo >= produto["preco"]:
                            saldo -= produto["preco"]
                            itens[id]["quantidade"] -= 1
                            print(f"maq: Produto {produto['nome']} comprado com sucesso")
                        else:
                            print(f"maq: Saldo insufuciente para satisfazer o seu pedido\nmaq: Saldo Disponivel = {saldo}€; Pedido = {produto['preco']}€")
                    else :
                        print(f"maq: O Produto {id} está esgotado")
                else:
                    print(f"maq: O Produto {id} não existe")

            elif token.type == "SALDO":
                print(f"maq: Saldo Disponivel = {round(saldo,2)}€")

            elif token.type == "ADICIONAR":
                nome = token.value.split(" ")[1]
                quantidade = int(token.value.split(" ")[2])
                for produto in produtos:
                    if produto["nome"] == nome:
                        produto["quantidade"] += quantidade
                        break
                else:
                    if len(token.value.split(" ")) == 4:
                        preco = float(token.value.split(" ")[3])
                        produtos.append({"id": len(produtos)+1, "nome": nome, "preco": preco, "quantidade": quantidade})
                    else:
                        print(f"maq: O preço do produto está em falta")
                print(f"maq: Adicionado {quantidade} itens ao produto {nome}")

if __name__ == "__main__":
    main(sys.argv)