# Abrir el archivo auto-mpg.data leerlo y almacenarlo en la variable f

f = open("auto-mpg.data", mode='r',encoding='utf-8')
lista_con_datos = []

for i in f:
    lista_con_datos.append(i.split(sep=' '))

for letter in lista_con_datos:
    for i in letter:
        if i == '':
            letter.remove(i)
       
for i in lista_con_datos:
    if i == []:
        lista_con_datos.remove(i)

for i in range(len(lista_con_datos)):
    for j in lista_con_datos[i]:
        if j=='':
            lista_con_datos[i].remove(j)

for i in range(len(lista_con_datos)):
    for j in lista_con_datos[i]:
        if j=='':
            lista_con_datos[i].remove(j)

for i in range(len(lista_con_datos)):
    for j in lista_con_datos[i]:
        if j=='':
            lista_con_datos[i].remove(j)



print(lista_con_datos)

