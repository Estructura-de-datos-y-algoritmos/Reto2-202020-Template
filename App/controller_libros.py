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

import config as cf
from App import model_libros
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model_libros.newCatalog()
    return catalog


def loadData(catalogo, moviesFie,castingFile):
    loadMovies(catalogo,moviesFie)
    loadCasting(catalogo,castingFile)


def loadCasting(catalogo,castingFile):
    castingFile = cf.data_dir + castingFile
    #print("ESTa es casting ..", castingFile)

    dialect = csv.excel()
    dialect.delimiter=";"

  
    input_file = csv.DictReader(open(castingFile,encoding="utf-8"),dialect=dialect)
    for casting in input_file:
        model_libros.addDirectors(catalogo,casting)




def loadMovies(catalogo,moviesFie):
    moviesFie = cf.data_dir + moviesFie
    #print("ESTa es la pelicula ..", moviesFie)

    dialect = csv.excel()
    dialect.delimiter=";"

  
    input_file = csv.DictReader(open(moviesFie,encoding="utf-8"),dialect=dialect)

    for movie in input_file:
        #print("movieee \n",movie)
        #print("primer genero ",movie['genres'])
        #break
        model_libros.addMovie(catalogo, movie)
        generos = movie['genres'].split("|")
        for gen in generos:
            model_libros.addMoviesGeneros(catalogo,gen.strip(),movie)


  

def movieSize(catalogo):
     return model_libros.movieSize(catalogo)


def generosSize(catalogo):
    return model_libros.generosSize(catalogo)

def directorsSize(catalogo):
    return model_libros.directorsSize(catalogo)

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
