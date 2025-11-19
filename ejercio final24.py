# "determinar el salario con horas extras"

print(" ingrese cuantas horas son ")
horas = float(input("horas trabajadas:"))
pago= float(input("pagos por horas:"))
 
if horas > 40:
    extra = ( horas - 40) * pago * 1.5 
    total = 40 * pago + extra 
else:
    total = horas * pago 
    


print(" el resultado del salario total:", total)
