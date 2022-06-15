from math import log
from operator import contains
from webbrowser import get


class prob_estadistica:

    def __detectarSeparador(texto):
        formaNumeros = [ "0", "1", "2", "3", "4", "5", 
                        "6", "7", "8", "9", ".", ","]
        separador = ""

        
        for i in range(0, len(texto)):
            if((texto[i] not in formaNumeros)
                or texto[i:i+2] == ", "):
                    k = i

                    while(texto[k] not in formaNumeros or texto[k:k+2] == ", " ):
                        separador = separador + texto[k]
                        k += 1
                    
                    return separador
                

    @staticmethod
    def __adaptar_texto(texto: str):
        separador = prob_estadistica.__detectarSeparador(texto)
        return texto.replace(separador, " ")

    @staticmethod
    def crear_lista_numeros(texto):
        numero_str = ""
        lista_numeros = list()
        texto = prob_estadistica.__adaptar_texto(texto)
        for i in range(len(texto)):

            if(not (texto[i] == " ")):
                if(texto[i] == ","):
                    numero_str = numero_str + "."
                elif (not texto[i] == '.'):
                    numero_str = numero_str + texto[i]
            else:
                lista_numeros.append(float(numero_str))
                numero_str = ""
        
        return lista_numeros

    @staticmethod
    def get_rango(Rmax, Rmin):
        return Rmax - Rmin

    @staticmethod
    def get_rango_redondeado(Rmax, Rmin, decimales_significativos):
        return round(Rmax - Rmin, decimales_significativos)

    @staticmethod
    def get_cant_intervalos(n):
        return 1 + (3.3 * log(n, 10))

    @staticmethod
    def get_cant_intervalos_redondeado(n, decimales_significativos):
        return 1 + round((3.3 * log(n, 10)), decimales_significativos)

    @staticmethod
    def get_amplitud_intervalos(rango, cant_intervalos):
        return rango/cant_intervalos

    @staticmethod
    def get_amplitud_intervalos_redondeado(rango, cant_intervalos):
        return round(rango/cant_intervalos, cant_intervalos)

    @staticmethod
    def get_rango_de_una_lista(lista_numeros):
        lista_numeros.sort()

        return lista_numeros[-1] - lista_numeros[0]

    @staticmethod
    def get_rango_redondeado_de_una_lista(lista_numeros, decimales_significativos):
        lista_numeros.sort()

        return round(lista_numeros[-1] - lista_numeros[0], decimales_significativos)

    @staticmethod
    def get_cant_intervalos_de_una_lista(lista_numeros):
        return 1 + (3.3 * log(len(lista_numeros), 10))

    @staticmethod
    def get_cant_intervalos_redondeado_de_una_lista(lista_numeros, decimales_significativos):
        return round(1 + (3.3 * log(len(lista_numeros), 10)), decimales_significativos)

    @staticmethod
    def get_amplitud_intervalos_de_una_lista(lista_numeros):
        rango = prob_estadistica.get_rango_de_una_lista(lista_numeros)
        cant_intervalos = prob_estadistica.get_cant_intervalos_de_una_lista(lista_numeros)

        return rango/cant_intervalos

    @staticmethod
    def get_amplitud_intervalos_redondeado_de_una_lista(lista_numeros, decimales_significativos):
        rango = prob_estadistica.get_rango_redondeado_de_una_lista(lista_numeros, decimales_significativos)
        cant_intervalos = prob_estadistica.get_cant_intervalos_redondeado_de_una_lista(lista_numeros, decimales_significativos)

        return round(rango/cant_intervalos, decimales_significativos)

    @staticmethod
    def get_lista_numeros_sin_repetidos(lista_numeros):
        lista_numeros_sin_repetir = list()
        
        for numero in lista_numeros:
            if not contains(lista_numeros_sin_repetir, numero):
                lista_numeros_sin_repetir.append(numero)
        
        return lista_numeros_sin_repetir

    @staticmethod
    def __get_condicion_intervalo(lista, indice_lista, superior):
        condicion_fin = False

        if(indice_lista < len(lista)):
                condicion_fin = lista[indice_lista] < superior
        else:
                condicion_fin = lista[indice_lista] <= superior
        
        return condicion_fin

    @staticmethod
    def get_tabla_intervalos(lista, amplitud):
        lista_numeros_sin_repetir = prob_estadistica.get_lista_numeros_sin_repetidos(lista)
        lista_intervalos = list()
        tabla_intervalos = list()
        numero_inicial = lista_numeros_sin_repetir[0]
        lista_numeros_sin_repetir.sort()
        indice_lista_numeros = 0
        condicion_fin = False

        while(numero_inicial <= (lista_numeros_sin_repetir[-1] + amplitud)):
            lista_intervalos.append(numero_inicial)
            numero_inicial += amplitud
        
        for i in range(len(lista_intervalos)-1):
            cantidad_numeros_en_un_intervalo = 0

            inferior = lista_intervalos[i]
            superior = lista_intervalos[i+1]
            
            while((indice_lista_numeros < len(lista))
                    and ((lista[indice_lista_numeros] >= inferior) 
                        and (prob_estadistica.__get_condicion_intervalo(lista, indice_lista_numeros, superior)))):

                cantidad_numeros_en_un_intervalo += 1
                indice_lista_numeros += 1
                

            tabla_intervalos.append({"inferior": round(inferior, 2), 
                                     "superior": round(superior, 2), 
                                     "cantidad": cantidad_numeros_en_un_intervalo})

        return tabla_intervalos


