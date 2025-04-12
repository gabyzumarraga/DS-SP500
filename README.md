# Proyecto DS - Modelo Predictivo para Anticipar Movimientos en las Acciones del Índice S&P 500

El índice S&P 500, (Standard & Poor’s 500), es un índice sobre el rendimiento de las 500 mayores empresas que cotizan en Estados Unidos (por capitalización de mercado). Es un indicador clave de la salud económica de la 
bolsa estadounidense ya que abarca distintos tipos de industrias, como tecnología, atención médica, servicios financieros, bienes de consumo y energía, seleccionadas por su tamaño, liquidez y representatividad económica.  


El objetivo principal de este proyecto es desarrollar un modelo predictivo que permita anticipar si el precio de una acción del índice S&P 500 subirá o bajará en función de datos históricos, como precios de apertura, cierre, máximos, mínimos y otras variables derivadas.


##  Contexto 

**Hipótesis principal:** Los movimientos históricos de precios pueden 
revelar tendencias repetitivas o correlaciones significativas que permitan prever 
cambios futuros en los precios de las acciones en el mercado bursatil. 

**Qué necesitas comprobar o resolver:** Identificar patrones relevantes en los precios y volúmenes que puedan ayudar a entender mejor el comportamiento de los precios de las acciones en el mercado. 

**Pregunta de investigación:** ¿Qué patrones de precios se observan en 
las acciones de las empresas del S&P 500, y cómo pueden usarse para anticipar 
movimientos futuros?

**Relevancia:** Este analisis puede ayudar a los stakeholders, accionistas o inversionistas a:
1. Tomar decisiones informadas: Ayuda a los inversores y analistas financieros a tomar decisiones más fundamentadas sobre la compra o venta de acciones. Igualmente puede ser utilizado por instituciones financieras, fondos de inversión o traders individuales para mejorar sus rendimientos al conocer el comportamiento o tendencia de las acciones.
2. Gestion de riesgos: permite identificar patrones que podrían reducir el riesgo asociado con las inversiones en el mercado bursátil.
3. Optimizar estrategias: Facilita la creación de estrategias de trading automatizadas basadas en predicciones de movimientos del mercado.


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
├── data
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

### Descripción breve de cada carpeta: 

1. data/: Datos en bruto (raw), datos limpios (clean) y datos procesados (curated). 
2. instrucciones/: Documentos que indican las instrucciones de cada etapa del proyecto. 
3. notebooks/: Notebooks utilizados. Estan ordenados pos tema para EDA, data 
wrangling y Modeling. 
4. src/: Aquí se guardan los scripts Python que contienen funciones o módulos 
reutilizables. 
5. reports/: Informes, visualizaciones y resultados. 
6. README.md: Visión general clara del proyecto (propósito, estructura, 
instrucciones de uso). 
7. .gitignore: Lista de archivos y carpetas que se excluiran en el control de versiones 
8. requirements.txt: Indica las librerías y versiones que se utilizan en el proyecto.

## Usage Instructions

1. Clonar el repositorio: https://github.com/gabyzumarraga/DS-SP500.git
2. Instalar las librerias requeridas con el siguiente comando:

   ```
   pip install -r requirements.txt
   ```
3. Descargar del dataset de Kaggle: https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks?select=sp500_companies.csv
4. Usar los Jupyter notebooks ubicados en la carpeta `notebooks/` en el mismo orden

