def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y


def menu():
    print(f"Selecione a operação: \n")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print(f"5. Sair \n")

def obter_numero(prompt):
    while True:
        try:
            numero = float(input(prompt))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def calculadora():
    while True:
        menu()
        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == '5':
            print("Obrigado por usar a calculadora. Até mais!\n\n")
            break

        if escolha in ['1', '2', '3', '4']:
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")

            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
            elif escolha == '4':
                resultado = dividir(num1, num2)
                if resultado == "Erro: Divisão por zero não é permitida.":
                    print(resultado)
                else:
                    print(f"Resultado: {num1} / {num2} = {resultado} \n ")
        else:
            print("Escolha inválida. Por favor, selecione uma opção de 1 a 5.\n\n ")

if __name__ == "__main__":
    calculadora()
