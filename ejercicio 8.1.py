def diccionarioCuadrados():
    n=int(input("Escribe un número: "))
    numeros={}
    for i in range(n):
        numeros[i+1]=((i+1)**2)
    print(numeros)

if __name__ == "__main__":
    diccionarioCuadrados()



