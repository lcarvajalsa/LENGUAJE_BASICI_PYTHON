baul=[]
opera=1
opera=int(input("Selecciona UNO para abrir tu baúl\n"))
while opera==1:
    elem1=int(input("Deseas agrege un elemento al Baúl UNO para si, DOS para no\n"))
    if elem1==1:
        elem=str(input("Agrege un elemento al Baúl\n"))
        baul.append(elem)
        print(baul)
        elem3=int(input("Desea agregar otro elemento UNO para si DOS para no\n"))
        while elem3==1:
            elem=str(input("Agrege un elemento al Baúl\n"))
            baul.append(elem)
            print(baul)
            elem3=int(input("desea agregar otro elemento UNO para si DOS para no\n"))
    elif elem1==2:
        print("No has agregado elemento")
        break
    else:
        print("Elección incorrecta")
        break   
    elem2=int(input("Deseas ver la listar articulos del baul de forma ascendente UNO para si DOS para no\n")) 
    if elem2==1:
        baul.sort(reverse=False)
        print("Sus elemento al Baúl\n ",baul)
        del baul[0]
        print("Borraste el ultimo de la lista\n ",baul)
        print("Lista de tu Baul \n",baul)
        for i, e in enumerate(baul):
            print(i,e)
    else:
        print("Sus elemento al Baúl ",baul)
    dato=int(input("Desea retirar un elemento del Baúl UNO para si, DOS para no\n"))
    if dato==1:
        dato1=str(input("Selecciona el elemento\n"))
        baul.remove(dato1)
        print("Sus elemento al Baúl ",baul)
    else:
        print("Sus elemento al Baúl ",baul)
    opera1=int(input("Desea cerrar el Baúl UNO para si y DOS para no"))
    if opera1==1:
        opera=2
print("Cerraste tu Baúl")
