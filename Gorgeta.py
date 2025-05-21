def gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:

    return valor_conta * (porcentagem_gorjeta / 100)



try:
        
        valor_conta = float(input("Informe o valor da conta: R$ "))
        percentual_gorjeta = float(input("Informe o percentual da gorjeta (%): "))
        
        valor_gorjeta = gorjeta(valor_conta, percentual_gorjeta)
        total = valor_conta + valor_gorjeta
        
        print(f"\nValor da gorjeta: R$ {valor_gorjeta:.2f}")
        print(f"Valor total (conta + gorjeta): R$ {total:.2f}")

except ValueError:
    print("Por favor, insira valores numéricos válidos.")
