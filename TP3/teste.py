import re


lista = []
texto = "123 Off 456 On 789 = 10"
sequencias = re.findall(r'\d', texto)
textt = "123 Off 456 On 789 = 10"
seq = re.findall(r'\d', textt)

lista.append(sequencias)

lista.append(seq)

print(lista)