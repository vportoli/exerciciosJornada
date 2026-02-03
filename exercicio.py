def calculadora(num1, num2, operacao):
    if operacao == 1:        # Soma
        return num1 + num2
    elif operacao == 2:      # Subtração
        return num1 - num2
    elif operacao == 3:      # Multiplicação
        return num1 * num2
    elif operacao == 4:      # Divisão
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: divisão por zero"
    else:                    # Operação inválida
        return 0
