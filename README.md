# ProyectoIndividualML

# ProyectoIndividualML - Trabajo como Data Scientist en Steam, una plataforma multinacional de videojuegos.
# Proyecto MLOps: Sistema de Recomendación de Videojuegos  🎮

**Objetivo Principal**🎯
Desarrollar un sistema de recomendación de videojuegos para la plataforma Steam. Con el fin de mejorar la experiencia de los usuarios al sugerir juegos relevantes y atractivos

> # 1. Extracción, transformación 🧹| Análisis Exploratorio de Datos|📈 
Objetivo: Limpiar y preprocesar los archivos brindados, con datos iniciales no estructurados, comprender las relaciones entre las variables, para que sean aptos para el análisis, posteiror realización de las funciones y entrenamiento del modelo

Dificultades: Los archivos eran muy pesados,  en formato jason.gzip, con datos anidados, alto porcentaje de None y Nan, símbolos, lo que dificultaba su manipulación, extracción, transformación y su análisis.
(ETL)
En los tres casos, los archivos se encuentran en formato JSON comprimidos en .gz,  los cuales fueron descomprimidos antes de ser cargados a Python.
Se hizo una exploración exhaustiva de los tres archivos para entender la estructura de los datos. Luego cada uno fue transformado en un Data Frame, para una mejor exploración y entendimiento de la situación, y toma de desición de tratamiento a implementar.
En consecuencia se determinó realizar pequeños DF para ser funcionales y trabajar con archivos de mejor manipulación en tamaño para cada función, para lo cual, se comenzó por definir las columnas requeridas. Seguidamente se desanidaron las columnas con datos considerados necesarios. En todos los casos una vez creado el nuevo Data Frame , se realizó una limpieza general (contar nulos, duplicados, datos unicos, en la mayoría de los casos los nan fueron reemplazados por o y duplicados eliminados), sumado a transformaciones y análisis específicos de cada DF que se aclararán a continuación, aquellos que se consideran relevantes. Una vez concluidos los procedimeintos mencionados, fueron reducidos en un 50%, previendo su carga futura y guardados en formato csv.

**Descripcón de particularidades por archivo** 🌟

**User_eviews**: se extrajeron las columnas necesarias para crear un nuevo DF bajo en nombre **df_original**para trabajar las funciones 1 y 2, para lo cual se procedió a la verificación y limpieza de nulos, Nan, duplicados, luego se dividió la columna 'posted' en nuevas columnas de día, mes y año, se sumó un dígito a día y se redujo nuevamente a una sola columna "Fecha", la cual contiene (año, mes, día) en formato Str. La columna "recomended" originalmente conteniá valores booleanos, siendo reemplazada por int. donde true = 1 y false = o

**Steam_games**: para la función 1 se creó el DF denominado: **df_new_game_copy**, mediante la selección de las columnas: "price", "items_count", "user_id", convertiendo los datos en  "price" y "items_count" a tipo float y los "None" por 0 para evitar errores a la hora de contarlos o sumar como también una mejor interpretación de los datos.
Se crea el DF **df_new_game_copy**, para realizar la función 3 y 4. Se procede a desanidar la columna "genre",  extrayendo los valore en columnas separadas para cada género. Luego se concatenan las columnas desanidadas de "genre" con el DF inicial. Finalmente se crea una función  para rellenar los valores NaN en 'user_id' con valores aleatorios,  si 'app_name' no es NaN. 
Para trabajar la función 5 se creó el DF **df_funcion5**, comenzando del archivo original se seleccionaron las columnas: release_date,	developer, y	price	items_count. Se filtran los datos en la columna price para visualizar la cantidad de  veces que aparecen: 'Free to Play', 'Free To Play', 'Free'. Por otra parte , se extrae los primeros 4 caracteres de la columna 'release_date' y se crea una nueva columna 'year'

**User_items**:
para la realización de la función 3 y 4  se trabajó en la creación del DF **df_items_ph3**. Donde se procedió a desanidar la columna "item" para extraer: item_id,	item_name,	playtime_forever	y playtime_2weeks. Allí, playtime_forever se convierte a float y se crea una nueva columna 'playtime_hours' que permite visualizar el tiempo en  horas.
Posteriormente se hizo un merge en pandas, para combinar dos DataFrames(**df_new_games_copy, df_items_ph3**) para lograr el DF adecuado para trabajar la funcion 3 y 4 denominado df_fusion3. Logrado simplificar la manipulación de los datos mediante con las columnas elegidas, para hacerles limpieza, transformación, y luego ser guardados en formato csv.
Las técnicas utilizadas fueron: la imputación de valores faltantes, la eliminación de duplicados y la detección y tratamiento de valores atípicos.

# 2. Desarrollo de las funciones para la API
A partir de especificaciones dadas, como se mencionó anteriormente se crearon los archivos csv contemplando las necesidades y particularidades requeridas para la construcción de cada función. En consecuencia, se pudo comprobar el óptimo funcionamiento, de cada función mediante la obtención de resultados lógicos.

# 3. Desarrollo de la API con FastAPI 🚀
Mediante la creación del archivo main.py se instauró una API utilizando el framework FastAPI, permitiendo realizar consultas específicas sobre los datos, obteniendo recomendaciones de videojuegos. Las funciones utilizadas son las desarrolladas en el punto 2, disponibles en el archivo **proyecto_funciones**.  Las consultas posibles a realizar son: información del usuario, contar reseñas en un rango de fechas, buscar juegos por género, entre otras.

# 4. Despliegue de la API en la Nube ☁️
Se seleccionó la plataforma Railway, para desplegar la API en un entorno accesible públicamente y poder ser utilizada, ya simplificó el proceso de deployment para conectar al repositorio de GitHub .

# 5. Modelo de Aprendizaje Automático 🤖

Se diseñó un sistema de recomendación basado en filtrado colaborativo que utiliza PCA (Análisis de Componentes Principales) y la similitud de coseno para proporcionar recomendaciones de ítems basadas en la similitud entre los ítems. El código crea una función que toma un ítem de referencia y devuelve las mejores recomendaciones para ese ítem en función de la similitud de coseno.

> Mapea usuarios e ítems a índices enteros para procesamiento eficiente.
> Divide los datos en conjuntos de entrenamiento y prueba.
> Normaliza las características de los ítems y aplica PCA para reducir la dimensionalidad.
> Calcula la similitud de coseno entre ítems y crea una matriz de similitud.
> Define una función para obtener recomendaciones de ítems basadas en la similitud.
> Utiliza la función para obtener recomendaciones para un ítem de referencia.


# Anexos

*Linkedin*:https://www.linkedin.com/in/robruschini/

**Link drive a archivos originales**: https://drive.google.com/drive/folders/1f6SyIawen1rKy9I8YbIvnuDMYP4diBGH?usp=sharing

**Video Demostrativo**: Se adjunta video explicativo
# Detalle de librerias:
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns 
import ipywidgets as widgets
import ast
import re
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity



