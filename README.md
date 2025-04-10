# Proyecto #2 - CRISP-DM, FEATURE ENGINEERING AND MODEL RESEARCH 

**Tema:** Análisis del desempeño de las empresas en el S&P (Standard and Poor's) 500 
utilizando datos históricos del mercado bursátil

El objetivo principal de este proyecto es analizar las tendencias y patrones históricos de precios y volúmenes de las acciones de las empresas del S&P 500 para proporcionar insights accionables.

Una vez finalizado analizada la data, procedemos con el proceso de Feature Engineering Y modeling. El objetivo es realizar la predicción de si sube o no una acción (problema de clasificacion), por lo cual se analizaran algunos modelos para determinar cual el el mejor a utilizar. Para ello, se trabajará únicamente con el archivo sp500_stocks. 

Para esta segunda entrega se realizara lo siguiente: 
- Entendimiento del problema/negocio
- EDA (Entendimiento de los datos)
- Data Wrangling (Data Preparation).
- Feature Engineering
- Modeling

## Project Structure

El proyecto está organizado de la siguiente manera:

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
├── notebooks
│   ├── 01_EDA.ipynb
│   ├── 02_DataWrangling.ipynb
│   ├── 03_FeatureEngineering.ipynb
│   ├── 04_Modeling.ipynb
├── src
│   └── funciones.py
│   └── utils.py
├── reports
│   └── CRISP-DM.pdf
│   └── Proyecto #1.pdf
└── .gitignore
└── README.md
├── requirements.txt

### Descripción breve de cada carpeta: 

1. data/: Datos en bruto (raw) de los datos procesados (curated). 
2. notebooks/: Crea notebooks ordenados por número o por tema para EDA, data 
wrangling y cualquier otro paso relevante de tu pipeline. 
3. src/: Aquí se guardan los scripts Python que contienen funciones o módulos 
reutilizables. 
4. reports/: Aquí irán tus informes, visualizaciones y resultados. 
○ También puedes incluir figures/ para almacenar y referenciar imágenes 
(gráficas, diagramas, etc.). 
5. README.md: Debe ofrecer una visión general clara del proyecto (propósito, estructura, 
instrucciones de uso). 
6. .gitignore: Lista de archivos y carpetas que no quieres incluir en el control de versiones 
(por ejemplo, datos grandes, archivos temporales, etc.). 
7. requirements.txt: Indicando las librerías y versiones que utilizas para que otros (o tú 
mismo, en el futuro) puedan reproducir el entorno.

## Usage Instructions

1. Clonar el repositorio: https://github.com/gabyzumarraga/DS-SP500.git
2. Instalar las librerias requeridas con el siguiente comando:

   ```
   pip install -r requirements.txt
   ```
   
3. Usar los Jupyter notebooks ubicados en la carpeta `notebooks/`
