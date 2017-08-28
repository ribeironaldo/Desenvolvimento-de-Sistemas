valor = int(input("digite um valor : "))

if valor < 0:
    print (valor*-1)
elif valor > 10:
    valor2 = int(input("digite segundo valor de referência: "))
    print (valor - valor2)
else:
    print (valor/5)
