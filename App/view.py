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
from time import process_time
from DISClib.ADT import map as mp

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


moviesFile = 'AllMoviesDetailsCleaned.csv'
castingFile ='AllMoviesCastingRaw.csv'


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


        

    #print(lt.size(ids))



def printMenu():
    print("Bienvenido")
    print("1- Iniciar Catalogo")
    print("2- Cargar Peliculas")
    print("3- Encontar buenas peliculas")
    print("0- Salir")

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.iniciarC()
        print(mp.size(cont["movies"]))

    elif int(inputs[0]) == 2:
        t0 = process_time()
        print("Cargando peliculas")
        controller.cargar_datos(cont, moviesFile)
        print("Peliculas cargadas")
        print(mp.size(cont["movies"]))
        t1 = process_time()
        t = t1 -t0
        print("Tiempo de carga de las peliculas, productoras, generos y paises: ", t)
        t2 = process_time()
        controller.cargar_casting(cont, castingFile)
        t3 = process_time()
        tc = t3-t2
        T = tc + t
        print("Tiempo de carga de los directores y actores: ", tc)
        print("Tiempo total: ", T)

    elif int(inputs[0]) == 4:
        nombre = input("Ingrese el nombre de un director: ")
        t0 = process_time()
        ids = controller.ids_peli_director(cont, nombre)
        controller.peliculas_por_director(cont, ids)
        t1 = process_time()
        t = t1-t0
        print("Tiempo de carga: ", t)
    
    elif int(inputs[0]) == 3:
        """
            Econtrar las peliculas y su informacion asociada a una productora de cine
        """
        productora = input('Ingrese el nombre de la productora de cine que desea consultar: ')
        t0 = process_time()

        ''''''''''''''''''''''''''''''''''''''''''
        
        t1 = process_time()
        T= t1-t0
        print("Tiempo de carga: ", T)

    elif int(inputs[0]) == 5:
        """
            Conocer a un actor
        """
        productora = input('Ingrese el nombre de la productora de cine que desea consultar: ')
        t0 = process_time()

        ''''''''''''''''''''''''''''''''''''''''''
        
        t1 = process_time()
        T= t1-t0
        print("Tiempo de carga: ", T)
    
    elif int(inputs[0]) == 6:
        """
            Entender genero cinematografico
        """
        productora = input('Ingrese el nombre de la productora de cine que desea consultar: ')
        t0 = process_time()

        ''''''''''''''''''''''''''''''''''''''''''
        
        t1 = process_time()
        T= t1-t0
        print("Tiempo de carga: ", T)
    
    elif int(inputs[0]) == 7:
        """
            Encontrar peliculas por pais
        """
        productora = input('Ingrese el nombre de la productora de cine que desea consultar: ')
        t0 = process_time()

        ''''''''''''''''''''''''''''''''''''''''''
        
        t1 = process_time()
        T= t1-t0
        print("Tiempo de carga: ", T)
    else:
        sys.exit(0)
sys.exit(0)

# ___________________________________________________
#  Menu principal
# ___________________________________________________
