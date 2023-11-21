turno = input(
    "digite seu turno, M - matutino, V - vespertino, N - noturno:"
).upper()
if turno == "M":
    print("bom dia!")
elif turno == "V":
    print("boa tarde!")
elif turno == "N":
    print("boa noite!")
else:
    print("valor invalido!")