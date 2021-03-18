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
    print("1- Cargar información en el catálogo")
    print("2- Consultar videos con mas Likes para una categoria especifica")
    print("0- Salir del menu")

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

def nCategoryVideos(catalog, category):
    return controller.nCategoryVideos(catalog, category)

def nOrganizador(videos, n):
    """
    Retorna los n primeros videos
    """
    size = lt.size(videos)
    print('Los videos son: ')
    if size > n:
        i=1
        while i <= n:
            video = lt.getElement(videos)
            print('El titulo es: ' + video['title'])
            print('El canal es: ' + video['channel_title'])
            print('La fecha de trending es: ' + video['trending_date'])
            print('La fecha de publicacion es: ' + video['publish_time'])
            print('Las viewes son: ' + video['views'])
            print('Los likes son: ' + video['likes'])
            print('Los dislikes son: ' + video['dislikes'])
            print('')
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
        catalog = initCatalog()
        loadData(catalog)
        print('Videos cargados ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas ' + str(lt.size(catalog['categories'])))
    elif int(inputs[0]) == 2:
        categoria = input("Introduzca una categoria: ")
        print("Cargando informacion de los videos por pais y categoria...")
        videos = nCategoryVideos(catalog, categoria)
        n = int(input("Introduzca la cantidad de videos: "))
        nOrganizador(videos, n)
    else:
        sys.exit(0)
sys.exit(0)
