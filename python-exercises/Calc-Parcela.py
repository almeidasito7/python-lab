def calcular_parcela(preco_final, parcelas):
    percentuais_acrescimo = {
        6: 0.03,  # 3% de acréscimo para 6 parcelas
        12: 0.06,  # 6% de acréscimo para 12 parcelas
        18: 0.09,  # 9% de acréscimo para 18 parcelas
        24: 0.12,  # 12% de acréscimo para 24 parcelas
        30: 0.15,  # 15% de acréscimo para 30 parcelas
        36: 0.18,  # 18% de acréscimo para 36 parcelas
        42: 0.21,  # 21% de acréscimo para 42 parcelas
        48: 0.24,  # 24% de acréscimo para 48 parcelas
        54: 0.27,  # 27% de acréscimo para 54 parcelas
        60: 0.30   # 30% de acréscimo para 60 parcelas
    }
    acrescimo = preco_final * percentuais_acrescimo[parcelas]
    preco_total = preco_final + acrescimo
    valor_parcela = preco_total / parcelas
    return preco_total, valor_parcela

def main():
    preco_carro = float(input("Digite o valor do carro: "))

    preco_final_avista = preco_carro * 0.8  # Desconto de 20% para pagamento à vista
    print(f"Preço final à vista (20% de desconto): R$ {preco_final_avista:.2f}")

    print("\nTabela de Parcelamento:")
    print("")
    for parcelas in range(6, 61, 6):
        preco_total, valor_parcela = calcular_parcela(preco_carro, parcelas)
        print(f"O preço final parcelado em {parcelas}x é de R$ {preco_total:.2f} com parcelas em R$ {valor_parcela:.2f}")

if __name__ == "__main__":
    main()