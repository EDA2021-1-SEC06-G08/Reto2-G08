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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar todos los videos,
    adicionalmente, crea una lista vacia para las categorias. Retorna el catalogo inicializado.
    """
    catalog = {'videos':None,
                'categories':None,
                'videosCategoria':None
                }

    catalog['videos'] = lt.newList('SINGLE_LINKED',
                                       cmpfunction=cmpVideosByViews)
    catalog['categories'] = lt.newList('SINGLE_LINKED',
                                       cmpfunction=comparecategories)
    catalog['videosCategory'] = mp.newMap(40,
                                            maptype='PROBING',
                                            loadfactor=0.5,
                                            comparefunction=comparecategories)
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'],video)

def addCategory(catalog, category):
    """
    Adiciona la categoria a lista de categoria
    """
    t = newCategory(category['name'], category['id'])
    if lt.isPresent(catalog['categories'],t) == 0:
        lt.addLast(catalog['categories'], t)

def addMapVideoCategory(catalog, category):
    idEsta = mp.contains(catalog['videosCategory'], category['id'])
    if not idEsta:
        mp.put(catalog['videosCategory'], category['id'], lt.newList())

def addVideoCategory(catalog, video):
    idCat = video['category_id']
    lista = mp.get(catalog['videosCategory'], idCat)
    lt.addLast(lista, video)
    mp.put(catalog['videosCategory'], idCat, lista)

# Funciones para creacion de datos

def newCategory(name, id):
    """
    Crea una nueva estructura para modelar las categorias 
    """
    category = {'name': '', 'id': ''}
    category['name'] = name
    category['id'] = id
    return category

# Funciones de consulta

def nCategoryVideos(catalog, category):
    video = mp.contains(catalog['videosCategory'], category)
    if video:
        videos = mp.get(catalog['videosCategory'], category)
        return me.getValue(videos)
    return

# Funciones utilizadas para comparar elementos dentro de una lista

def comparecategories(name, category):
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
# Funciones de ordenamiento
