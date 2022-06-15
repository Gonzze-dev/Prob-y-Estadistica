from openpyxl import Workbook
from PyEstadistica import prob_estadistica as pe
import utili_excel as uex

def mostrar_rango_intrevalo_y_amplitud(lista):
    rango = 50
    cant_intervalos = 7
    lista.sort()
    print('rango: ', pe.get_rango(lista[1], lista[0]) )
    print('cant intervalos: ', pe.get_cant_intervalos(len(lista)) )
    print('amplitud: ', pe.get_amplitud_intervalos(rango, cant_intervalos))

def hacer_todo(texto):
    lista = pe.crear_lista_numeros(texto)
    mostrar_rango_intrevalo_y_amplitud(lista)

    print("\n\n",lista)









