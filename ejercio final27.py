#"realizar una calculadora simple"
n1= float(input("el numero 1:"))
n2= float(input("el numero 2:"))
op= input("operador (+-*/):")

if op == "/" and n2 ==0:
    print("error: no se puede dividir entero 0 ")
else:
    if op == "+": r = n1 + n2
    elif op == "-" : r = n1-n2
    elif op == "*" : r = n1*n2
    elif op == "/" : r = n1/n2
    else : r  ="operador invalido"
    print("resultado:".r)
    
    

