"""
Problema:
1. De uno a cien
2. Si el numero es multiplo de 3 imprime Saul
3. Si el numero es multilplo de 5 imprime Eduardo
4. Si es 3 y de 5 imprime Saul Eduardo.
"""
# Funcion para calcular si el numero es multiplo
# utilizando el modulo de la división.

def funcion1(num1, num2):

	return True if num1 % num2 == 0 else False

listamultiplos3 = []
listamultiplos5 = []
interseccion= []

# bucle del 1 al 100

for i in range(1, 101):

    if funcion1(i, 3):
        listamultiplos3.append(i)

    if funcion1(i, 5):
        listamultiplos5.append(i)

for i in listamultiplos3:
	for i2 in listamultiplos5:

		if i == i2: #and i not in interseccion:
			interseccion.append(i)

print ("Los multiplos de 3 son:", listamultiplos3, "Se imprime Saúl")
print ("Los multiplos de 5 son:", listamultiplos5, "Se imprime Eduardo")
print ("Los multiplos comunes : ", interseccion, "Se imprime Saúl Eduardo")




