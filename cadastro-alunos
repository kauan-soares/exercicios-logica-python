cadastros = []
c = True

while c:
    entrada = input("Digite seu nome e email separados por (;): ").split(";")
    if len(entrada) == 2:
        nome = entrada[0].strip()
        email = entrada[1].strip().lower()
        cadastros.append({"nome": nome, "email": email})
        continuar = input("Deseja fazer um novo cadastro? {sim/não}: ").strip().lower() == "sim"
        c = continuar
    else:
        print("Entrada inválida. Por favor, digite seu nome e email separados por ';'.")

for cadastro in cadastros:
    print(f"{cadastro['nome']} | {cadastro['email']}")

print(f"Total de cadastros: {len(cadastros)}")