# Funciones de limpieza, wrangling, feature engineering y modeling
import math
import pandas as pd
from sklearn.utils import shuffle
from sklearn.metrics import recall_score, precision_score, f1_score, classification_report, accuracy_score, mean_squared_error, r2_score


"""
Creacion de variables lag

Parametros:
- DataFrame: The dataframe containing the data.
- columns: List of column names to create lag variables for.
- num_lags: Number of lag variables to create.

Retorna:
- DataFrame: Dataframe con las variables lag

"""
def create_lag_variables(df, columns, num_lags):

    for lag in range(1, num_lags + 1):
        for column in columns:
            df[f"{column}_Lag{lag}"] = df[column].shift(lag)
    return df


"""
Sobremuestreo de la clase minoritaria.

Parámetros:
- caracteristicas (pd.Series): x_train
- objetivo (pd.Series): y_train
- tasa_de_crecimiento (int): Número de veces que se replicará la clase minoritaria.

"""
def sobremuestreo(caracteristicas, objetivo, tasa_de_crecimiento):

    caracteristicas_0 = caracteristicas[objetivo == 0]
    caracteristicas_1 = caracteristicas[objetivo == 1]

    objetivo_0 = objetivo[objetivo == 0]
    objetivo_1 = objetivo[objetivo == 1]

    caracteristicas_resampled = pd.concat([caracteristicas_0] + [caracteristicas_1] * tasa_de_crecimiento)
    objetivo_resampled = pd.concat([objetivo_0] + [objetivo_1] * tasa_de_crecimiento)

    caracteristicas_resampled, objetivo_resampled = shuffle(
        caracteristicas_resampled,
        objetivo_resampled,
        random_state=12345
    )

    return caracteristicas_resampled, objetivo_resampled


"""
Genera el reporte de clasificación para el modelo.

Parametros:
- y_test: Valores reales de la variable objetivo.
- y_pred: Valores predichos por el modelo.

Retorna:
- None: Imprime el reporte de clasificación y otras métricas de evaluación.

"""
def reporte(y_test, y_pred):
    
    print("Reporte de clasificación:")
    print(classification_report(y_test, y_pred))

    print("Exactitud: ", accuracy_score(y_test, y_pred))
    print('Recall:', recall_score(y_test, y_pred)) # validacion_objetivo, predict_validacion_rl
    print('Precision:', precision_score(y_test, y_pred)) # validacion_objetivo, predict_validacion_rl

    print("\nRMSE: ", math.sqrt(mean_squared_error(y_test, y_pred)))
    print("R^2: ", r2_score(y_test, y_pred))


"""
Genera el reporte de predicciones para el modelo.

Parametros:
- y_pred: Valores predichos por el modelo.

Retorna:
- None: Imprime el reporte de clasificación y otras métricas de evaluación.

"""
def predicciones(y_pred):
    conteo_clases = pd.Series(y_pred).value_counts()

    print("Conteo de clases:")
    print(conteo_clases)

    # Porcentaje de acciones que suben con respecto a las que bajan
    print("\nTotal de datos sobre los que predice: " , y_pred.shape[0])
    print("Datos que fueron predichos: " , y_pred.sum())

    print("El modelo predice que el", (y_pred.sum() / y_pred.shape[0] * 100).__round__(2), "% de acciones suben")

