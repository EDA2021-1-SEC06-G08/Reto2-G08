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
 """

import config as cf
import model
import csv
import tracemalloc
import time

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# =====================================
# Inicialización del Catálogo de libros
# =====================================



def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo en modo ARRA_LIST.
    """
    catalog = model.newCatalog()
    return catalog



# ================================
# Funciones para la carga de datos
# ================================


def loadData(catalog):
    """
    Carga los datos de los archivos y carga los datos en la 
    estructura datos
    """
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    loadVideos(catalog)
    loadCategories(catalog)
    
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)
    return delta_time, delta_memory

def loadVideos(catalog):
    """
    Carga los videos del archivo. Por cada video se toma su categoria y por
    cada una de ellas, se crea en la lista de categorias, a dicha categoria 
    una referencia al video que se esta procesando.
    """
    videosfile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding = "utf8", errors="ignore"))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategories(catalog):
    """
    Carga todas las categorias del archivo y las agrega a la lista de categorias
    """
    categoriesfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(categoriesfile,encoding = "utf8", errors="ignore"))
    for category in input_file:
        model.addCategory(catalog, category)



# =======================================
# Funciones de consulta sobre el catálogo
# =======================================


#requerimiento 1
def VideoMasLikes (catalog, country, category):
    return model.VideoMasLikes(catalog, country, category)

#requerimiento 2 
def video_mas_trending_pais(catalog, country):
    return model.video_mas_trending_pais(catalog, country)
# requerimiento 3

def TrendingVideoCategory(catalog, category):
    """
    Contiene la informacion del video mas trendring por category que es pasada como parametro
    y la cantidad de dias que fue trending
    """
    return model.TrendingVideoCategory(catalog, category)

# requerimiento 4

def VideosMasLikesTags(catalog, country, tag):
    """
    Contiene los videos organizados por likes
    """
    return model.VideosMasLikesTags(catalog, country, tag)


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
