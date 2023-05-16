#/Construya un programa en Python que realice las siguientes
#/operaciones:

ficha=[]
opera=1
opera=int(input("Selecciona UNO para abrir la ficha \n"))
while opera==1:
    elem1=int(input("Deseas agrege un instructor a la ficha UNO para si, DOS para no\n"))
    if elem1==1:
#/ Permita agregar el nombre de un instructor a la lista
        elem=str(input("Agrege Nombre del Instructor\n"))
        ficha.append(elem)
        print(ficha)
        elem3=int(input("Desea agregar otro Instructor a la ficha UNO para si DOS para no\n"))
        while elem3==1:
            elem=str(input("Agrege Nombre del instructor\n"))
            ficha.append(elem)
            print(ficha)
            elem3=int(input("Desea agregar otro Instructor a la ficha UNO para si DOS para no\n"))
    elif elem1==2:
        print("No tiene un Instructor asignado")
        break
    else:
        print("No cumple con las caracteristicas de Ingreso")
        break   
#/Listar los instructores que están en la lista
    elem2=int(input("Deseas ver la listar de instructores asignados  de forma A-Z UNO para si DOS para no\n")) 
    if elem2==1:
        ficha.sort(reverse=False)
        print("Los Instructores asignados a la ficha son: \n ",ficha)
        del ficha[0]
        print("Se borrara el ultimo de la ficha por falta de horarios\n ",ficha)
        print("Ficha actualizada a la fecha \n",ficha)
        for i, e in enumerate(ficha):
            print(i,e)
    else:
        print("Confiemado los registros actuales ",ficha)
#/Modificar un elemento de la lista (seleccionado por el usuario)
    dato=int(input("Desea modificar un Instructor de la ficha UNO para si, DOS para no\n"))
    if dato==1:
        dato1=int(input("Selecciona numero del Instructor a modificar\n"))

        dato2=str(input("Ingrese nombre\n"))
        ficha[dato1]=dato2
       
        print("Confirmacion de ficha a la fecha ",ficha)
    else:
        print("Comprobando instructores a la fecha ",ficha)
#/Borrar un elemento de la lista (seleccionado por el usuario)
    dato=int(input("Desea retirar un Instructor de la ficha UNO para si, DOS para no\n"))
    if dato==1:
        dato1=str(input("Selecciona el Instructor\n"))
        ficha.remove(dato1)
        print("Confirmacion de ficha a la fecha ",ficha)
    else:
        print("Comprobando instructores a la fecha ",ficha)
    opera1=int(input("Desea cerrar la ficha UNO para si y DOS para no\n"))
    if opera1==1:
        opera=2
#/Buscar un elemento particular de la lista por su nombre sin importar las mayúsculas o minúsculas.

#/Ordenar la lista de instructores de la A-Z
    
print("Cerraste la ficha ")