import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Leer archivos CSV con manejo de errores y especificando delimitadores si es necesario
try:
    metadata_indicador = pd.read_csv('Metadata_Indicator_API_NY.GDP.MKTP.CD_DS2_es_csv_v2_468671.csv')
    metadata_pais = pd.read_csv('Metadata_Country_API_NY.GDP.MKTP.CD_DS2_es_csv_v2_468671.csv')
    
    # Saltar las primeras filas que contienen metadatos
    datos_pib = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_es_csv_v2_468671.csv', skiprows=4)
except Exception as e:
    print(f"Error leyendo los archivos CSV: {e}")
    exit()

# Procesar los datos de PIB
try:
    # Asegurarnos de que las columnas tengan el nombre correcto
    datos_pib = datos_pib.rename(columns={'Country Name': 'País'})

    # Filtrar las columnas relevantes a partir de 2024 (último año disponible)
    columnas_pib = [col for col in datos_pib.columns if col.isdigit() and int(col) >= 2024]
    datos_pib = datos_pib[['País'] + columnas_pib]

    # Eliminar filas con valores faltantes en los años seleccionados
    datos_pib = datos_pib.dropna()

    # Generar datos aleatorios para FIB
    np.random.seed(42)
    datos_pib['FIB'] = np.random.uniform(4.0, 8.0, size=len(datos_pib))

    # Modelo de regresión lineal
    X = datos_pib.iloc[:, 1:].values  # Ignorar la columna 'País'
    y = datos_pib['FIB'].values
    modelo = LinearRegression().fit(X, y)

    # Parámetros de la regresión lineal
    print(f"Coeficientes de regresión: {modelo.coef_}")
    print(f"Intersección: {modelo.intercept_}")

    # Gráfico de barras comparativo
    fig, ax = plt.subplots(figsize=(10, 6))

    # Posiciones de las barras
    indices = np.arange(len(datos_pib))

    # Crear barras de PIB
    bar1 = ax.bar(indices - 0.2, datos_pib.iloc[:, 1:].mean(axis=1), 0.4, label='PIB')

    # Crear barras de FIB
    bar2 = ax.bar(indices + 0.2, datos_pib['FIB'], 0.4, label='FIB', alpha=0.7)

    # Configurar etiquetas y título
    ax.set_xticks(indices)
    ax.set_xticklabels(datos_pib['País'], rotation=45, ha='right', fontsize=8)  # Ajuste de la rotación y tamaño de la fuente
    ax.set_ylabel('Valor')
    ax.set_title('Comparación del PIB y la FIB por país en 2024')
    ax.legend()

    plt.tight_layout()
    plt.show()

except KeyError as e:
    print(f"Error procesando los datos: columna no encontrada {e}")
    exit()
