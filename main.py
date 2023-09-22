from fastapi import FastAPI
import uvicorn
import pandas as pd
from fastapi.responses import RedirectResponse
from textblob import TextBlob 



#Archivo Reviews - Función 1 y 2
df_original = pd.read_csv ("df_original.csv")

#Archivo games . Función 1
df_new_game_copy = pd.read_csv ("df_new_game_copy.csv")

# Archivo Items - Función 3 y 4
df_fusion3 = pd.read_csv ("df_fusion3.csv")                       
                           
#Archivo Games - Función 5
df_funcion5 = pd.read_csv ("df_funcion5.csv")


app = FastAPI ()

@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse("/docs#/", status_code=308) 

@app.get("/")
def read_root():
    return {"Hello": "World ro"}


@app.get ("/def userdata/ {User_id}")

def userdata(User_id: str):
    # Filtrar los datos para el usuario específico
    datos_usuario = df_original[df_original['user_id'] == User_id]
    
    # Calcular la cantidad de dinero gastado por el usuario
    total_gastado = df_new_game_copy[df_new_game_copy['user_id'] == User_id]['price'].sum()
    
    # Calcular el porcentaje de recomendación en base a la columna correcta (ajusta esto)
    # Suponiendo que "opiniones.recomendacion" es la columna relevante en df_original
    porcentaje_recomendacion = (datos_usuario['recommend'].sum() / len(datos_usuario)) * 100
    
    # Calcular la cantidad de ítems
    cantidad_items = df_new_game_copy[df_new_game_copy['user_id'] == User_id]['items_count'].sum()
    
    # Devolver los resultados como un diccionario
    resultados = {
        'id_usuario': User_id,
        'total_gastado': total_gastado,
        'porcentaje_recomendacion': porcentaje_recomendacion,
        'cantidad_items': cantidad_items
    }
    
    return resultados


@app.get ("/def countreviews/ {start_date: str, end_date}")

def countreviews(start_date: str, end_date: str,) -> dict:
    # Filtrar los datos para las fechas dadas en formato de cadena (str)
    filtrado_data = df_original[(df_original['fecha'] >= start_date) & (df_original['fecha'] <= end_date)]

    # Contar la cantidad de usuarios únicos que realizaron reseñas en ese período
    unique_users = filtrado_data['user_id'].nunique()

    # Calcular el porcentaje de recomendación en base a reviews.recommend
    # Suponiendo que "recommend" es la columna relevante en df_original
    # Si hay "None" en "recommend", se excluyen del cálculo
    reviews = filtrado_data['recommend'].dropna().astype(int)
    percentage_recommendation = (reviews.sum() / len(reviews)) * 100

    # Devolver los resultados como un diccionario
    resultados = {
        'cantidad_usuarios': unique_users,
        'porcentaje_recomendacion': percentage_recommendation
    }

    return resultados


@app.get ("/def genre/ {genero}")

def genre(genero: str):
    try:
        # Filtrar el DataFrame para obtener las filas del género especificado
        genre_df = df_fusion3[df_fusion3['app_name'] == genero]

        # Verificar si el DataFrame filtrado no está vacío
        if genre_df.empty:
            return "Género no encontrado en el DataFrame"

        # Calcular la posición del género en el ranking según el tiempo de juego 'playtime_forever'
        genre_ranking = genre_df.groupby('app_name')['playtime_forever'].sum().reset_index()
        genre_ranking = genre_ranking.sort_values(by='playtime_forever', ascending=False)
        position = genre_ranking[genre_ranking['app_name'] == genero].index[0] + 1

        # Crear un diccionario con la posición y el nombre del género
        result_dict = {
            "Posición": position,
            "Género": genero
        }
        return result_dict
    except IndexError:
        return "Género no encontrado en el ranking"
   
   
    
    
@app.get ("/def userforgenre/ {genero}")

def userforgenre(genero: str):
    try:
        # Filtra las filas correspondientes al género dado
        genero_df = df_fusion3[df_fusion3[genero] == 1]

        # Ordena el DataFrame por horas de juego en orden descendente
        sorted_genero_df = genero_df.sort_values(by='playtime_hours', ascending=False)

        # Selecciona las 5 primeras filas para obtener el top 5 de usuarios
        top_5_usuarios = sorted_genero_df[['user_url', 'item_id', 'playtime_hours']].head(5)

        # Convertir el DataFrame resultante en una lista de diccionarios
        usuarios_lista = top_5_usuarios.to_dict(orient='records')

        return usuarios_lista
    except KeyError:
        return f"Género '{genero}' no encontrado en el DataFrame"
    



@app.get ("/developer/ {esarrollador}")

def developer(desarrollador: str):
    try:
        # Filtrar el DataFrame para obtener las filas del desarrollador especificado
        df_desarrollador = df_funcion5[df_funcion5['developer'] == desarrollador]

        # Verificar si el DataFrame filtrado no está vacío
        if df_desarrollador.empty:
            return "No se encontraron datos para el desarrollador especificado."

        # Calcular el porcentaje de contenido gratuito ("Free") por año
        def calcular_porcentaje_free(group):
            total_items = len(group)
            porcentaje_free = (group['price'] == 'Free').sum() / total_items * 100
            return porcentaje_free

        porcentaje_free_por_anio = df_desarrollador.groupby('year').apply(calcular_porcentaje_free)

        # Calcular la cantidad total de items por año
        cantidad_items_por_anio = df_desarrollador['year'].value_counts().sort_index()

        # Combinar las dos series en un DataFrame
        resultado_df = pd.DataFrame({'Año': porcentaje_free_por_anio.index,
                                     'Contenido Free (%)': porcentaje_free_por_anio.values,
                                     'Cantidad de Items': cantidad_items_por_anio.values})

        # Convertir el DataFrame resultante en una lista de diccionarios
        resultado_lista = resultado_df.to_dict(orient='records')

        return resultado_lista
    except KeyError:
        return f"Desarrollador '{desarrollador}' no encontrado en el DataFrame"