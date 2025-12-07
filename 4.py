# função para carregar a lista das cidades
def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, hab = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(hab))
            )
    return resultado

# função para carregar as cidades pela população
def cidades_maiores(hab_minima, cidades):
    for cidade in cidades:
        uf, ibge, nome, dia, mes, hab = cidade
        
        if hab > hab_minima:
            print(f"IBGE: {ibge} - {nome}({uf}) - POPULAÇÃO: {hab}")


def main():
    # entrada de dados
    hab = int(input("Digite a população mínima: ")) 
    
    # processamento
    cidades = carrega_cidades()

    # saída de dados
    print(f"CIDADES COM MAIS DE {hab} HABITANTES:")
    cidades_maiores(hab, cidades)

# cha,ma a função principal
if __name__ == "__main__":
    main()