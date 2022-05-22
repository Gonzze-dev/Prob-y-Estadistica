from openpyxl import Workbook
from PyEstadistica import prob_estadistica

book = Workbook()
sheet = book.active

lista = ("16.500 – 10.050 – 12.320 – 10.000 – 22.540 – 7.325 – 13.800 – 14.600 –"
+ " 25.000 – 17.085 – 19.000 – 11.900 – 13.760 – 15.075 – 20.210 – 7.280 –"
+ " 21.200 – 23.090 – 24.500 – 15.800 – 5.000 – 13.050 – 21.600 – 17.700 ")

l_numeros = prob_estadistica.crear_lista_numeros(lista)
l_numeros.sort()

print('rango: ', prob_estadistica.get_rango(l_numeros[1], l_numeros[0]) )
print('cant intervalos: ', prob_estadistica.get_cant_intervalos(len(l_numeros)) )

for i in range(len(l_numeros)):
    celda = "A" + str(i+1)
    sheet[celda] = l_numeros[i]

book.save('negocio.xlsx')