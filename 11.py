salario_anterior = float(input("digite seu salario atual:"))
salario_atual = 0.0
diferenca_entre_salarios = 0.0
percentual_de_aumento = 0.0

if salario_anterior <= 280:
    percentual_de_aumento = 20 
elif salario_anterior <= 750:
    percentual_de_aumento = 15
elif salario_anterior <= 1500:
    percentual_de_aumento = 10
else:
   percentual_de_aumento = 5

difenca_entre_salarios = salario_anterior * (percentual_de_aumento / 100)
salario_atual = salario_anterior + diferenca_entre_salarios
print(f"seu salario antes do reajuste era  de R${salario_anterior:.2f}")
print(f"seu salario foi aumentando em {percentual_de_aumento}%")
print(f"seu salario oi aumentado em R${difenca_entre_salarios:.2f}")
print(f"seu salario atual e de R$ {salario_atual:.2f}")




