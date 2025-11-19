#"realizar una calificacion de imc"
peso= float(input("el peso:"))
altura= float(input("la altura:"))
imc= peso/ (altura**2)



if imc < 18.5 :
   print ("bajo peso:")

elif imc < 25:
     print ("normal:")
elif imc < 30:
     print ("sobrepeso:")

else:
  print ("esta obeso ")