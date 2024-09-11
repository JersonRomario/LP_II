nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (M para masculino, F para femenino): ").upper()
if (sexo == "F" and nombre[0].upper() < "F") or (sexo == "M" and nombre[0].upper() > "O"):
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")