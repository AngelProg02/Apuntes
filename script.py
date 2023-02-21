import time

import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta 
import dateutil
import requests
import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url_notasCortes = "https://www.juntadeandalucia.es/economiaconocimientoempresasyuniversidad/sguit/g_not_cor_anteriores.php"
# Lectura de la página
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
url_notasCortes = requests.get(url_notasCortes,headers=headers)

if url_notasCortes.status_code == 200:
    url_notasCortes = BeautifulSoup(url_notasCortes.text, "html.parser")
    
    # Muestra el contenido de la web HTML
    #print(transfermarkt_web.prettify())
    

    # Obtenemos la tabla
    #Recorrer la ruta de la tabla con el comando find --> que sea una etiqueta div con un id y dentro de esta volvemos a filtrar
    table = url_notasCortes.find("table", {"class" : "table table-striped"})
    url_notasCortes_table = pd.read_html(str(table), header=0, encoding="utf-8", decimal=",", thousands=".")[0]
    url_notasCortes_table = url_notasCortes_table.iloc[15:20,[1,2,3,4,5,6]]
    nombre_columnas = ["Titulación: ","NotaCorte - Bachiller ", "Titulados Universitarios ",">25 ",">40 ",">45 "]
    #Suma al rango cada vez que se ejecuta y hace las columnas
    indice_columna = [1,2,3,4,5,6]
    #Bucle for para añadir el nombre de las columnas a los array y el índice con el incremento
    for indice in range(0,5):
       url_notasCortes_table[nombre_columnas[indice]] = url_notasCortes_table[url_notasCortes_table.columns[indice_columna[indice]]]
       print(url_notasCortes_table[nombre_columnas[indice]])
    # Muestra el contenido de la tabla HTML
    #La función de panda pd.read_html(...) como maquetamos y señalamos las cosas
  