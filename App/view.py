"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("0- Para salir del programa")
    print("1- Cargar información en el catálogo")
    print("2- Consultar n videos con mas views para un pais y una categoria especifica")
    print("3- Consultar el video mas tendring para un pais")
    print("4- Consultar el video mas tendring para una categoria")
    print("5- Consultar n videos con mas likes para un pais y un tag")

def initCatalog():
    """
    Inicializa el catalogo de libros con el tipo Single List
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)

def categoriesCargadas(categories):
    """
    Imprime las categorias cargadas
    """
    size = lt.size(categories)
    i=1
    print('Las categorias son: ')
    while i <= size:
        category = lt.getElement(categories,i)
        print(category['id'] + " " + category['name'])
        i+=1

#requerimiento 1
def trendingVideoCountry (catalog, country): 
    return controller.video_mas_trending_pais(catalog, country)

def TrendingVideoC(catalog, country):
    """
    Retorna la informacion del video desglozada
    """
    video = trendingVideoCountry(catalog, country)
    print('El titulo es: ' + video[0]['title'])
    print('El nombre del canal es: ' + video[0]['channel_title'])
    print('El país es: ' + video[0]['country'])
    print('La cantidad de dias que fue trending es: ' + str(video[1]))


def nVideosViews(videos,n):
    """
    Retorna los n primeros videos con mas views 
    """
    size = lt.size(videos)
    print('Los videos son: ')
    if size > n:
        i=1
        while i <=n:
            video = lt.getElement(videos, i)
            print('El titulo es: ' + video['title'])
            print('La trending date es: ' + video['trending_date'])
            print('El canal es: ' + video['channel_title'])
            print('La fecha de publicacion es: ' + video['publish_time'])
            print('Las views son: ' + video['views'])
            print('Los likes son: ' + video['likes'])
            print('Los dislikes son: ' + video['dislikes'])
            i+=1



def TrendingVideo(catalog, category):
    """
    Retorna la informacion del video desglozada
    """
    video = TrendingVideoCategory(catalog, category)
    print('El titulo es: ' + video[0]['title'])
    print('El nombre del canal es: ' + video[0]['channel_title'])
    print('La categoria es: ' + video[0]['category_id'])
    print('La cantidad de dias que fue trending es: ' + str(video[1]))

# requerimiento 4

def VideosMasLikesTags(catalog, country, tag):
    """
    Retorna la lista con los videos organizados por likes
    """
    return controller.VideosMasLikesTags(catalog, country, tag)

def nVideosLikes(videos, n):
    """
    Retorna los n primeros videos con mas likes
    """
    size = lt.size(videos)
    print('Los videos son: ')
    if size > n:
        i=1
        while i <=n:
            video = lt.getElement(videos, i)
            print('El titulo es: ' + video['title'])
            print('El canal es: ' + video['channel_title'])
            print('La fecha de publicacion es: ' + video['publish_time'])
            print('Las viewes son: ' + video['views'])
            print('Los likes son: ' + video['likes'])
            print('Los dislikes son: ' + video['dislikes'])
            print('Los tags son: ' + video['tags'])
            i+=1


catalog = None

"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        print('Videos cargados ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas ' + str(lt.size(catalog['categories'])))
        categoriesCargadas(catalog['categories'])
    elif int(inputs[0]) == 2:
        pais = input("Introduzca un pais: ")
        category = input("Introduzca una categoria: ")
        print("Cargando informacion de los videos con más likes por país y categoría...")
        respuesta = controller.VideoMasLikes(catalog, pais, category)
        print(respuesta)
        n = int(input("Introduzca la cantidad de videos con mas views: "))
        print("Cargando informacion de los", n, "videos con más views por país y categoría...")
        lista = controller.VideoMasLikes(catalog, pais, category)
        nVideosViews(lista, n)
    elif int(inputs[0]) == 3:
        pais = input("Introduzca un pais: ")
        print("Cargando informacion del video más trending en", pais)
        TrendingVideoC(catalog, pais)

    elif int(inputs[0]) == 4:
        category = input("Introduzca una categoria: ")
        print("Cargando informacion de los videos por categoria...")
        TrendingVideo(catalog, category)
    elif int(inputs[0]) == 5:
        country = input("Introduzca un pais: ")
        tag = input("Introduzca un tag: ")
        n = int(input("Introduzca la cantidad de videos con mas likes: "))
        print("Cargando informacion de los videos por tag y pais")
        videos = VideosMasLikesTags(catalog, country, tag)
        nVideosLikes(videos, n)
    else:
        sys.exit(0)
sys.exit(0)
