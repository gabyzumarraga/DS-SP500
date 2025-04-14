# Proyecto DS - Modelo Predictivo para anticipar movimientos en las acciones de las empresas que estan dentro del Índice S&P 500

El índice S&P 500, (Standard & Poor’s 500), es un indicador bursátil sobre el rendimiento de las acciones de las 500 empresas lideres que cotizan en la bolsa de valores de Estados Unidos (por capitalización de mercado). Este es un indicador clave de la salud económica de los Estados Unidos ya que abarca información sobre diferentes tipos de industrias, como tecnología, atención médica, servicios financieros, bienes de consumo y energía, seleccionadas por su tamaño, liquidez y representatividad económica.   


El objetivo principal de este proyecto es desarrollar un modelo predictivo que permita anticipar si el precio de las acciones de las empresas que se encuentran dentro del S&P 500 subirá o bajará (diariamente) en función de datos históricos, como precios de apertura, cierre, cambios diarios de precios y otras variables derivadas.

##  Contexto 

**Hipótesis principal:** Los movimientos históricos de precios pueden revelar tendencias repetitivas o correlaciones significativas que permitan prever cambios en los precios de las acciones en el mercado bursátil. 

**Qué necesitas comprobar o resolver:** Identificar patrones relevantes en los precios de las acciones que puedan ayudar a entender el comportamiento de los precios de las acciones en el mercado para tomar decisiones de inversión y mejorar el rendimiento. 

**Pregunta de investigación**: ¿Qué patrones de precios se existen en las acciones de las empresas del S&P 500, y cómo pueden usarse para anticipar movimientos futuros?


**Relevancia:** Este análisis puede ayudar a los stakeholders, inversionistas, analistas financieros o incluso instituciones financieras a:
1. Tomar decisiones informadas: sobre la compra o venta de acciones para mejorar sus rendimientos al conocer el comportamiento o la tendencia de las acciones de interés.
2. Gestión de riesgos: permitirá identificar patrones que podrían reducir el riesgo asociado con las inversiones este mercado.
3. Optimizar estrategias: facilita la creación de estrategias de trading automatizadas basadas en predicciones de movimientos del mercado.



## Project Structure

El proyecto está organizado de la siguiente manera:

```
├── data
│   ├── clean
│       └── df_clean_companies.csv
│       └── df_clean_index.csv
│       └── df_clean_stocks.csv
│   ├── curated
│       └── df_curated_companies.csv
│       └── df_curated_index.csv
│       └── df_curated_stocks.csv
│   ├── raw
│       └── sp500_companies.csv
│       └── sp500_index.csv
│       └── sp500_stocks.csv
├── instrucciones
│   ├── Proyecto #1
│   ├── Proyecto #2
│   ├── Proyecto Final
├── notebooks
│   ├── 01_EDA.ipynb
│   ├── 02_DataWrangling.ipynb
│   ├── 03_FeatureEngineering.ipynb
│   ├── 04_Modeling.ipynb
│   ├── 04_Modeling2.ipynb
├── reports
│   └── CRISP-DM #1.docx
│   └── CRISP-DM #2.pdf
│   └── CRISP-DM #1.docx
│   └── CRISP-DM #2.pdf
├── src
│   └── funciones.py
│   └── utils.py
└── .gitignore
└── README.md
├── requirements.txt
```

### Descripción breve de cada carpeta: 

1. data/: Datos en bruto (raw), datos limpios (clean) y datos procesados (curated). 
2. instrucciones/: Documentos que indican las instrucciones de cada etapa del proyecto. 
3. notebooks/: Notebooks utilizados. Estan ordenados pos tema para EDA, data 
wrangling y Modeling. 
4. src/: Aquí se guardan los scripts Python que contienen funciones o módulos 
reutilizables. 
5. reports/: Informes, visualizaciones y resultados. 
6. ../resultados/: Metricas oobtenidas de los modelos probados con diferentes hiperparametros.
7. README.md: Visión general clara del proyecto (propósito, estructura, 
instrucciones de uso). 
8. .gitignore: Lista de archivos y carpetas que se excluiran en el control de versiones 
9. requirements.txt: Indica las librerías y versiones que se utilizan en el proyecto.

## Usage Instructions

1. Clonar el repositorio: https://github.com/gabyzumarraga/DS-SP500.git
2. Instalar las librerias requeridas con el siguiente comando:

   ```
   pip install -r requirements.txt
   ```
3. Descargar del dataset de Kaggle: https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks?select=sp500_companies.csv
4. Usar los Jupyter notebooks ubicados en la carpeta `notebooks/` en el mismo orden

