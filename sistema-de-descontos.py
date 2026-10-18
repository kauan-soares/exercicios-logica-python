c = 1

def calcular_total(preco, quantidade, desconto):
    subtotal = preco * quantidade
    total = subtotal - desconto
    return total

while True:
    quantidade = int(input("Digite a quantidade que vai vender: "))
    if quantidade == 0:
        print("ENCERRANDO...")
        break

    elif quantidade < 0:
        print("Valor inválido")
        continue
        
    preco = float(input("Digite o preço da unidade: "))
    desconto = int(input("Digite o valor do desconto: "))
    frete = float(input("Digite o valor do frete: "))
    cupom = input("Tem cupom de desconto? {sim/não}: ").strip().lower() == "sim"
    
    if quantidade > 0:
        resultado = calcular_total(preco, quantidade, desconto)
        
        if resultado >= 200:
            valor_frete = 0
        elif resultado >= 100:
            valor_frete = frete / 2
        else:
            valor_frete = frete
            
        print("-----------------------")
        print(f"{c}o. Compra")
        print(f"Valor da compra: R${resultado}")
        print(f"Valor do frete: R${valor_frete}")
        print("-----------------------")
        
        continuar = input("Quer continuar? {sim/não}: ").strip().lower() == "sim"
        if not continuar:
            print("-------------------------------")
            print(f"Quantidade de vendas: {c}")
            print("-------------------------------")
            print("Encerrando...")
            break
        else:
            c = c + 1