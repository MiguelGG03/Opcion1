import pandas as pd

f = open("auto-mpg.data", mode='r',encoding='utf-8')
lista_con_datos = []

for i in f:
    
    var=i.replace('\t',' ')
    var2=var.replace('\n','')
    var3=var2[0:7].strip()
    var4=var2[7:11].strip()
    var5=var2[11:22].strip()
    var6=var2[22:33].strip().replace('?','0.0')
    var7=var2[33:44].strip().replace('.','')
    var8=var2[44:51].strip()
    var9=var2[51:55].strip()
    var10=var2[55:57].strip()
    var11=var2[57:].strip().replace('"','')

    lista_con_datos.append([float(var3),int(var4),float(var5),float(var6),int(var7),float(var8),int(var9),int(var10),var11])



print(lista_con_datos)

