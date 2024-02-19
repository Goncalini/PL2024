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
