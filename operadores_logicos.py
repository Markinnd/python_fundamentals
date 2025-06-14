
# And, Or e Not 

# Operadores lógicos em Python são usados para combinar condições booleanas.
# Os principais operadores lógicos são: and, or e not.      
## O operador `and` retorna True se ambas as condições forem verdadeiras.
# O operador `or` retorna True se pelo menos uma das condições for verdadeira.
# O operador `not` inverte o valor booleano da condição.    

# Exemplo de uso dos operadores lógicos

saldo = 1000
saque = 200
limite = 100

saldo >= saque and saldo >= limite  # Verifica se o saldo é maior ou igual ao saque e ao limite
# Saída: True (1000 é maior que 200 e 100)

saldo >= saque or saldo >= limite  # Verifica se o saldo é maior ou igual ao saque ou ao limite
# Saída: True (1000 é maior que 200, então a condição é verdadeira) 

saldo >= saque and saldo < limite  # Verifica se o saldo é maior ou igual ao saque e menor que o limite
# Saída: False (1000 não é menor que 100, então a condição é falsa) 

saldo >= saque or saldo < limite  # Verifica se o saldo é maior ou igual ao saque ou menor que o limite
# Saída: True (1000 é maior que 200, então a condição é verdadeira) 


not (saldo >= saque)  # Verifica se o saldo não é maior ou igual ao saque
# Saída: False (1000 é maior que 200, então a condição é falsa) 
not (saldo < limite)  # Verifica se o saldo não é menor que o limite
# Saída: True (1000 não é menor que 100, então a condição é verdadeira) 

contatos = []

not contatos  # Verifica se a lista de contatos está vazia
# Saída: True (a lista está vazia, então a condição é verdadeira)   

not ""  # Verifica se a string está vazia
# Saída: True (a string está vazia, então a condição é verdadeira)  


not 0  # Verifica se o número é zero
# Saída: True (0 é considerado falso em Python, então a condição é verdadeira)  

not 1  # Verifica se o número é diferente de zero
# Saída: False (1 é considerado verdadeiro em Python, então a condição é falsa) 

