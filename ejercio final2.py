# "comparar tres numero"

a= int(input("ingrese numeros"))
b= int(input("ingrese numeros"))  
c= int(input("ingrese numeros"))

if a != b and a != c and b != c:
   if a > b: 
     if a > c:
          print ("el numero mayor es:" ,a)
     else:
          print ("el numero mayor es:" ,c)
   else:
        if b > c:
          print ("el numero mayor es:" ,b)
        else:
          print ("el numero mayor es:" ,c)
else:
    print ("ingrese tres numeros dirferentes")