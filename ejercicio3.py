import math
catetoA = input('Cuanto mide el primer cateto: ')
catetoA =int(catetoA)
catetoB = input('Cuanto mide el segundo cateto: ')
catetoB =int(catetoB)
hipotenusa = math.sqrt(catetoA**2 + catetoB**2)
print("La hipotenusa es:", hipotenusa)