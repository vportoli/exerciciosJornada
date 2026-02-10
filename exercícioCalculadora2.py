def calculadora():
    while True:
        print("\n=== Bem-vindo à Calculadora ===")
        print("Escolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número da operação: ")

        if opcao == "0":
            print("Encerrando a calculadora... Até logo!")
            break
        elif opcao in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if opcao == "1":
                    resultado = num1 + num2
                    print(f"Resultado da soma: {resultado}")
                elif opcao == "2":
                    resultado = num1 - num2
                    print(f"Resultado da subtração: {resultado}")
                elif opcao == "3":
                    resultado = num1 * num2
                    print(f"Resultado da multiplicação: {resultado}")
                elif opcao == "4":
                    if num2 == 0:
                        print("Não é possível dividir por zero!")
                    else:
                        resultado = num1 / num2
                        print(f"Resultado da divisão: {resultado}")
            except ValueError:
                print("Entrada inválida! Por favor, digite apenas números.")
        else:
            print("Essa opção não existe. Tente novamente.")

# Para rodar a calculadora:
calculadora()
