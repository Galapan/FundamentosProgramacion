import math
X1 = float(input('Cordenada X1: '))
X2 = float(input('Cordenada X2: '))
Y1 = float(input('Cordenada Y1: '))
Y2 = float(input('Cordenada Y2: '))
distancia = math.sqrt((X1-X2)**2 + (Y1-Y2)**2)
print("La distancia es de:",distancia)