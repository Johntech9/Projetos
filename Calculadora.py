saudacao = "seja bem vindo a calculadora virtual"
print(saudacao)

numero_1 = input("digite um número: ")
numero_2 = input("digite um número: ")
sinal = input("escolha um sinal entre +-/* ")

try:
    numero_float_1 = float(numero_1)
    numero_float_2 = float(numero_2)

    if sinal == "+":
        print(numero_float_1 + numero_float_2)
    elif sinal == "-":
        print(numero_float_1 - numero_float_2)
    elif sinal == "/":
        print(numero_float_1 / numero_float_2)
    elif sinal == "*":
        print(numero_float_1 * numero_float_2)
    else:
        print("Sinal inválido")

except ValueError:
    print("Entrada inválida, digite apenas números")

    