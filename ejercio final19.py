# "determina cuales son el promedio de las  cinco asignaturas"

print(" ingrese cuales son las cinco asignaturas ")
notas  = []
for i in range(5):
    notas.append(float(input("notas: ")))
    
    prom= "suma"(notas)/5
    print("promedio:", prom)
        
if prom < 3:
    print("bajo")
elif prom<4:
     print("medio")
else:
     print("alto")
    