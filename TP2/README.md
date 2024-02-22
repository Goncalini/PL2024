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

Foi utilizado essencialmente o método "sub" da libraria re, que recebe uma expressão regular, e ao analisar uma linha de código, retorna ao segundo argumento todos os matchs capturados\

Para listas foi tido em conta uma flag que imprimia <ol> quando a mesma tinha conhecimento de iniciar uma lista numerada e quando deteta que a mesma termina imprime </ol>


## Comentários adicionais

Foram feitas duas versões diferentes, uma que recebe uma expressão em markdown que o usuario deve dar input no terminal (MD_HTML_CoverterTerminal) e outra que recebe um ficheiro em markdown e passa o mesmo para HTML (MD_HTML_CoverterFile)



































Links uteis:
https://docs.python.org/pt-br/3/library/re.html
https://regex101.com








Criar em Python um pequeno conversor de MarkDown para HTML
Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
In: # Exemplo
Out: <h1>Exemplo</h1>
Bold: pedaços de texto entre "**":
In: Este é um **exemplo** ...
Out: Este é um <b>exemplo</b> ...
Itálico: pedaços de texto entre "*":
In: Este é um *exemplo* ...
Out: Este é um <i>exemplo</i> ...
Lista numerada:
In:
1. Primeiro item
2. Segundo item
3. Terceiro item
Out:
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
Link: [texto](endereço URL)
In: Como pode ser consultado em [página da UC](http://www.uc.pt)
Out: Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>
Imagem: ![texto alternativo](path para a imagem)
In: Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
Out: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...
