# "realizar una calculadora basica"

a= float(input("ingrese el primer numeros"))
b= float(input("ingrese el segundo numero"))  
op= input("ingrese el operador (+,-,*,/): ")

if op == "+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op== "*":
    print(a*b)
elif op== "/":
    print(a/b)
else:
    print("el operador no es valido")
        