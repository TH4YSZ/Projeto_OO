import random

# Gera a parte antes do traço (8 dígitos)
parte_numerica = ''.join([str(random.randint(0, 9)) for _ in range(8)])

# Gera o dígito após o traço (1 dígito)
digito_verificador = random.randint(0, 9)

# Cria a sequência completa no formato desejado
numero_formatado = f"{parte_numerica}-{digito_verificador}"
print(numero_formatado) 