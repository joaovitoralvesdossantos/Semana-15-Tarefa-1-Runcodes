# Função para as temperaturas
def maior_temp(t1, t2):
    temp1, escala1 = t1
    temp2, escala2 = t2

    # converte para Celsius se necessário
    if escala1 == 'F':
        temp1 = (temp1 - 32) * 5 / 9
    if escala2 == 'F':
        temp2 = (temp2 - 32) * 5 / 9

    if temp1 >= temp2:
        return t1
    else:
        return t2

# função principal
def main():

    # entrada de dados
    temp1 = float(input("Digite a primeira temperatura: "))
    esc1 = input("Digite a escala da primeira temperatura (C/F): ").upper()[0]

    temp2 = float(input("Digite a segunda temperatura: "))
    esc2 = input("Digite a escala da segunda temperatura (C/F): ").upper()[0]

    #processamento
    t1 = (temp1, esc1)
    t2 = (temp2, esc2)
    maior = maior_temp(t1, t2)

    # saída de dados
    print(maior)

# chama a função principal
if __name__ == "__main__":
    main()