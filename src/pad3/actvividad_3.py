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

# Convertir a DataFrame
df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)
# Guardar el DataFrame en un archivo CSV
df.to_csv('frutas.csv', index=False)

# Crear el DataFrame
data = {
    'Granadilla': [20, 49],
    'Tomates': [50, 100]
}

# Definir los índices
index = ['ventas 2021', 'ventas 2022']

# Crear el DataFrame
ventas_frutas = pd.DataFrame(data, index=index)

# Mostrar el DataFrame
print(ventas_frutas)
# Datos
categorias = ['Granadilla', 'Tomates']
ventas_2021 = [20, 50]
ventas_2022 = [49, 100]

# Posiciones de las barras
x = np.arange(len(categorias))

# Ancho de las barras
ancho = 0.35

# Crear el gráfico de barras
fig, ax = plt.subplots()
barras1 = ax.bar(x - ancho/2, ventas_2021, ancho, label='Ventas 2021')
barras2 = ax.bar(x + ancho/2, ventas_2022, ancho, label='Ventas 2022')

# Añadir etiquetas y título
ax.set_ylabel('Cantidad de Ventas')
ax.set_title('Ventas de Granadilla y Tomates por Año')
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.savefig('ventas_granadilla_tomates.png')  # Guardar en archivo
plt.show()

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
df = pd.read_csv('C:\winemag-data-130k-v2.csv')

# Mostrar las primeras filas del DataFrame
print(df.head())

# Para visualizar todas las columnas y configurar opciones
pd.set_option('display.max_columns', None)  # Muestra todas las columnas
pd.set_option('display.width', 1000)       # Ajuste de ancho para mejor visualización

# Mostramos el DataFrame completo (si no es muy grande)
print(df)

# Cargar los datos en un DataFrame (cambia 'ruta/a/tu/archivo.csv' con la ruta de tu archivo)
df = pd.read_csv('C:\winemag-data-130k-v2.csv')

# Obtener las primeras cinco filas
primeras_filas = df.head(5)

# Obtener las últimas cinco filas
ultimas_filas = df.tail(5)

# Concatenar las dos partes verticalmente
resultados = pd.concat([primeras_filas, ultimas_filas])

# Guardar el resultado en un archivo CSV
resultados.to_csv('resultado_primeras_ultimas_filas.csv', index=False)

print("Archivo generado: resultado_primeras_ultimas_filas.csv")