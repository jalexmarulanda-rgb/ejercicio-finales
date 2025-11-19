#  "determinar una clasificacion de edades"
print(" ingrese las edades de las personas")
edad = int(input())
if edad<=12:
    print("la persona es un niño")
elif edad<=17:
    print("la persona es un adolecente")
elif edad<=64:
    print("la persona es un adulto")
else:
    print("la persona es un adulto mayor") 