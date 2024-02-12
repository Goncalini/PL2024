# Titulo

TPC 1 de PL - Analise um Dataset

# Autor

Gonçalo Daniel Machado Costa, A100824

# Enúnciado

Proibido usar o módulo CSV;
Ler o dataset, processá-lo e criar os seguintes resultados:
    Lista ordenada alfabeticamente das modalidades desportivas;
    Percentagens de atletas aptos e inaptos para a prática desportiva;
    Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...

# Explicação

-->Em prol de de ler um ficheiro csv sem o uso do módulo CSV, foi usado a função open no modo de read 'open(arquivo, 'r')'
-->Após isso foram inicializadas uma lista de modalidades, variaveis auxiliares para o calculo de atletas aptos e inaptos e um dicionário para a distribuição, cuja estrutura será chave -> (idade // 5)*5: Esta parte da expressão calcula o quociente da divisão inteira entre a idade e 5. Isso significa que dividimos a idade por 5 e ignoramos qualquer parte fracionária, obtendo assim um número inteiro que representa a "faixa" de idade, e depois multiplicamos esse quociente por 5 para agrupar as idades em intervalos de 5 anos. A mesma chave esta ligada a um tuplo que representa (número total de pessoas nessa faixa etária, lista de nomes dos atletas nessa faixa etária).

## Para responder às questões do enunciado forem implementadas as seguintes estratégias
Lista ordenada alfabeticamente das modalidades desportivas:
-->A cada linha analisada, após a mesma ser parseada "row = line.rstrip().split(',')", é dividida em substrings armazenadas em "row", que possibilita a seleção de uma substring em especifico, como a modalidade, e a mesma é armazenada na lista auxiliar "modalidades". Utilizando a função sorted de python,com um set, é possivel eliminar modalidades repetidas e ordenar las por ordem alfabética.

Percentagens de atletas aptos e inaptos para a prática desportiva:
-->A cada linha parseada é verificado se o ultimo atributo é true ou false, e a partir disso o valor das variaveis auxiliar enable e able são aincrementadas e calculadas atravez de "(able / total) * 100" e "(enable / total) * 100"

 Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...:
 -->A medida que cada linha é analisada e parseada, os devidos valores são armazenados no dicionario "destribuicao", cuja estrutura foi explicada em cima, os valores totais sao incrementados na devida key e o nome(primeiro e ultimo) adicionado há lista de nomes dessa faixa etária

 ## Comentarios adicionais

 Foi feito um menu que cada opção responde às devidas questões.
 Vale realçar que para o código ser compilado é preciso o ficheiro CSV estar na mesma pasta que o módulo python!
