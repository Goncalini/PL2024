# Titulo

TPC 3 de PL - Somador on/off

# Autor

Gonçalo Daniel Machado Costa, A100824


# Explicação

Com o recurso da libraria 're' (regex) foi iterado ao longo do ficheiro linha a linha uma expressão regular que capturava e por sua vez armazenava cada ocorrencia de 'on', 'off', '=' e um digito numa lista de listas, essa mesma lista foi tranformada em uma lista com todos os elementos das sublistas e a mesma foi percorrida.\
A cada ocorrência de um 'on', uma flag auxiliar é ativade, e a mesma é desativada quando ocorre um 'off'.\
Quando a flag está ativada cada digito encontrado é adicionado ao somatório atual.\
A cada ocorrência de um '=' o somatório atual é imprimido.
