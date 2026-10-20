def calcular_total(preco, quantidade, desconto, cupom):
    subtotal = preco * quantidade
    if cupom:
        subtotal = subtotal * 0.90
    total = subtotal - desconto   
    return total

cadastros = []
lista_vendas = []

while True:
    print("\n====  SISTEMA DE GESTÃO DE VENDAS  ====")
    opcao = int(input("1 - Cadastrar Clientes \n2 - Listar Clientes \n3 - Registrar Venda \n4 - Exibir Relatório Geral \n0 - Sair \nEscolha uma opção: "))
    
    if opcao == 1:
        while True:
            entrada = input("Digite seu nome e email, separado por (;): ").split(";")
            if len(entrada) == 2:
                nome = entrada[0].strip()
                email = entrada[1].strip().lower()
                cadastros.append({"nome": nome, "email": email})
                print("Cliente cadastrado com sucesso!")
                break
            else:
                print("Entrada inválida. Por favor, digite seu nome e email separados por ';'.")
                
    elif opcao == 2:
        if not cadastros:
            print("Nenhum cliente cadastrado até o momento.")
        else:
            for cadastro in cadastros:
                print("----------------------------------------------")
                print(f"{cadastro['nome']} | {cadastro['email']}")
                print("----------------------------------------------")
                
    elif opcao == 3:
        while True:
            email_cliente = input("Digite o E-mail do cliente: ")
            quantidade = int(input("Digite a quantidade a ser vendida: "))
            
            if quantidade > 0:
                preco = float(input("Digite o valor unitario do produto: "))
                cupom = input("Você tem cupom? {sim/não}: ").strip().lower() == "sim"
                desconto = float(input("Digite o valor de desconto: "))
                frete = float(input("Digite o valor do frete: "))
              
                total_vendas = calcular_total(preco, quantidade, desconto, cupom)
                
                if total_vendas >= 200:
                    frete = 0
                elif total_vendas >= 100:
                    frete = frete / 2             
                
                lista_vendas.append({
                    "email_cliente": email_cliente, 
                    "total_vendas": total_vendas, 
                    "frete": frete
                })
                print(f"Venda registrada com sucesso! Total: R$ {total_vendas:.2f} | Frete: R$ {frete:.2f}")
                break
                
            elif quantidade == 0:
                print("Saindo do registro de vendas...")
                break
            else:
                print("Valor inválido")
                
    elif opcao == 4:
        faturamento_total = sum(venda["total_vendas"] for venda in lista_vendas)
        print ("==================================================")
        print("\n================ RELATÓRIO GERAL ================")
        print(f"Total de clientes cadastrados: {len(cadastros)}")
        print(f"Total de vendas realizadas: {len(lista_vendas)}")
        print(f"Faturamento total acumulado: R$ {faturamento_total:.2f}")
        print("=================================================")
        
    elif opcao == 0:
        print("Saindo...")
        break