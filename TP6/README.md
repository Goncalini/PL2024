# TPC6: Gramática Independente de Contexto
#### Autor: Gonçalo Daniel Machado Costa, A100824

## Resumo

Este trabalho consiste na implementação de uma gramática independente de contexto para representar expressões aritméticas e lógicas simples. A gramática é composta por terminais, não-terminais e regras de produção, que descrevem como as expressões podem ser formadas. 

### Exemplos

```
$ ?a
$ b=a*6/(4-1)
$ !a+b
$ c=(a*b)/(a+b)
```

## Resolução e Gramática

```
T = {'(', ')', '-', '+', '*', '/', '=', '?', '!', var, num}

N = {S, Expressão, Expressão2, Expressão3, Sinal, Sinal2}

S = S

P = {
    S -> '?' var                 LA = {'?'}
       | '!' Expressão           LA = {'!'}
       | var '=' Expressão       LA = {var}

    Expressão -> Expressão2 Sinal

    Sinal -> '+' Expressão          LA = {'+'}
        | '-' Expressão             LA = {'-'}
        | & (empty)                 LA = {$, ')'} 
    
    Expressão2 -> Expressão3 Sinal2      LA = {'(', var, num}

    Sinal2 -> '*' Expressão         LA = {'*'}
         | '/' Expressão            LA = {'/'}
         | &                        LA = {'+', '-', $, ')'}

    Expressão3 -> '(' Expressão ')'   LA = {'('}
           | var                      LA = {var}
           | num                      LA = {num}
}
```
