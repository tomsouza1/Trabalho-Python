# Variável de controle para saída do programa
saida = '6'

# Função de adição
def adicao(a, b):
    return a + b

# Função de subtração
def subtracao(a, b):
    return a - b

# Função de multiplicação
def multiplicacao(a, b):
    return a * b

# Função de divisão
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

# Função principal da calculadora
def calculadora(num1, num2, operacao):
    operacao = operacao.lower()
    if operacao in ['+', 'adicao']:
        resultado = adicao(num1, num2)
    elif operacao in ['-', 'subtracao']:
        resultado = subtracao(num1, num2)
    elif operacao in ['*', 'multiplicacao']:
        resultado = multiplicacao(num1, num2)
    elif operacao in ['/', 'divisao']:
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida. Tente novamente."
    return resultado

# Laço principal do programa
while saida.lower() != 'n':
    try:
        # Solicita os valores e a operação do usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, / ou o nome da operação): ")

        # Chamada à função calculadora
        resultado = calculadora(num1, num2, operacao)

        # Exibe o resultado
        print(f"Resultado da operação: {resultado}")

        # Pergunta se o usuário deseja continuar
        saida = input("Deseja continuar? (S/N): ")
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")