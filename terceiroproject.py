c = 1

def calcular_total (preco, quantidade, desconto):
    subtotal = preco * quantidade
    total = subtotal - desconto
    return total
while True:
      quantidade = int(input("Digite a quantidade que vai vender: "))
      if quantidade == 0:
         print("ENCERRANDO...")
         break
      preco = float(input("Digite o preço da unidade: "))
      desconto = int(input("Digite o valor do desconto: "))
      if quantidade > 0:
         resultado = calcular_total(preco, quantidade, desconto)
         if resultado >= 200:
             print("Frete grátis")
         print("---------------------------")
         print(f"{c}o. Compra")
         print(f"Valor da compra: R${resultado}")
         print("---------------------------")
         continuar = input("Quer continuar? {sim/não}: ").strip().lower() == "sim"
         if not continuar:
             print("Encerrando..")
             break
         else:
             c = c + 1
      elif quantidade < 0:
           print("Valor inválido")
