def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def divisao(x, y):
    return x / y

def multiplicacao(x, y):
    return x * y

while True:
    try:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        operador = input("Informe a operação (+, -, *, /): ")

        if operador == '+':
            resultado = adicao(x, y)
        elif operador == '-':
            resultado = subtracao(x, y)
        elif operador == '*':
            resultado = multiplicacao(x, y)
        elif operador == '/':
            if y == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida.")
            resultado = divisao(x, y)
        else:
            print("Operação inválida. Use apenas +, -, * ou /.")
            continue

        print(f"Resultado: {resultado}")
        break  

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
