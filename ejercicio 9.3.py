total=0
tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
print("Considerando la tupla: "+ str(tupla))
for i in range(len(tupla)):
    if tupla[i]>5:
        total+=1
print("Existen "+ str(total) + " números mayores a 5 en la tupla")