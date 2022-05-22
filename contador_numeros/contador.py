from openpyxl import Workbook
from PyEstadistica import prob_estadistica


book = Workbook
sheet = book.active

texto = ("16.500 – 10.050 – 12.320 – 10.000 – 22.540 – 7.325 – 13.800 – 14.600 –"
+ " 25.000 – 17.085 – 19.000 – 11.900 – 13.760 – 15.075 – 20.210 – 7.280 –"
+ " 21.200 – 23.090 – 24.500 – 15.800 – 5.000 – 13.050 – 21.600 – 17.700 ")


#print(l_numeros)

# print(len(l_numeros))

# for i in range(len(l_numeros)):
#     celda = "A" + str(i+1)
#     sheet[celda] = l_numeros[i]

# book.save('tortas.xlsx')

# l_numeros_sin_repetir = prob_estadistica.get_lista_numeros_sin_repetidos(l_numeros)


# print()
# l_numeros.sort()
# print(l_numeros)
# print()

# rango = prob_estadistica.get_rango_redondeado_de_una_lista(l_numeros, 2)
# cant_intervalos = prob_estadistica.get_cant_intervalos_redondeado_de_una_lista(l_numeros, 2)
# amplitud = prob_estadistica.get_amplitud_intervalos_redondeado_de_una_lista(l_numeros, 1)
# amplitud_sin_redondear = prob_estadistica.get_amplitud_intervalos_de_una_lista(l_numeros)

# print("rango: ", rango)
# print()
# print("cantidad de intervalos: ", cant_intervalos)
# print()
# print("amplitud: ", amplitud)
# print()
# print("amplitud sin redondear: ", amplitud_sin_redondear)
# print()


# tabla = prob_estadistica.get_tabla_intervalos(l_numeros, amplitud)



# for fila in tabla:
#     print(fila)

