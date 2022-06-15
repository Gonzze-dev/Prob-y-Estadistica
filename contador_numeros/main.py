from cgitb import text
from openpyxl import Workbook
from PyEstadistica import prob_estadistica as pe
import utili_excel as uex
import utili_lista as ulista

book = Workbook()
sheet = book.active

texto = ("4,5 ; 10 ; 6 ; 10 ; 6,5 ; 8 ; 11 ; 11,5 ; 10,5 ; 8 ; 7 ; 9,5 ; 11,5 ; 9 ; 5 ; 10 ; 5 ; 10,5 ; 6,5 ; 3,5 ; 10 ; 10 ; 6 ; 10,5 ; 9. 2 ")

uex.crear_ordenar_guardar(book, sheet, texto, "negocio")
ulista.hacer_todo(texto)