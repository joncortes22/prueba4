"""
for x in range(4):
    num1 = int(input("Ingrese el primer valor: "))
    num2 = int(input("Ingrese el segundo valor: "))
    print(x)
    if num1>num2:
        print(f"El segundo valor es mayor ({num1})")
    else:
        print(f"El segundo valor es mayor ({num2})")
"""

orden = []
orden.append(int(input("Ingrese el primer valor: ")))
orden.append(int(input("Ingrese el segundo valor: ")))
orden.append(int(input("Ingrese el tercer valor: ")))
mayor = orden[0]

for x in range(len(orden)): #hacer prueba con doble for, como lo dijo max
    for i in range(len(orden)):
        if orden[x]>orden[i]:
            aux = orden[x]
            orden[x] = orden[i]
            orden[i] = aux
        

for x in orden:
    print(x)