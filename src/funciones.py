# Funciones de limpieza, wrangling, feature engineering y modeling
import pandas as pd
from sklearn.utils import shuffle


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
