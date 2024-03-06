from ply import lex, yacc
import sys


reserved = {
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE'
}

tokens = [
    "COMANDO",  
    "OPERADOR",
    "ATRIBUTO",
    "DELIMITADOR",
    "NUMERO",
    "FINAL_DELIMITADOR"
] + list(reserved.values())

t_OPERADOR = r'>='

t_DELIMITADOR = r','

t_NUMERO = r'\d+'

t_FINAL_DELIMITADOR = r';'


def t_COMANDO(t):
    r"\b[a-zA-Z]+\b"
    if reserved.get(t.value.lower()):
        t.type = "COMANDO"
    else:
        t.type = "ATRIBUTO"
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def main (args):
    if len(args) < 2:
        return
    with open(args[1], 'r') as file:
        data = file.read()
        lexer = lex.lex() 
        lexer.input(data)
        for tok in lexer:
            print(tok) 

if __name__ == '__main__':
    main(args=sys.argv)