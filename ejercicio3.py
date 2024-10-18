import math
catetoA = float(input('Cuanto mide el primer cateto: '))
catetoB = float(input('Cuanto mide el segundo cateto: '))
hipotenusa = math.sqrt(catetoA**2 + catetoB**2)
print("La hipotenusa es:", hipotenusa)