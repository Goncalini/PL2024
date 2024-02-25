# Titulo

TPC 3 de PL - Somador on/off

# Autor

Gonçalo Daniel Machado Costa, A100824


# Explicação

Com o recurso da libraria 're' (regex) foi iterado ao longo do ficheiro linha a linha uma expressão regular que capturava e por sua vez armazenava cada ocorrencia de 'on', 'off', '=' e um digito numa lista de listas, essa mesma lista foi tranformada em uma lista com todos os elementos das sublistas e a mesma foi percorrida.\
A cada ocorrência de um 'on', uma flag auxiliar é ativade, e a mesma é desativada quando ocorre um 'off'.\
Quando a flag está ativada cada digito encontrado é adicionado ao somatório atual.\
A cada ocorrência de um '=' o somatório atual é imprimido.





































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
