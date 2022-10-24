def pago():
    pago = 10
    total = pago
    print("El pago del mes: 1 es igual a: " + str(pago))
    for i in range(19):
        pago*=2
        total+=pago
        print("El pago del mes: " + str(i+2) + " es igual a: " + str(pago))
    print("el pago total fue: "+ str(total))
if __name__ == "__main__":
    pago()