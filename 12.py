valor_da_hora = float(input("digite quanto voce recebe por hora:"))
horas_trabalhadores = float(
    input("digite quantas horas voce trabalhou esse mês:")
)
salario_bruto = valor_da_hora = horas_trabalhadores
if salario_bruto <= 900:
    desconto_ir = 0.0
elif salario_bruto <= 150:
    desconto_ir = 5
elif salario_bruto <= 2500:
    desconto_ir = 10 
else:
    desconto_ir = 20

IR = salario_bruto = (desconto_ir / 100)
INSS = salario_bruto = (10 / 100)
FGTS = salario_bruto = (11 / 100)
total_de_descontos = IR + INSS
salario_liquido = salario_bruto - total_de_descontos

print(
f"nsalario bruto                  :R${salario_bruto:.2f}",
f"/n(-) IR (5%)                   :R${IR:.2f}",
f"/n(-) INSS (100)                :R${INSS:.2f}",
f"/nFGTS(10%)                     :R${FGTS:.2f}",
f"/ntotal de  descontos           :R${total_de_descontos:.2f}",
f"/nsalario liquido               :R${salario_liquido:.2f}",







)
