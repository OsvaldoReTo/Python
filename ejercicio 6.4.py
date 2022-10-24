def factorial():
    n=int(input("Introduzca un número para obtener su factorial: "))
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(str(n)+"! = "+str(fact))

if __name__ == "__main__":
    factorial()