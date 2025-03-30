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

# **Obtener información sobre el DataFrame**
df.info()

# **Contar cuántas entradas hay**
number_of_entries = len(df)
print(f'Número de entradas: {number_of_entries}')

# **Seleccionar las primeras filas del DataFrame (opcional)**
df_head = df.head()  # Por ejemplo, puedes usar las primeras 5 filas

# **Generar un archivo CSV**
df_head.to_csv('punto_6_entradas.csv', index=False)


# precio promedio
ata = {
    'country': ['US', 'Spain', 'US', 'France'],
    'description': [
        "This tremendous 100% varietal wine...",
        "Pure aroma of fig, blackberry...",
        "This wine spent 20 months...",
        "This is the top wine from LA Begude..."
    ],
    'designacao': ['Marley’s Vineyard', 'Cardorum Selection Especial Reserve', 'Special selected Lieu-Reserve', 'La Brilade'],
    'points': [96, 90, 96, 95],
    'price': [130.0, 190.0, 96.0, 66.0],
    'province': ['California', 'Northern Spain', 'California', 'Provence'],
    'region_1': ['Napa Valley', 'Yoro', 'Sonoma', 'Nîmes'],
    'variety': ['Cabernet Sauvignon', 'Tinto', 'Sauvignon Blanc', 'Provence red blend'],
    'winery': ['Hertz', 'Bodega Carmen Rodriguez', 'Macayda', 'Domaine de la Begude']
}

df = pd.DataFrame(data)

# Calcular el precio promedio
average_price = df['price'].mean()

# Guardar el resultado en un archivo CSV
result = pd.DataFrame({'Average Price': [average_price]})
result.to_csv('average_wine_price.csv', index=False)

print("Archivo 'average_wine_price.csv' creado con el precio promedio.")

# Verificar la versión de Python
import sys

# Versión mínima requerida
MIN_PYTHON_VERSION = (3, 6)

def check_python_version():
    if sys.version_info < MIN_PYTHON_VERSION:
        print(f"Error: Se requiere Python {MIN_PYTHON_VERSION[0]}.{MIN_PYTHON_VERSION[1]} o superior.")
        print(f"Versión actual: {sys.version}")
        return False
    print(f"Versión de Python correcta: {sys.version}")
    return True

# Verificar versiones de librerías específicas (ejemplo: pandas)
def check_library_version(library, min_version):
    try:
        module = __import__(library)
        if tuple(map(int, module.__version__.split('.'))) < min_version:
            print(f"Error: Se requiere {library} {min_version} o superior. Versión actual: {module.__version__}")
            return False
        print(f"{library} tiene la versión correcta: {module.__version__}")
        return True
    except ImportError:
        print(f"Error: {library} no está instalado.")
        return False

# Ejecución de las verificaciones
if __name__ == "__main__":
    if check_python_version():
        check_library_version('pandas', (1, 1))
        check_library_version('numpy', (1, 18))
        
        import shutil
import os

# crear copia d e seguridad
# Función para crear una copia de seguridad de un directorio

def crear_copia_seguridad(ruta_origen, ruta_destino):
    # Verifica si la ruta de origen existe
    if not os.path.exists(ruta_origen):
        print(f"La ruta de origen '{ruta_origen}' no existe.")
        return

    # Si la ruta de destino no existe, créala
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)

    # Crea la copia de seguridad
    try:
        shutil.copytree(ruta_origen, ruta_destino, dirs_exist_ok=True)
        print(f"Copia de seguridad realizada desde '{ruta_origen}' a '{ruta_destino}'.")
    except Exception as e:
        print(f"Error al crear la copia de seguridad: {e}")

# Ejemplo de uso
ruta_origen = 'C:\actvidad_3_final\act_3_Pati-o_Moscoso\src\pad3\actvividad_3.py'
ruta_destino = 'C:\actvidad_3_final\act_3_Pati-o_Moscoso\src\pad3\backup'
# Llama a la función para crear la copia de seguridad


crear_copia_seguridad(ruta_origen, ruta_destino)

# Encontrar el precio más alto
max_price_row = df.loc[df['price'].idxmax()]

# Mostrar información del vino con el precio más alto
print("Vino con el precio más alto:")
print(max_price_row)

# Guardar la información en un archivo CSV
max_price_row.to_frame().T.to_csv('vino_mas_caro.csv', index=False)

print("Información guardada en 'vino_mas_caro.csv'")

# Definir los datos
data = {
    'Unnamed: 0': [0, 1, 2, 16, 19, 150892, 150896, 150914],
    'country': ['US', 'US', 'US', 'US', 'US', 'US', 'US', 'US'],
    'description': [
        'This tremendous 100% varietal wine hails from...',
        'Mac Watson honors the memory of a wine once ma...',
        'The producer sources from two blocks of the v...',
        'This blockbuster, powerhouse of a wine suggest...',
        'This fresh and lively medium-bodied wine is b...',
        'A light, earthy wine, with violet, berry and...',
        'Some raspberry fruit in the aroma, but things...',
        'Old-gold in color, and thick and syrupy. The...'
    ],
    'designation': [
        'Martha\'s Vineyard', 'Special Selected Late Harvest',
        'Cap\'s Crown Vineyard', 'Rainin Vineyard', 
        'Cap\'s Crown Vineyard', 'Coastal',
        None, 'Late Harvest Cluster Select'
    ],
    'points': [96, 96, 95, 95, 95, 82, 82, 94],
    'price': [23.0, 9.0, 60.0, 325.0, 75.0, 10.0, 10.0, 25.0],
    'province': ['California', 'California', 'California', 'California', 'California', 'California', 'California', 'California'],
    'region_1': ['Napa Valley', 'Sonoma', 'Sonoma Coast', 'Diamond Mountain District', 'Sonoma Coast', 'California', 'California', 'Mendocino/Lake Counties'],
    'region_2': ['Napa', 'Knights Valley', 'Sonoma', 'Napa', 'Sonoma', 'California Other', 'California Other', 'Lake Counties'],
    'variety': ['Cabernet Sauvignon', 'Sauvignon Blanc', 'Pinot Noir', 'Cabernet Sauvignon', 'Pinot Noir', 'Merlot', 'Pinot Noir', 'White Riesling'],
    'winery': ['Heitz', 'Macauley', 'Blue Farm', 'Hall', 'Gary Farrell', 'Callaway', 'Camelot', 'Navarro']
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Guardar como archivo CSV
df.to_csv('punto_9_vinos.csv', index=False)
#
# Cargar el dataset (cambia 'ruta_a_tu_archivo.csv' con la ruta de tu archivo CSV)

wines = pd.read_csv('C:\dataset_wine\winemag-data_first150k.csv')

# Encuentra el índice del vino con el precio más alto
indice_max_precio = wines['price'].idxmax()

# Obtén toda la información de ese vino
vino_caro = wines.loc[indice_max_precio]

# Generación del archivo
with open('vino_caro.txt', 'w') as f:
    f.write("El vino más caro de California es:\n")
    for key, value in vino_caro.items():
        f.write(f"{key}: {value}\n")