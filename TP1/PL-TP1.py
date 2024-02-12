import sys
import os

def read_csv(arquivo):
    with open(arquivo, 'r') as file:
        next(file)
        modalidades = []
        able = 0
        enable = 0
        distribuicao = {}

        for line in file:
            row = line.rstrip().split(',')
            modalidades.append(row[8])
            if row[12] == 'true':
                able +=1
            else:
                enable +=1
            idade = int(row[5])
            key = (idade//5)*5 
            nome = row[3] + ' ' + row [4]
            if key not in distribuicao:
                distribuicao[key] = (1,[nome])
            else:
                totaln, nomes = distribuicao[key]
                distribuicao[key] = (totaln + 1, nomes + [nome])

    modalidadesort = sorted(list(set(modalidades)))

    total = able + enable
    percent_able = (able / total) * 100
    percent_enable = (enable / total) * 100

    return modalidadesort, percent_able, percent_enable, distribuicao

def main():
    modalidadesort, percent_able, percent_enable, distribuicao = read_csv('emd.csv')
    while True:
        print("\nMenu:")
        print("1. Lista ordenada alfabeticamente das modalidades desportivas")
        print("2. Percentagens de atletas aptos e inaptos para a prática desportiva")
        print("3. Distribuição de atletas por escalão etário")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("Modalidades desportivas ordenadas:", modalidadesort)
        elif opcao == '2':
            print("Percentagem de atletas aptos:", percent_able)
            print("Percentagem de atletas inaptos:", percent_enable)
        elif opcao == '3':
            for i in range(0, 100, 5):
                if i in distribuicao: 
                    print(f"[{i}-{i+4}]:", distribuicao[i])
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()