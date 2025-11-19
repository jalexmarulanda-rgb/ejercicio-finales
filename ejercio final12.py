# " determinar la paridad de tres numero"

a= int(input("ingrese el primer numeros"))
b= int(input("ingrese el segundo numeros"))  
c= int(input("ingrese el tercer numeros"))

if a % 2 == 0 and b % 2 == 0  and c % 2 == 0:
   print ("el resultado todos son pares:")
elif a % 2 != 0 and b % 2 != 0  and c % 2 != 0:
   print ("el resultado todos son impares")
else:
  print ("hay mexcla de pares e impares")