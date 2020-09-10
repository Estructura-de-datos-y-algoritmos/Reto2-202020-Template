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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def compareMoviesIds(id1, id2):
    """
    Compara dos ids de libros
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

'''

def compareGeneros(genero1, genero2):
    print("genero 1 ", genero1 , " genero 2 ", genero2)
    if genero1 == genero2:
        return 0
    return 1
'''

def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    print("CREAR Catalogo...")
    
    catalog = {'movies': None,
               'generos': None,
               'directores':None
          }

    catalog['movies'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['generos'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareGenerosByName)
    
    catalog['directors'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareDirectorsByName)
    '''
    catalog['tags'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compareTagNames)
    catalog['tagIds'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compareTagIds)
    catalog['years'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareMapYear)
    '''


    return catalog




# Funciones para agregar informacion al catalogo

def addMovie(catalog, movie):
    """
    Esta funcion adiciona un libro a la lista de libros,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['movies'], movie)

   
def addMoviesGeneros(catalogo,genero_f,movie):
    generos = catalogo['generos']
    existegenero = mp.contains(generos,genero_f)    
    if existegenero:
        entrada_genero  = mp.get(generos,genero_f)
        el_genero = me.getValue(entrada_genero) 
    else:
        el_genero = newGenro(genero_f)
        mp.put(generos,genero_f, el_genero)

    lt.addLast(el_genero['movies'],movie)

    el_genero['acumulado_vote_count']  = int(el_genero['acumulado_vote_count'])+int(movie['vote_count'])


def addDirectors(catalogo,casting):
    directors = catalogo['directors']
    nombre_director = casting['director_name']
    existedirector = mp.contains(directors,nombre_director)
    if existedirector:
        entrada_director = mp.get(directors,nombre_director) # devuelve la key , value. Key nombre del director, y el value todo el dic del director
        el_director = me.getValue(entrada_director)  # deb deser retorna le valor 
    else:
        el_director = newDirector(casting['director_name']) #crea un nuevo "valor" para key: nombre director
        mp.put(directors,nombre_director,el_director) # mete en el mapa directors, una key con nombre director y valor el_director
    
    el_director['cantidad_peliculas'] = int(el_director['cantidad_peliculas']) +1
    
    lt.addLast(el_director['movies'],casting )

    




    

# ==============================
# Funciones de consulta
# ==============================

def compareGenerosByName(keyname, genero):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    genentry = me.getKey(genero)
    if (keyname == genentry):
        return 0
    elif (keyname > genentry):
        return 1
    else:
        return -1

def compareDirectorsByName(keyname, director):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(director)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def newDirector(nombreDirector):
    """
    Crea una nueva estructura para modelar los directores de una pelicula
    y su promedio de ratings, inicialmente en cero 
    """
    director = {'name': "", "movies": None,  "cantidad_peliculas": 0}
    director['name'] = nombreDirector
    director['movies'] = lt.newList('SINGLE_LINKED', compareDirectorsByName)
    return director


def newGenro(genero_f):

    """
    Crea una nueva estructura para modelar los generos de una pelicula
    y su promedio de ratings, inicialmente en cero 
    """
    genero = {'name': "", "movies": None,  "acumulado_vote_count": 0}
    genero['name'] = genero_f
    genero['movies'] = lt.newList('SINGLE_LINKED', compareGenerosByName)
    return genero


def movieSize(catalogo):
    return lt.size(catalogo['movies'])

def generosSize(catalogo):
    return mp.size(catalogo['generos'])

def directorsSize(catalogo):
    return mp.size(catalogo['directors'])


# ==============================
# Funciones de Comparacion
# ==============================


