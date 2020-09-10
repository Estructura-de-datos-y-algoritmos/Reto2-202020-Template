"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


moviesFile = 'SmallMoviesDetailsCleaned.csv'
castingFile ='MoviesCastingRaw-small.csv'


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________
def dar_datos(peliculas):
    primera = lt.getElement(peliculas, 1)
    print("Primera Pelicula\n")
    print("     Titulo: ", primera["original_title"])
    print("     Fecha de estreno: ", primera["release_date"])
    print("     Promedio de votación: ", primera["vote_average"])    
    print("     Numero de votos: ", primera["vote_count"])
    print("     Idioma: ", primera["original_language"],"\n")
    
    primera = lt.getElement(peliculas, peliculas["size"])
    print("Ultima Pelicula\n")
    print("     Titulo: ", primera["original_title"])
    print("     Fecha de estreno: ", primera["release_date"])
    print("     Promedio de votación: ", primera["vote_average"])    
    print("     Numero de votos: ", primera["vote_count"])
    print("     Idioma: ", primera["original_language"],"\n")



def printMenu():
    print("Bienvenido")
    print("1- Iniciar Catalogo")
    print("2- Cargar Peliculas")
    print("0- Salir")

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.iniciarC()
        print(lt.size(cont["movies"]))

    elif int(inputs[0]) == 2:
        print("Cargando peliculas")
        controller.cargar_datos(cont, moviesFile)
        print("Peliculas cargadas")
        print(lt.size(cont["movies"]))
        dar_datos(cont["movies"])

    else:
        sys.exit(0)
sys.exit(0)

# ___________________________________________________
#  Menu principal
# ___________________________________________________
