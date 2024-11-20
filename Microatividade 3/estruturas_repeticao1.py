# Variável inicial
entrada_idade = '0'  # Valor inicial é uma string vazia

# Estrutura de repetição
while str(entrada_idade) != '0':
    # Solicita entrada do usuário
    entrada_idade = input('Digite um número qualquer ou 0 para sair: ')
    
    # Exibe o número digitado pelo usuário
    print(f'Número digitado: {entrada_idade}')