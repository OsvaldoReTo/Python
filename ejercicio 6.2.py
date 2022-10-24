def primos():
    flag=0
    N =int(input("Introduce la cantidad de primos que quieras: "))
    filtro=[]
    arr=[2]
    output=[]
    for i in range(2,300):
        for j in range(len(arr)):
            if i%arr[j]==0:
                break
            else:
                arr.append(i)
                arr=list(set(arr))
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                continue
            else:
                if arr[i]%arr[j]==0:
                    filtro.append(arr[i])
                    filtro=list(set(filtro))
    for m in range(len(filtro)):
        arr.remove(filtro[m])
    for k in range(N):
        output.append(arr[k])
    print(output)

if __name__ == "__main__":
    primos()