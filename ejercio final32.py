"realizar un descuento por categoria"
cat= input("la categoria (a,b,c): ").upper()
if cat == "A": desc = 0.30
elif cat == "B":desc =0.20
elif cat == "c":desc =0.10
else:desc =0

precio=float(input("precio:"))
print("precio fianl:", precio * (1-desc))



