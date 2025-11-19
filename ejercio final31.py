"realizar un rango de puntaje"
p = float(input("el puntaje 0-100:"))

if p >= 90: r = "A"
elif p >= 80: r = "b"
elif p >= 70: r = "c"
elif p >= 60: r = "d"
else: r = "f"
print("el rango:", r)