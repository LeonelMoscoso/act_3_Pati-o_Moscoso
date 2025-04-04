import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
print(os.getcwd())

class actividad_3:
    def __init__(self):
        pass
    
# Especificar la ruta del archivo, por ejemplo, un archivo CSV
archivo = 'C:\dataset_final\winemag-data_first150k.csv'

# Cargar el dataset
dataset = pd.read_csv('C:\dataset_final\winemag-data_first150k.csv')

# Definir df aquí
data = {
    'variety': ['Pinot Noir', 'Cabernet Sauvignon', 'Chardonnay', 'Zinfandel', 'Syrah', 
                'Merlot', 'Sauvignon Blanc', 'Red Blend', 'Bordeaux-style Red Blend', 'Petite Sirah'],
    'counts': [7633, 7452, 6536, 3691, 2705, 2293, 2220, 1783, 1130, 830]
}
df = pd.DataFrame(data)

# Ahora puedes imprimir df
print(df.head())

# Mostrar las primeras filas del dataset
print(dataset.head())

# Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head())

# Resumen de estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())

# Mostrar la cantidad de vinos por variedad
variedad_count = df['variety'].value_counts()

print("\nCantidad de vinos por variedad:")
print(variedad_count)

# Gráfico de barras de las 10 variedades más comunes
plt.figure(figsize=(10, 6))
variedad_count.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Variedades de Vinos')
plt.xlabel('Variedad')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Mostrar el gráfico
plt.tight_layout()
plt.show()

# Filtrar vinos con puntaje mayor a 90
vinos_altos = df[df['points'] > 90]
print("\nVinos con puntaje mayor a 90:")
print(vinos_altos[['variety', 'points']].head())
print(df.columns.tolist())
# Eliminar espacios en nombres de columnas:
df.columns = df.columns.str.strip()
# Paso 1: Verificar columnas
print("Columnas disponibles:", df.columns.tolist())

# Paso 2: Corregir el nombre (ejemplo si la columna se llama "Points")
vinos_altos = df[df['points'] > 90]

# Opcional: Renombrar la columna (si prefieres usar "points")
df = df.rename(columns={'points': 'points'})
vinos_altos = df[df['points'] > 90]
print("Columnas del DataFrame:", df.columns.tolist())


    
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
df.to_csv('reviews.csv', index=False)

print("Archivo 'reviews.csv' generado con éxito.")

# Cargar los datos en un DataFrame (cambia 'ruta/a/tu/archivo.csv' con la ruta de tu archivo)
df = pd.read_csv('C:\dataset_final\winemag-data_first150k.csv')

# Ensure the path is correct as per your directory structure
file_path = r'C:\dataset_final\winemag-data_first150k.csv' 

try:
    df = pd.read_csv(file_path)
    print(df.head())  # Display the first few rows of the DataFrame
except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Please check if the file path is correct and the file exists.")

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
result.to_csv('punto_7_average_wine_price.csv', index=False)

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
max_price_row.to_frame().T.to_csv('punto_8_vino_mas_caro.csv', index=False)

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
df.to_csv('punto_9_vinos california.csv', index=False)
#
# Cargar el dataset (cambia 'ruta_a_tu_archivo.csv' con la ruta de tu archivo CSV)

wines = pd.read_csv('C:\dataset_final\winemag-data_first150k.csv')

# Encuentra el índice del vino con el precio más alto
indice_max_precio = wines['price'].idxmax()

# Obtén toda la información de ese vino
vino_caro = wines.loc[indice_max_precio]

# Generación del archivo
with open('punto_10_vino_caro.txt', 'w') as f:
    f.write("El vino más caro de California es:\n")
    for key, value in vino_caro.items():
        f.write(f"{key}: {value}\n")
        
    # Datos de ejemplo sobre los tipos de uva más comunes en California
data = {
    'Variedad': ['Chardonnay', 'Cabernet Sauvignon', 'Merlot', 'Zinfandel', 'Pinot Noir'],
    'Descripción': [
        'Uva blanca ampliamente cultivada, elegante y fresca.',
        'Uva tinta, conocida por su cuerpo y taninos fuertes.',
        'Variedad suave, frutal y fácil de beber.',
        'Uva tinta californiana, con sabores a mora y especias.',
        'Uva tinta, ligera y con notas de frutas rojas.'
    ]
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Mostrar el DataFrame
print("Tipos de uva más comunes en California:")
print(df)

# Guardar en un archivo CSV
df.to_csv('punto_11_tipos_de_uva_california.csv', index=False)

print("El archivo 'tipos_de_uva_california.csv' ha sido generado exitosamente.")   

# Lista de tipos de uva y sus cantidades
uvas_california = [
    ("Pinot Noir", 7633),
    ("Cabernet Sauvignon", 7452),
    ("Chardonnay", 6536),
    ("Zinfandel", 3691),
    ("Syrah", 2705),
    ("Merlot", 2293),
    ("Sauvignon Blanc", 2220),
    ("Red Blend", 1783),
    ("Bordeaux-style Red Blend", 1130),
    ("Petite Sirah", 830)
]

# Nombre del archivo a crear
nombre_archivo = 'tipos_uvas_california.txt'

# Escribir la información en el archivo
with open(nombre_archivo, 'w') as archivo:
    for uva, cantidad in uvas_california:
        archivo.write(f'{uva} {cantidad}\n')

print(f'Archivo {nombre_archivo} creado con éxito.')

# Datos 
data = {
    'variety': [
        'Pinot Noir',
        'Cabernet Sauvignon',
        'Chardonnay',
        'Zinfandel',
        'Syrah',
        'Merlot',
        'Sauvignon Blanc',
        'Red Blend',
        'Bordeaux-style Red Blend',
        'Petite Sirah'
    ],
    'count': [
        7633,
        7452,
        6536,
        3691,
        2705,
        2293,
        2220,
        1783,
        1130,
        830
    ]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Guardar DataFrame en un archivo CSV
df.to_csv('punto_12_tipo uvas california.csv', index=False)

# Imprimir en un formato similar al de la imagen
print(df.to_string(index=False))
print("Name: variety, dtype: int64")

try:
    wine_data = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"El archivo no se encontró en la ruta: {file_path}")
    
    df = pd.read_csv(r'C:\dataset_wine\winemag-data_first150k.csv')
    
    # excepciones
    try:
        df = pd.read_csv(file_path)
        print(df.head())  # Muestra las primeras filas del DataFrame
    except FileNotFoundError:
        print("El archivo no se encuentra en la ruta especificada.")
    except pd.errors.EmptyDataError:
        print("El archivo está vacío.")
    except pd.errors.ParserError:
        print("Error al analizar el archivo. Verifica el formato CSV.")
    except Exception as e:
        print(f"Se produjo un error desconocido: {e}")
        
        # direccion alternativa
        # Cambia la ruta a la ubicación correcta de tu archivo CSV
        
        df = pd.read_csv('new_path_to_your_file/winemag-data_first150k.csv')
        
        # Verifica si el archivo existe antes de intentar leerlo
if not os.path.exists(file_path):
    print(f"Error: El archivo no se encuentra en la ruta especificada: {file_path}")
else:
    try:
        # Intenta leer el archivo
        wine_data = pd.read_csv(file_path)
        print("Archivo leído correctamente.")
        print(wine_data.head())  # Muestra las primeras filas para verificar
    except FileNotFoundError:
        print(f"Error: El archivo no se encontró en la ruta especificada: {file_path}")
    except pd.errors.ParserError:
        print("Error: Hubo un problema al analizar el archivo CSV. Verifica el formato.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        
        