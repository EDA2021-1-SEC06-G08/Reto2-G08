"""
 * Copyright 2020, Departamento de sistemas y Computación,
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import quicksort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


# =======================
# Construccion de modelos
# =======================


def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar todos los videos,
    adicionalmente, crea una lista vacia para las categorias. Retorna el catalogo inicializado.
    """
    catalog = {'videos':None,
                'categories':None,
                'videosCategory':None,
                'videosCountry':None,
                'videosTag':None
                }

    catalog['videos'] = lt.newList('SINGLE_LINKED',
                                       cmpfunction=cmpVideosByViews)
    catalog['categories'] = lt.newList('SINGLE_LINKED',
                                       cmpfunction=comparecategories)
    catalog['videosCategory'] = mp.newMap(100,
                                            maptype='PROBING',
                                            loadfactor=0.4,
                                            comparefunction=cmpcategory)
    catalog['videosCountry'] = mp.newMap(800,
                                            maptype='PROBING',
                                            loadfactor=0.4,
                                            comparefunction=cmpcountry)
    return catalog



# ==============================================
# Funciones para agregar informacion al catalogo
# ==============================================


def addVideo(catalog, video):
    """
    Se adiciona el video a la lista de videos
    """
    lt.addLast(catalog['videos'],video)
    addMapVideoCategory(catalog, video)
    addMapVideoCountry(catalog, video)

def addCategory(catalog, category):
    """
    Adiciona la categoria a lista de categoria
    """
    t = newCategory(category['name'], category['id'])
    if lt.isPresent(catalog['categories'],t) == 0:
        lt.addLast(catalog['categories'], t)

def addMapVideoCategory(catalog, video):
    """
    Adiciona una category como llave en el map y como value una lista 
    que contiene los videos que sean de igual category
    """
    idEsta = mp.contains(catalog['videosCategory'], video['category_id'])
    if not(idEsta):
        mp.put(catalog['videosCategory'], video['category_id'], lt.newList('ARRAY_LIST'))
        entry = mp.get(catalog['videosCategory'], video['category_id'])
        lista = me.getValue(entry)
        lt.addLast(lista, video)
        mp.put(catalog['videosCategory'], video['category_id'], lista)
    else:
        entry = mp.get(catalog['videosCategory'], video['category_id'])
        lista = me.getValue(entry)
        lt.addLast(lista, video)
        mp.put(catalog['videosCategory'], video['category_id'], lista)

def addMapVideoCountry(catalog, video):
    """
    Adiciona un country como llave en el map y como value una lista
    que contiene los videos que sean de igual pais
    """
    idEsta = mp.contains(catalog['videosCountry'], video['country'])
    if not(idEsta):
        mp.put(catalog['videosCountry'], video['country'], lt.newList('ARRAY_LIST'))
        entry = mp.get(catalog['videosCountry'], video['country'])
        lista = me.getValue(entry)
        lt.addLast(lista, video)
        mp.put(catalog['videosCountry'], video['country'], lista) 
    else:
        entry = mp.get(catalog['videosCountry'], video['country'])
        lista = me.getValue(entry)
        lt.addLast(lista, video)
        mp.put(catalog['videosCountry'], video['country'], lista)



# ================================
# Funciones para creacion de datos
# ================================


def newCategory(name, id):
    """
    Crea una nueva estructura para modelar las categorias 
    """
    category = {'name': '', 'id': ''}
    category['name'] = name
    category['id'] = id
    return category



# =====================
# Funciones de consulta
# =====================





# ================================================================
# Funciones utilizadas para comparar elementos dentro de una lista
# ================================================================


def comparecategories(name, category):
    """
    Compara si name se encuentra como category
    """
    if name == category:
        return 0

def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
     Args:
        video1: informacion del primer video que incluye su valor 'views'
        video2: informacion del segundo video que incluye su valor 'views'
    """
    return int(video1['views']) > int(video2['views'])

def cmpLikes(video1, video2):
    """
    Devuelve verdadero (True) si los 'likes' del video1 son menos que los del video2
     Args:
        video1: informacion del primer video que incluye su valor 'views'
        video2: informacion del segundo video que incuye su valor 'views'
    """
    return int(video1['likes']) > int(video2['likes'])

def cmpcategory(category, catalog):
    """
    Compara si la category del video es igual a alguna llave
    """
    categoryentry = me.getKey(catalog)
    if category == categoryentry:
        return 0
    elif category > categoryentry:
        return 1
    else: 
        return -1

def cmpcountry(country, catalog):
    """
    Compara si el country del video es igual a alguna llave
    """
    countryentry = me.getKey(catalog)
    if country == countryentry:
        return 0
    elif country > countryentry:
        return 1
    else:
        return -1