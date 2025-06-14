# Operadores de Identidade
 
# Os operadores de identidade em Python são usados para verificar se dois objetos são o mesmo objeto na memória.    
# Os principais operadores de identidade são: `is` e `is not`.  
# O operador `is` retorna True se os dois objetos forem o mesmo objeto na memória.
# O operador `is not` retorna True se os dois objetos não forem o mesmo objeto na memória.  

# Exemplo de uso dos operadores de identidade
saldo1 = 1000
limite = 1000   
# Verifica se saldo1 e saldo2 são o mesmo objeto na memória
print(saldo1 is limite)  # Saída: False (são valores iguais, mas objetos diferentes na memória)     
# Verifica se saldo1 e saldo2 não são o mesmo objeto na memória
print(saldo1 is not limite)  # Saída: True (são valores iguais, mas objetos diferentes na memória)  
# Verifica se saldo1 é o mesmo objeto que 1000
print(saldo1 is 1000)  # Saída: True (saldo1 é o mesmo objeto que 1000 na memória)
# Verifica se saldo1 não é o mesmo objeto que 1000
print(saldo1 is not 1000)  # Saída: False (saldo1 é o mesmo objeto que 1000 na memória) 

