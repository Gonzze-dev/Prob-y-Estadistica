from array import array
from cgitb import text
from cmath import log
from PyEstadistica import prob_estadistica
from openpyxl import Workbook

# book = Workbook()
# sheet = book.active

texto = "10,5 20,2 15,4 11,6 13,8 20,5 14,0 16,5 17,0 12,0 15,4 21,3 22,0 23,1 15,9 16,5 13,0 18,0 16,0 17,3 17,8 19,0 13,4 17,3 14,2 15,0 16,2 19,0 15,5 16,0 "
#contenido = input('insertar numeros: ')

l_numeros = prob_estadistica.crear_lista_numeros(texto)

# print(len(l_numeros))

# for i in range(len(l_numeros)):
#     celda = "A" + str(i+1)
#     sheet[celda] = l_numeros[i]

# book.save('tortas.xlsx')

l_numeros_sin_repetir = prob_estadistica.get_lista_numeros_sin_repetidos(l_numeros)


print()
l_numeros.sort()
print(l_numeros)
print()

rango = prob_estadistica.get_rango_redondeado_de_una_lista(l_numeros, 2)
cant_intervalos = prob_estadistica.get_cant_intervalos_redondeado_de_una_lista(l_numeros, 2)
amplitud = prob_estadistica.get_amplitud_intervalos_redondeado_de_una_lista(l_numeros, 1)
amplitud_sin_redondear = prob_estadistica.get_amplitud_intervalos_de_una_lista(l_numeros)

print("rango: ", rango)
print()
print("cantidad de intervalos: ", cant_intervalos)
print()
print("amplitud: ", amplitud)
print()
print("amplitud sin redondear: ", amplitud_sin_redondear)
print()


tabla = prob_estadistica.get_tabla_intervalos(l_numeros, amplitud)



for fila in tabla:
    print(fila)