# variaveis e constantes
# Variáveis - são usadas para armazenar valores que podem mudar durante a execução do programa.
# Em Python, não há declaração explícita de tipo, mas é uma boa prática usar nomes descritivos.

age = 30
name = "João"

print(f'Idade: {age}, Nome: {name}')

age, name = 25, "Maria"
print(f'Idade: {age}, Nome: {name}')

# Constantes - o valor não deve ser alterado
# Em Python, não há uma maneira de declarar constantes de forma nativa, mas é comum usar letras maiúsculas para indicar que uma variável é uma constante.
# Em Python, há uma convenção de nomenclatura para constantes, que é usar letras maiúsculas e sublinhados.

# Boas práticas
# O padrão de nomes deve ser snake case
# Escolher nomes descritivos e significativos
# Nome de constantes deve ser em letras maiúsculas

limite_saque_diario = 1000.00

BRAZILIAN_STATES = [
    "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia",
    "Ceará", "Distrito Federal", "Espírito Santo", "Goiás",
    "Maranhão", "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais",
    "Pará", "Paraíba", "Paraná", "Pernambuco",
    "Piauí", "Rio de Janeiro", "Rio Grande do Norte",
    "Rio Grande do Sul", "Rondônia", "Roraima",
    "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
]

print(f'Limite de saque diário: {limite_saque_diario}')
print(f'Estados brasileiros: {", ".join(BRAZILIAN_STATES)}')


