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
from DISClib.DataStructures import listiterator as it
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
                'videosCountry':None
                }

    catalog['videos'] = lt.newList('SINGLE_LINKED',
                                       cmpfunction=cmpVideosByViews)
    catalog['categories'] = lt.newList('SINGLE_LINKED',
                                       cmpfunction=comparecategories)
    catalog['videosCategory'] = mp.newMap(100,
                                            maptype='PROBING',
                                            loadfactor= 0.4,
                                            comparefunction=cmpcategory)
    catalog['videosCountry'] = mp.newMap(600,
                                            maptype='PROBING',
                                            loadfactor= 0.4,
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
        videos = me.getValue(entry)
        lt.addLast(videos, video)
        mp.put(catalog['videosCategory'], video['category_id'], videos)
    else:
        entry = mp.get(catalog['videosCategory'], video['category_id'])
        videos = me.getValue(entry)
        lt.addLast(videos, video)
        mp.put(catalog['videosCategory'], video['category_id'], videos)

def addMapVideoCountry(catalog, video):
    """
    Adiciona un country como llave en el map y como value una lista
    que contiene los videos que sean de igual pais
    """
    idEsta = mp.contains(catalog['videosCountry'], video['country'])
    if not(idEsta):
        mp.put(catalog['videosCountry'], video['country'], lt.newList('ARRAY_LIST'))
        entry = mp.get(catalog['videosCountry'], video['country'])
        videos = me.getValue(entry)
        lt.addLast(videos, video)
        mp.put(catalog['videosCountry'], video['country'], videos) 
    else:
        entry = mp.get(catalog['videosCountry'], video['country'])
        videos = me.getValue(entry)
        lt.addLast(videos, video)
        mp.put(catalog['videosCountry'], video['country'], videos)



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

#requerimiento 1
def VideoMasLikes(catalog, country, category):
    idEsta = mp.contains(catalog['videosCountry'], country)
    if idEsta:
        entry = mp.get(catalog['videosCountry'], country)
        videos = me.getValue(entry)
        category_list = lt.newList('ARRAY_LIST')
        iterador = it.newIterator(videos)
        while it.hasNext(iterador):
            elemento = it.next(iterador)
            if comparecategory_video(category, elemento, catalog) == 1:
                lt.addLast(category_list,elemento)
                #tenemos que ordenar category_list por likes 
                category_list1 = sa.sort(category_list, cmpVideosByViews)
    return category_list1


#requerimiento 2 

def video_por_pais(catalog, country):
    paisEsta = mp.contains(catalog['videosCountry'], country)
    if paisEsta:
        entry = mp.get(catalog['videosCountry'], country)
        videos_por_pais = me.getValue(entry)
        videos_por_pais = sa.sort(videos_por_pais, cmpTitle)
        diasValGrande = 0
        diasValPequenio = 0
        videoGrande = None
        videoPequenio = None
        videoAnterior = None
        iterador = it.newIterator(videos_por_pais)
        while it.hasNext(iterador):
            elemento = it.next(iterador)
            title = elemento['title']
            if videoPequenio == None:
                videoPequenio = title
            elif title == videoPequenio:
                diasValPequenio += 1
            else:
                if diasValGrande < diasValPequenio:
                    diasValGrande = diasValPequenio
                    videoGrande = videoAnterior
                diasValPequenio = 1
                videoPequenio = title
            videoAnterior = elemento
        return videoGrande,diasValGrande

def relacionar_id_categorias(category, catalog):
    nombre = ""
    iterador = it.newIterator(catalog['categories'])
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        if category == elemento['id']:
            nombre = elemento['name']
            break
    return nombre

#Requerimiento 3

def TrendingVideoCategory(catalog, category):
    """
    Busca la categoria dentro del map y retorna la lista con los videos de esa categoria.
    Despues compara los titulos de los videos y busca cual es que mas se repite.
    """
    idEsta = mp.contains(catalog['videosCategory'], category)
    if idEsta:
        entry = mp.get(catalog['videosCategory'], category)
        videos = me.getValue(entry)
        videos = sa.sort(videos, cmpTitle)
        diasValGrande = 0
        diasValPequenio = 0
        videoGrande = None
        videoPequenio = None
        videoAnterior = None
        iterador = it.newIterator(videos)
        while it.hasNext(iterador):
            video = it.next(iterador)
            title = video['title']
            if videoPequenio == None:
                videoPequenio = title
            elif title == videoPequenio:
                diasValPequenio += 1
            else:
                if diasValGrande < diasValPequenio:
                    diasValGrande = diasValPequenio
                    videoGrande = videoAnterior
                diasValPequenio = 1
                videoPequenio = title
            videoAnterior = video
        return videoGrande,diasValGrande

#requerimiento 4

def VideosMasLikesTags(catalog, country, tag):
    """
    Busca el pais dentro del map y retorna la lista con los videos de ese pais.
    Despues crea una lista que va a contener los tags y compare si el tag que pasa por
    parametro se encuentra en la lista de tag si es asi introduci el video dentro de la lista
    a retornar.
    Ademas organizar por cantidad de likes.
    """
    idEsta = mp.contains(catalog['videosCountry'], country)
    if idEsta:
        entry = mp.get(catalog['videosCountry'], country)
        videos = me.getValue(entry)
        taglist = lt.newList('ARRAY_LIST')
        iterador = it.newIterator(videos)
        while it.hasNext(iterador):
            video = it.next(iterador)
            lista_tags = video['tags'].split("|")
            tag_entre_comillas = '"' + tag + '"'
            if tag_entre_comillas in lista_tags:
                lt.addLast(taglist, video)
        taglist = sa.sort(taglist, cmpLikes)
        return taglist



# ================================================================
# Funciones utilizadas para comparar elementos dentro de una lista
# ================================================================

def comparecategory_video(category, video, catalog):
    relacion = relacionar_id_categorias(video['category_id'], catalog)
    if category == relacion:
        return 1

def comparecategories(name, category):
    """
    Compara si name se encuentra como category
    """
    if name == category:
        return 0

def cmpTitle(video1, video2):
    return video2['title'] > video1['title']

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
