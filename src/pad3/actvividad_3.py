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

# Crear una serie con los utensilios y sus cantidades
utensilios = pd.Series({'Cuchara': '3 unidades',
                        'Tenedor': '2 unidades',
                        'Cuchillo': '4 unidades',
                        'Plato': '5 unidades'}, name='Cocina')

# Mostrar la serie
print(utensilios)

# Guardar la serie en un archivo de texto
utensilios.to_csv('punto3_utensilios.csv', header=True)

# Cargar el dataset
file_path = 'C:\dataset_wine\winemag-data_first150k.csv'  # Reemplaza esto con la ruta del archivo CSV
wine_data = pd.read_csv(file_path)

# Mostrar las primeras filas para verificar la carga
print(wine_data.head())

# Datos de la tabla
data = {
    "Unnamed: 0": [1, 2, 3, 4, 5, 6, 7, 8],
    "country": ["US", "Spain", "US", "France", "Italy", "France", "Italy", "France"],
    "description": [
        "This tremendous 100% varietal...",
        "Ripe aromas of fig, blackberry...",
        "Max Watson honors the memory...",
        "This is the top wine from La Bequude...",
        "Many people feel Piane represents southern...",
        "Offers an intriguing nose with ginger...",
        "The classic example comes from a vineyard...",
        "More Pinot Grigios should taste like this..."
    ],
    "designation": [
        "Martha's Vineyard", 
        "Cardorum Selection Especial Reserve", 
        "Special selected Lieu-dit", 
        "Reserve", 
        "Cuvée Prégnant", 
        "Etre Prodin", 
        "Carad du Rossi", 
        None
    ],
    "points": [95, 96, 96, 94, 91, 92, 89, 15],
    "price": [235.0, 60.0, 69.0, 66.0, 20.0, 22.0, 30.0, 15.0],
    "province": [
        "California", 
        "Northern Spain", 
        "California", 
        "Provence", 
        "Southern Italy", 
        "Champagne", 
        "Northeastern Italy", 
        "Champagne"
    ],
    "region_1": [
        "Napa Valley", 
        "Toro", 
        "Knights Valley", 
        "Bandol", 
        "Fino di Avellino", 
        None, 
        "Alto Adige", 
        None
    ],
    "region_2": [
        None, 
        None, 
        "Sonoma", 
        "Provence red blend", 
        "White Blend", 
        "Champagne", 
        "Pinot Grigio", 
        "Champagne"
    ],
    "variety": [
        "Cabernet Sauvignon", 
        "Tempranillo", 
        "Sauvignon Blanc", 
        "Pinot Noir", 
        "White Blend", 
        "Champagne", 
        "Pinot Grigio", 
        "Pinot Grigio"
    ],
    "winery": [
        "Heitz", 
        "Bodegas Cibantos Rodriguez", 
        "Maclay", 
        "Domaine de la Bequude", 
        "Feudi di San Gregorio", 
        "H. Germain", 
        "Alois Lageder", 
        "Alois Lageder"
    ],
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Guardar en un archivo CSV
df.to_csv('punto4_reviews.csv', index=False)

print("Archivo 'reviews.csv' generado con éxito.")

# Cargar los datos en un DataFrame (cambia 'ruta/a/tu/archivo.csv' con la ruta de tu archivo)
df = pd.read_csv('C:\dataset_wine\winemag-data_first150k.csv')

# Para obtener las primeras cinco filas
df_head = df.head(5)

# Mostrar en pantalla
print(df_head)

# Guardar en un archivo
df_head.to_csv('punto 5_primeras_cinco_filas.csv', index=False)

# Para visualizarlo en formato tabular Jupyter Notebook (opcional)
df_head.style.set_table_styles(
    [{'selector': 'thead th', 'props': [('background-color', '#333'), 
                                          ('color', 'white')]},
     {'selector': 'tbody td', 'props': [('background-color', '#444'), 
                                          ('color', 'white')]}]
)


# Assuming df_head is your DataFrame
styled_df = df_head.style.set_table_styles({
    # Your styling options here
})

# Display styled DataFrame (in Jupyter notebook or similar)
styled_df

# Cargar el DataFrame (aquí debes especificar la fuente de tus datos)
# df = pd.read_csv('tu_archivo.csv')  # Por ejemplo, si es un CSV

# Usar el método .info() para obtener información sobre el DataFrame
df.info()

# Contar cuántas entradas hay
number_of_entries = len(df)
print(f'Número de entradas: {number_of_entries}')

# Generar un archivo (por ejemplo, CSV)
df_head.to_csv('punto_6.csv', index=False)