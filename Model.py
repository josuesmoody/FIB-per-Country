import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Función para obtener los datos de felicidad desde el World Happiness Report
def get_happiness_data():
    # Simular datos de felicidad para simplificar
    data = {
        'Country': [
            'Finland', 'Denmark', 'Iceland', 'Sweden', 'Israel', 
            'Netherlands', 'Norway', 'Luxembourg', 'Switzerland', 'Australia',
            'New Zealand', 'Costa Rica', 'Kuwait', 'Austria', 'Canada',
            'Belgium', 'Ireland', 'Czechia', 'Lithuania', 'United Kingdom',
            'Slovenia', 'United Arab Emirates', 'United States', 'Germany', 'Mexico',
            'Uruguay', 'France', 'Saudi Arabia', 'Kosovo', 'Singapore',
            'Taiwan Province of China', 'Romania', 'El Salvador', 'Estonia', 'Poland',
            'Spain', 'Serbia', 'Chile', 'Panama', 'Malta',
            'Italy', 'Guatemala', 'Nicaragua', 'Brazil'
        ],
        'Happiness Score': [
            7.741, 7.583, 7.525, 7.344, 7.341, 
            7.319, 7.302, 7.122, 7.060, 7.057,
            7.029, 6.955, 6.951, 6.905, 6.900,
            6.894, 6.838, 6.822, 6.818, 6.749,
            6.743, 6.733, 6.725, 6.719, 6.678,
            6.611, 6.609, 6.594, 6.561, 6.523,
            6.503, 6.491, 6.469, 6.448, 6.442,
            6.421, 6.411, 6.360, 6.358, 6.346,
            6.324, 6.287, 6.284, 6.272
        ]
    }
    return pd.DataFrame(data)

# Función para obtener los datos de PIB, esperanza de vida, desempleo, Gini y corrupción
def get_other_data():
    # Simular datos para simplificar
    data = {
        'Country': [
            'Finland', 'Denmark', 'Iceland', 'Sweden', 'Israel', 
            'Netherlands', 'Norway', 'Luxembourg', 'Switzerland', 'Australia',
            'New Zealand', 'Costa Rica', 'Kuwait', 'Austria', 'Canada',
            'Belgium', 'Ireland', 'Czechia', 'Lithuania', 'United Kingdom',
            'Slovenia', 'United Arab Emirates', 'United States', 'Germany', 'Mexico',
            'Uruguay', 'France', 'Saudi Arabia', 'Kosovo', 'Singapore',
            'Taiwan Province of China', 'Romania', 'El Salvador', 'Estonia', 'Poland',
            'Spain', 'Serbia', 'Chile', 'Panama', 'Malta',
            'Italy', 'Guatemala', 'Nicaragua', 'Brazil'
        ],
        'GDP per Capita': np.random.uniform(20000, 60000, 44),
        'Life Expectancy': np.random.uniform(70, 85, 44),
        'Unemployment Rate': np.random.uniform(3, 15, 44),
        'Gini Coefficient': np.random.uniform(25, 45, 44),
        'Corruption Index': np.random.uniform(20, 80, 44)
    }
    return pd.DataFrame(data)

# Función para generar el DataFrame combinado
def generate_combined_dataframe():
    happiness_data = get_happiness_data()
    other_data = get_other_data()
    return pd.merge(happiness_data, other_data, on='Country')

# Función para realizar el análisis de regresión
def perform_regression_analysis(df):
    X = df[['GDP per Capita', 'Life Expectancy', 'Unemployment Rate', 'Gini Coefficient', 'Corruption Index']]
    y = df['Happiness Score']

    # Añadir una constante (intercepto) al modelo
    X = sm.add_constant(X)

    # Crear el modelo de regresión múltiple
    model = sm.OLS(y, X).fit()

    return model

# Función para visualizar los datos de felicidad por país junto con los resultados del análisis de regresión
def visualize_data(df, model):
    sns.set(style="whitegrid")

    # Gráfico de barras horizontal de la puntuación de felicidad
    plt.figure(figsize=(12, 10))
    sns.barplot(x='Happiness Score', y='Country', data=df, palette='viridis')
    plt.xlabel('Happiness Score', fontsize=14)
    plt.ylabel('Country', fontsize=14)
    plt.title('World Happiness Report 2024', fontsize=16)
    plt.show()

    # Resumen del modelo
    print(model.summary())

def main():
    df = generate_combined_dataframe()
    model = perform_regression_analysis(df)
    visualize_data(df, model)

if __name__ == "__main__":
    main()
