# Usando for para imprimir os andares de 1 a 20
# Codigo 1
for andar in range(1, 21):
    if andar == 13:
        continue  # pula o 13º andar
    print(andar)

# Usando while para imprimir os andares
# Codigo 2
andar = 1
while andar <= 20:
    if andar != 13:
        print(andar)
    andar += 1

# Usando while para imprimir em ordem decrescente
# Codigo 3
andar = 20
while andar >= 1:
    if andar != 13:
        print(andar)
    andar -= 1
