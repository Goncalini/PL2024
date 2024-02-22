# Titulo

TPC 2 de PL - Conversor de MD para HTML

# Autor

Gonçalo Daniel Machado Costa, A100824


# Explicação

Com o recurso da libraria 're' (regex) e através de expressões regulares foi implementado um conversor de markdown para html para:
- Cabeçalhos
- Palvras/Expressões em italico
- Palvras/Expressões em negrito
- Listas Numeradas
- Imagens
- Links

Foi utilizado essencialmente o método "sub" da libraria re, que recebe uma expressão regular, e ao analisar uma linha de código, retorna ao segundo argumento todos os matchs capturados

Para listas foi tido em conta uma flag que imprimia \<ol> quando a mesma tinha conhecimento de iniciar uma lista numerada e quando deteta que a mesma termina imprime \</ol>


## Comentários adicionais

Foram feitas duas versões diferentes, uma que recebe uma expressão em markdown que o usuario deve dar input no terminal (MD_HTML_CoverterTerminal) e outra que recebe um ficheiro em markdown e passa o mesmo para HTML (MD_HTML_CoverterFile)

Links uteis:
https://docs.python.org/pt-br/3/library/re.html
https://regex101.com



