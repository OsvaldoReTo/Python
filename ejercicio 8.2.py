def diccionariocaracteres():
    frase = input("Escribe una frase: ")
    dic = {}
    frase = frase.replace(" ","")
    for i in range(len(frase)):
        a = frase[i:i+1]
        if a in dic:
            dic[a]=dic[a]+1
        else:
            dic[a]=1
    print(dic)
if __name__ == "__main__":
    diccionariocaracteres()





