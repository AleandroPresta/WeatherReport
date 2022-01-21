"""
web_scraping è una libreria interna all'applicazione che si occupa, tramite passi intermedi di recuperare i dati
metereologici dal web (wunderground.com/history) e di restituirli sotto forma di Dataframe Pandas
"""

import pandas as pd
from selenium.webdriver import Chrome
from pyvirtualdisplay import Display
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import date

chromedriver_path = '/home/aleandro/PycharmProjects/ProgettoBD/chromedriver'

sensors_italy = [
    'LIBP',
    'LIBF',
    'LICA',
    'LIRN',
    'LIPE',
    'LJPZ',
    'LIRA',
    'LIMJ',
    'LIML',
    'LIPY',
    'LIBF',
    'LIMF',
    'LIBD',
    'LIEE',
    'LICJ',
    'LIRQ',
    'LIPB',
    'LIRZ',
    'LIMW',
    'LIPZ']

cities_italy = [
    "L'Aquila",
    "Potenza",
    "Catanzaro",
    "Napoli",
    "Bologna",
    "Trieste",
    "Roma",
    "Genova",
    "Milano",
    "Ancona",
    "Campobasso",
    "Torino",
    "Bari",
    "Cagliari",
    "Palermo",
    "Firenze",
    "Bolzano",
    "Perugia",
    "Aosta",
    "Venezia"
]

"""Non per tutte le regioni è disponibile un sensore nel capoluogo:
        
        Abruzzo => Pescara LIBP (più vicino a L'Aquila)
        Basilicata => Foggia LIBF (più vicino a Potenza)
        Calabria => Lamezia Terme LICA (più vicino a Catanzaro)
        Campania => Napoli LIRN
        Emilia-Romagna => Bologna LIPE
        Friuli Venezia-Giulia => Piran, Slovenia LJPZ (più vicino a Trieste)
        Lazio => Roma LIRA
        Liguria => Genova LIMJ
        Lombardia => Milano LIML
        Marche => Ancona LIPY
        Molise => Foggia LIBF (più vicino a Campobasso)
        Piemonte => Torino LIMF
        Puglia => Bari LIBD
        Sardegna => Cagliari LIEE
        Sicilia => Palermo LICJ
        Toscana => Firenze LIRQ
        Trentino => Bolzano LIPB (più vicina a Trento)
        Umbria => Perugia LIRZ
        Valle d'Aosta => Aosta LIMW
        Veneto => Venezia LIPZ

"""


def create_url(sensor_name, requested_date):  # Crea l'URL da cui estrarremo la tabella con i dati metereologici
    url = 'https://www.wunderground.com/history/daily/' + sensor_name + '/date/' + requested_date
    return url


def today_date():  # Ottiene la data di oggi nel formato richiesto (YYYY-mm-dd)
    today = date.today()
    d = today.strftime("%Y-%m-%d")
    return d


def today_date_history(year):  # Ottiene la data di oggi ma di anni precedenti
    today = date.today()
    d = today.strftime(str(year) + "-%m-%d")
    print("WeatherReport> Analyzing date: " + d)
    return d


def get_daily_weather_table(sensor_name, selected_date):
    display = Display(visible=0, size=(800, 600))
    display.start()

    driver = Chrome(chromedriver_path)
    print("WeatherReport> Loading data from " + sensor_name + " in date " + selected_date)
    driver.get(create_url(sensor_name, selected_date))

    tables = WebDriverWait(driver, 20) \
        .until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mat-table.cdk-table.mat-sort.ng-star-inserted")))

    for table in tables:
        new_table = pd.read_html(table.get_attribute('outerHTML'))
        new_table = new_table[0].dropna()
        print("WeatherReport> Table loaded in a pandas dataframe")

    driver.quit()
    return new_table


def get_today_weather_table(sensor_name):
    # Evita che si apra una nuova pagina del browser ogni volta che si fa una richiesta
    display = Display(visible=0, size=(800, 600))
    display.start()

    driver = Chrome(chromedriver_path)
    today = today_date()
    print("WeatherReport> Loading data from " + sensor_name + " in date " + today)
    driver.get(create_url(sensor_name, today))

    tables = WebDriverWait(driver, 20) \
        .until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mat-table.cdk-table.mat-sort.ng-star-inserted")))

    for table in tables:
        new_table = pd.read_html(table.get_attribute('outerHTML'))
        new_table = new_table[0].dropna()
        print("WeatherReport> Table loaded in a pandas dataframe")

    driver.quit()
    return new_table


def get_weather_now(sensor_name):
    # Evita che si apra una nuova pagina del browser ogni volta che si fa una richiesta
    display = Display(visible=0, size=(800, 600))
    display.start()

    driver = Chrome(chromedriver_path)
    today = today_date()
    print("WeatherReport> Loading data from " + sensor_name + " in date " + today)
    driver.get(create_url(sensor_name, today))

    tables = WebDriverWait(driver, 20) \
        .until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mat-table.cdk-table.mat-sort.ng-star-inserted")))

    for table in tables:
        new_table = pd.read_html(table.get_attribute('outerHTML'))
        new_table = new_table[0].dropna()
        print("WeatherReport> Table loaded in a pandas dataframe")

    driver.quit()
    return new_table.tail(1)


def get_weather_now_italy():
    # Evita che si apra una nuova pagina del browser ogni volta che si fa una richiesta
    display = Display(visible=0, size=(800, 600))
    display.start()

    frames = []
    today = today_date()

    for i in range(0, len(sensors_italy)):
        print("WeatherReport> Loading data from " + sensors_italy[i] + " in date " + today)
        driver = Chrome(chromedriver_path)
        driver.get(create_url(sensors_italy[i], today))

        tables = WebDriverWait(driver, 20) \
            .until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "mat-table.cdk-table.mat-sort.ng-star-inserted")))

        for table in tables:
            new_table = pd.read_html(table.get_attribute('outerHTML'))
            new_table = new_table[0].dropna()
            new_table = new_table.drop('Time', 1)
            new_table.insert(loc=0, column='City', value=cities_italy[i])
            print("WeatherReport> Table loaded in a pandas dataframe")

            frames.append(new_table.tail(1))
            print("WeatherReport> Table added to frames")

        driver.quit()

    df = pd.concat(frames)
    return df
