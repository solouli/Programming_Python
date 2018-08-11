#!/usr/bin/env python

muestras = ["Juan_0001_EC", "Juan_0001_EC_CT_MCT", "Juan_0001_EC_T1_M01", "Juan_0001_EC_T1_M02"]

lista01 = muestras[0].split("_")

nombre = lista01[0] + "_" + lista01[1] + "_"

for i in muestras:
    i = i.split("_")
    nombre = nombre + i[2]
    if len(i) > 3:
        nombre = nombre + "_"

#        for j in i:
#            if len(i) > j:
#             =

        nombre = nombre + i[3]
    nombre = nombre + "_"

print(nombre[:-1])
