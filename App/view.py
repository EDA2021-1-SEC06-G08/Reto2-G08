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
    print("2- Consultar n videos con mas views para un pais y una categoria especifica")
    print("3- Consultar el video mas tendring para un pais")
    print("4- Consultar el video mas tendring para una categoria")
    print("5- Consultar n videos con mas likes para un pais y un tag")
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
        categoriesCargadas(catalog['categories'])

    elif int(inputs[0]) == 2:
        x=0
    elif int(inputs[0]) == 3:
        x=0

    elif int(inputs[0]) == 4:
        print("Cargando informacion de videos...")
        category = input("Introduzca una categoria: ")
        print("Cargando informacion de los videos por pais y categoria...")
        
    elif int(inputs[0]) == 5:
        x=0
    else:
        sys.exit(0)
sys.exit(0)
