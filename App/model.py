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
# API del TAD Catalogo de Peliculas
# -----------------------------------------------------

def newCatalog():

  #  print("CREAR Catalogo...")
    
    catalog = {'movies': None,
               'directores': None
          }

    catalog['movies'] = lt.newList('SINGLE_LINKED', compareMoviesIds)
    catalog['directores'] = mp.newMap(100000,
                                      maptype ='PROBING', 
                                      loadfactor= 0.4, 
                                      comparefunction= compareDirectorsByName)
    return catalog

def Addpeli(catalog, row):
    
    lt.addLast(catalog["movies"], row)
    #CHAINING
    #PROBING

def Addcasting(catalog, row):
    directores = catalog["directores"]
    nombre_director = row["director_name"]
    existe = mp.contains(directores, nombre_director)
    if existe:
        llave_valor = mp.get(directores, nombre_director)
        valor = me.getValue(llave_valor)
        lt.addLast(valor, row["id"])
    else:
        lista = lt.newList('ARRAY_LIST')
        lt.addLast(lista, row["id"])
        mp.put(directores, nombre_director, lista)




# Funciones para agregar informacion al catalogo



# ==============================
# Funciones de consulta
# ==============================

def tamano(catalog):
    return mp.size(catalog["directores"])


def peli_director(catalog, nombre):
    llavev = mp.get(catalog["directores"], nombre)
    peliculas = me.getValue(llavev)
    return peliculas

# ==============================
# Funciones de Comparacion
# ==============================

def compareMoviesIds(id1, id2):
    #print("ESTE ES EL ELEMENTO 1!!!", id1)
    #print("DOS", id2)

    if id1 == id2["\ufeffid"]:
        return 0
    else:
        return 1

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

