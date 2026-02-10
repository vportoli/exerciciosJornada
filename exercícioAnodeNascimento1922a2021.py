# Programa para calcular idade a partir do ano de nascimento
# pedimos o nome
nome = input("Digite seu nome completo: ")

# pedimos o ano de nascimento
while True:
    try:
        ano = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))

        # Verificando se o ano está dentro do intervalo permitido
        if ano >= 1922 and ano <= 2021:
            idade = 2022 - ano
            print(f"\nOlá {nome}, em 2022 você terá {idade} anos.")
            break
        else:
            print("Ano fora do intervalo, tente novamente.")
    except:
        print("Você digitou algo errado, por favor digite apenas números.")

print("Fim do programa")
