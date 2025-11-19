"realizar una verificacion de usuario y contraseña"
user= input("ingrese la el usuario: ")
clave= input("ingrese la contraseña: ")

if user == " admin" and clave == " 1234":
    print("acceso permitido")
else:
    print("acceso denegado")