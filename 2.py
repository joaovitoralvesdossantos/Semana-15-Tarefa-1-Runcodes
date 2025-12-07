# Função para fazer a soma e conversão das temperaturas
def soma_temperaturas(t1, t2):
    temp1, esc1 = t1
    temp2, esc2 = t2

    # Se a segunda escala for Celsius
    if esc2 == 'C':
        if esc1 == 'F':  
            # converte temp1 para Celsius
            temp1 = (temp1 - 32) * 5/9
        soma = temp1 + temp2
        return (round(soma, 4), 'C')

    # Se a segunda escala for Fahrenheit
    else:
        if esc1 == 'C':
            # converte temp1 para Fahrenheit
            temp1 = temp1 * 9/5 + 32
        soma = temp1 + temp2
        return (round(soma, 4), 'F')

# função principal
def main():

    # entrada de dados
    temp1 = float(input("Digite a primeira temperatura: "))
    esc1 = input("Digite a escala da primeira temperatura (C/F): ").upper()[0]

    temp2 = float(input("Digite a segunda temperatura: "))
    esc2 = input("Digite a escala da segunda temperatura (C/F): ").upper()[0]

    # processamento
    t1 = (temp1, esc1)
    t2 = (temp2, esc2)
    resultado = soma_temperaturas(t1, t2)

    # saída de dados 
    print(resultado)

# chama a função principal
if __name__ == "__main__":
    main()