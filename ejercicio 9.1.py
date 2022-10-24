from random import randint, random

def prueba():
    print("Vamos a probarte en multiplicaciones: ")
    aciertos=0
    for i in range(10):
        a = randint(2,9)
        b = randint(2,9)
        res = int(input(str(a)+ " x " + str(b) + " = "))
        if (a*b==res):
            print("correcto")
            aciertos+=1
        else:
            print("incorrecto")
    print("El total de aciertos es: " +str(aciertos))

if __name__ == "__main__":
    prueba()