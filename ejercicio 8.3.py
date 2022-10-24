def compraFrutas():
    answer="si"
    while(answer == "si"):
        precioFrutas={"platano":30.32, "naranja": 14.50, "manzana": 17.80, "kiwi":32.53, "sandia":30.5}
        clave = input("¿Que fruta desea comprar? ")
        cantidad = int(input("indique cuantas frutas desea: "))
        if clave in precioFrutas:
            print("El pago total por la compra de " + clave +" es: $" + str(precioFrutas[clave]*cantidad))
            answer=input("¿Quiere continuar consultando? (Si/No): ")
            answer.lower()
        else:
            print("No tenemos esa fruta")
            answer=input("¿Quiere continuar consultando? (Si/No): ")
            answer.lower()
if __name__ == "__main__":
    compraFrutas()



    