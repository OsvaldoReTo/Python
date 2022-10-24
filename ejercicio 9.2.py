def cuadrados():
    lista=[1,2,3,4,5,6,7,8,9,10]
    cuadrados=[]
    for i in range(len(lista)):
        cuadrados.append(lista[i]**2)
    print(cuadrados)
if __name__ == "__main__":
    cuadrados()