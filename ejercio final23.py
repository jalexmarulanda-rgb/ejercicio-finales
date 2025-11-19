#"realizar una  de la temperatura ebullicion congelacion"
t = float(input("la temperatura:"))

if t < 0:
  print ("esta congelada :")
elif t < 100:
  print ("esta hirviendo:")
else:
  print ("la temperatura esta normal ")