from openpyxl import Workbook
from PyEstadistica import prob_estadistica as pe

def pasar_a_excel(book : Workbook, sheet, lista, nombreArchivo):
    for i in range(len(lista)):
        celda = "A" + str(i+1)
        sheet[celda] = lista[i]

        book.save(nombreArchivo)

def crear_ordenar_guardar(book : Workbook, sheet,texto_lista, nombreArchivo):
    lista = pe.crear_lista_numeros(texto_lista)
    lista.sort()
    pasar_a_excel(book, sheet, lista, nombreArchivo)