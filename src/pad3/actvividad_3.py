import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class actividad_3:
    def __init__(self):
        pass
    
        # Crear un DataFrame
data = {
    'Granadilla': [20],
    'Tomates': [50]
}
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv('punto_1.csv', index=False)

# Crear el DataFrame
data = {
    'Granadilla': [20, 49],
    'Tomates': [50, 100]
}
# Crear el DataFrame
df = pd.DataFrame(data, index=['ventas 2021', 'ventas 2022'])

# Guardar el DataFrame en un archivo CSV
df.to_csv('punto_2_ventas.csv')

print("Archivo 'ventas.csv' creado exitosamente.")



# Crear la serie con los utensilios y sus respectivas unidades
utensilios = pd.Series(
    {
        'Cuchara': '3 unidades',
        'Tenedor': '2 unidades',
        'Cuchillo': '4 unidades',
        'Plato': '5 unidades'
    },
    name='Cocina'
)

# Mostrar la serie
print(utensilios)

# Cargar el archivo CSV (asegúrate de especificar la ruta correcta)
# Cambia 'ruta/al/archivo.csv' por el nombre de tu archivo
df = pd.read_csv('C:\dataset_wine\winemag-data_first150k.csv')

# Mostrar las primeras filas del DataFrame
print(df.head())

# Para visualizar todas las columnas y configurar opciones
pd.set_option('display.max_columns', None)  # Muestra todas las columnas
pd.set_option('display.width', 1000)       # Ajuste de ancho para mejor visualización

# Mostramos el DataFrame completo (si no es muy grande)
print(df)

# Cargar los datos en un DataFrame (cambia 'ruta/a/tu/archivo.csv' con la ruta de tu archivo)
df = pd.read_csv('C:\dataset_wine\winemag-data_first150k.csv')

# Obtener las primeras cinco filas
primeras_filas = df.head(5)

# Obtener las últimas cinco filas
ultimas_filas = df.tail(5)

# Concatenar las dos partes verticalmente
resultados = pd.concat([primeras_filas, ultimas_filas])

# Guardar el resultado en un archivo CSV
resultados.to_csv('resultado_primeras_ultimas_filas.csv', index=False)

print("Archivo generado: resultado_primeras_ultimas_filas.csv")