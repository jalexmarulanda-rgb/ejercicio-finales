 #"realizar un calculo de impuestos"
ing= float(input("el ingreso anual:"))
 
 
 
 
 
if ing < 20000 : imp = ing * 0.05
elif ing < 50000: imp = ing * 0.10
else : imp = ing * 0.15
print("impuesto a pagar:",imp)
 