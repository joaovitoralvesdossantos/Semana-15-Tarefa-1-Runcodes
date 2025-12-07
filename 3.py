# função para carregar o arquivo cidades
def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, hab = linha.split(';')
            resultado.append(
                    (uf, int(ibge), nome, int(dia), int(mes), int(hab))
                )
    return resultado

# função principal
def main():

    # Entrada de dados
    dia = int(input("Digite o dia do aniversário: "))
    mes = int(input("Digite o mês do aniversário (1-12): "))

    cidades = carrega_cidades()

    # Nome dos meses para impressão
    nomes_meses = [
        "", "JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO",
        "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"
    ]

    if 1 <= mes <= 12:
        print(f"CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {nomes_meses[mes]}:")

        # Processamento
        for uf, ibge, nome, d, m, hab in cidades:
            if d == dia and m == mes:
                print(f"{nome}({uf})")
    else:
        print("Mês inválido.")

# chama a função principal
if __name__ == "__main__":
    main()