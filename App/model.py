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
from DISClib.DataStructures import listiterator as it
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
               'productores': None,
               'pais': None,
               'genre':None,
               'directores':None,
               'actores':None,
          }

    catalog['movies'] = mp.newMap(329100, maptype='CHAINING', loadfactor=1,comparefunction=compareMoviesIds    )
    catalog['productores']= mp.newMap(200000, maptype='CHAINING', loadfactor=1,comparefunction=comparar_productoras)
    catalog['pais']=mp.newMap(200000, maptype='CHAINING', loadfactor=1,comparefunction=comparar_pais    )
    catalog['genre']=mp.newMap(200000, maptype='CHAINING', loadfactor=1,comparefunction=comparar_genero   )
    catalog['actores']=mp.newMap(200000, maptype='CHAINING', loadfactor=1,comparefunction=comparar_actor    )
    catalog['directores'] = mp.newMap(200000,
                                      maptype ='CHAINING', 
                                      loadfactor= 1, 
                                      comparefunction= compareDirectorsByName)
    return catalog

def Addpeli(catalog, row):
    peliculas = catalog['movies']
    id_pelicula= row["\ufeffid"]
    existe = mp.contains(peliculas,id_pelicula)
    if existe:
       return print('id repetido / imposible')
    else:
        informacion_pelicula={}
        informacion_pelicula["original_title"]=row["original_title"]
        informacion_pelicula["vote_count"]=row["vote_count"]
        mp.put(peliculas,id_pelicula,informacion_pelicula)



def Add_productora(catalog,row):
    productores = catalog["productores"]
    nombre_productor = row["production_companies"]
    existe = mp.contains(productores, nombre_productor)
    if not existe:
        elementos_consultar={}
        elementos_consultar["todas_peliculas"]=[row["original_title"]]
        elementos_consultar["num_peliculas"]=1
        elementos_consultar["num_vote"]=float(row["vote_count"])
        mp.put(productores,nombre_productor,elementos_consultar)
    elif existe:
        llave_valor = mp.get(productores, nombre_productor)
        valor = me.getValue(llave_valor)
        valor["todas_peliculas"].append(row["original_title"])
        valor["num_peliculas"]+=1
        valor["num_vote"]+=float(row["vote_count"])
        mp.put(productores,nombre_productor,valor)


def Add_pais(catalog,row):
    paises=catalog["pais"]
    nombre_pais = row["production_countries"]
    existe = mp.contains(paises,nombre_pais)
    if not existe:
        informacion_pais={}
        informacion_pais["informacion_pelicula"]=[(row["original_title"],row["release_date"])]
        mp.put(paises,nombre_pais,informacion_pais)
    elif existe:
        llave_valor= mp.get(paises,nombre_pais)
        informacion_pais=me.getValue(llave_valor)
        informacion_pais["informacion_pelicula"].append((row["original_title"],row["release_date"]))
        mp.put(paises,nombre_pais,informacion_pais)
    

def Add_genero(catalog,row):
    tabla_generos=catalog["genre"]
    nombres_generos=row["genres"]
    nombres_generos.split("|")
    for genero in nombres_generos:
        existe=mp.contains(tabla_generos,genero)
        if not existe:
            elementos_consultar={}
            elementos_consultar["todas_peliculas"]=[row["original_title"]]
            elementos_consultar["num_peliculas"]=1
            elementos_consultar["num_vote"]=float(row["vote_count"])
            mp.put(tabla_generos,genero,elementos_consultar)
        elif existe:
            llave_valor = mp.get(tabla_generos, genero)
            valor = me.getValue(llave_valor)
            valor["todas_peliculas"].append(row["original_title"])
            valor["num_peliculas"]+=1
            valor["num_vote"]+=float(row["vote_count"])
            mp.put(tabla_generos,genero,valor)

def Add_actor(catalog,row):
    lista_actores=catalog["actores"]
    for num_actor in range(1,6):
        actor="actor{num}_name".format(num=num_actor)
        nombre_actor=row[actor]
        existe=mp.contains(lista_actores,nombre_actor)
        if not existe:
            lista_ids = lt.newList('ARRAY_LIST')
            lt.addLast(lista_ids, row["id"])
            colaboraciones={}
            colaboraciones[row["director_name"]]=1
            informacion_actor=[lista_ids,colaboraciones]
            mp.put(lista_actores, nombre_actor, informacion_actor)
        elif existe:
            llave_valor = mp.get(lista_actores, nombre_actor)
            valor = me.getValue(llave_valor)
            lt.addLast(valor[0], row["id"])
            if row["director_name"] in valor[1]:
                valor[1][row["director_name"]]+=1
            elif not row["director_name"] in valor[1]:
                valor[1][row["director_name"]]=1
            

            

def Add_director(catalog, row):
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


def ids_peli_director(catalog, nombre):
    llavev = mp.get(catalog["directores"], nombre)
    lista_ids = me.getValue(llavev)
    return lista_ids

def buscar_ids_peliculas(cont, ids):
    itera = it.newIterator(ids)
    tabla_pelicula = cont["movies"]
    suma_votos=0
    nombres_peliculas=[]
    numero_peliculas=0
    while it.hasNext(itera):
        
        ID = it.next(itera)
        Nombre_director=mp.get(tabla_pelicula,ID)
        informacion_director=mp.getValue(Nombre_director)
        suma_votos+=float(informacion_director["vote_count"])
        nombres_peliculas.append(informacion_director["original_title"])
        numero_peliculas+=1
    print(nombres_peliculas)
    print(suma_votos/numero_peliculas)
    print(numero_peliculas)

def peliculas_por_actor(cont,ids):
    return print("corregir")  


# ==============================
# Funciones de Comparacion
# ==============================

def compareMoviesIds(keyname, ids):

    authentry = me.getKey(ids)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
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

def comparar_productoras(keyname,productor):
    authentry = me.getKey(productor)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def comparar_pais(keyname,pais):
    authentry = me.getKey(pais)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def comparar_genero(keyname,genero):
    authentry = me.getKey(genero)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1


def comparar_actor(keyname,actor):
    authentry = me.getKey(actor)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1
