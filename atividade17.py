ano_nascimento = int(input("Informe o ano de nascimento: "))

import datetime
ano_atual = datetime.datetime.now().year

idade = ano_atual - ano_nascimento

if idade < 18:
    anos_restantes = 18 - idade
    print(f"Você tem {idade} anos e precisa se alistar daqui a {anos_restantes} anos.")
elif idade == 18:
    print("Você tem 18 anos e está na hora de se alistar no serviço militar.")
else:
    anos_passados = idade - 18
    print(f"Você tem {idade} anos e já passaram {anos_passados} anos do prazo de alistamento.")