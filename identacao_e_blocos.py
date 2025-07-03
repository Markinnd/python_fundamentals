# Em Pythoin, a identação é crucial para definir blocos de código.
# Um bloco de código é um conjunto de instruções que são executadas juntas.
# A identação é feita com espaços ou tabulações, mas deve ser consistente.  

# Exemplo de bloco de código com identação
def sacar(valor):
    if valor > 0:
        print(f"Saque de {valor} realizado com sucesso.")
    else:
        print("Valor inválido para saque.")

sacar(100)  # Saída: Saque de 100 realizado com sucesso.
sacar(-50)  # Saída: Valor inválido para saque.

