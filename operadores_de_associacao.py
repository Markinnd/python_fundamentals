# Operadores de Associação
# # Os operadores de associação em Python são usados para verificar se um valor está presente em uma sequência, como listas, tuplas ou strings.
# # Os principais operadores de associação são: `in` e `not in`.
# # O operador `in` retorna True se o valor estiver presente na sequência.
# # O operador `not in` retorna True se o valor não estiver presente na sequência.  

# Exemplo de uso dos operadores de associação
curso = "Curso de Python"
frutas = ["maçã", "banana", "laranja"]
saques = [100, 200, 300]

# Verifica se "Python" está presente na string curso
print("Python" in curso)  # Saída: True (Python está presente na string curso)      
# Verifica se "Java" está presente na string curso
print("Java" in curso)  # Saída: False (Java não está presente na string curso) 
# Verifica se "maçã" está presente na lista frutas
print("maçã" in frutas)  # Saída: True (maçã está presente na lista frutas)
# Verifica se "uva" está presente na lista frutas
print("uva" in frutas)  # Saída: False (uva não está presente na lista frutas)  
# Verifica se 200 está presente na lista saques
print(200 in saques)  # Saída: True (200 está presente na lista saques)
# Verifica se 400 está presente na lista saques 
print(400 in saques)  # Saída: False (400 não está presente na lista saques)
