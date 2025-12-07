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

    # entrada de dados
    mes = int(input("Digite o mês (1-12): "))
    populacao = int(input("Digite a população mínima: "))

    cidades = carrega_cidades()

    # nomes dos meses
    nomes_meses = [
        "", "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    print(f"CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {nomes_meses[mes].upper()}:")

    # processamento e saída de dados
    for uf, ibge, nome, dia, mes_cid, hab in cidades:
        if hab > populacao and mes_cid == mes:
            print(f"{nome}({uf}) tem {hab} habitantes e faz aniversário em {dia} de {nomes_meses[mes]}.")

# chama a função principal:
if __name__ == "__main__":
    main()