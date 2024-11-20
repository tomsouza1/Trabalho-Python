# Definição da função loginUsuario
def loginUsuario(perfil):
    # Verificação do perfil (considerando letras maiúsculas e minúsculas)
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Chamadas da função com diferentes valores para o parâmetro
loginUsuario('Admin')  # Maiúscula e minúscula
loginUsuario('admin')  # Apenas minúscula
loginUsuario('User')   # Outro perfil
loginUsuario('usuário')  # Valor diferente de admin