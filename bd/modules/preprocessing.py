import seaborn as sns
import pandas as pd

pd.set_option('display.max_columns', None)  # Ogni stampa di un dataframe mostrerà tutte le colonne
sns.color_palette("deep")  # Ogni grafico userà lo stile di colori 'deep'


def temp_to_int(temp):  # estrae dalla stringa temperatura un intero
    n = int(temp[:2])
    return n


def format_pressure(pr):
    p = float(pr[:5])
    return p


def format_date(d):
    if len(d) == 7:
        return '0' + d
    return d


def format_humidity(hum):
    if len(hum) == 6:
        h = int(hum[:3])
    if len(hum) == 5:
        h = int(hum[:2])
    if len(hum) == 4:
        h = int(hum[:1])
    return h


def format_wind(ws):
    if len(ws) == 6:
        w = int(ws[:2])
    if len(ws) == 7:
        w = int(ws[:3])
    if len(ws) == 8:
        w = int(ws[:4])
    return w


def time_conversion(s):
    if s[-2:] == "AM":
        if s[: 2] == '12':
            a = str('00' + s[2: 6])
        else:
            a = s[: -2]
    else:
        if s[:2] == '12':
            a = s[:-2]
        else:
            a = str(int(s[:2]) + 12) + s[2: 6]
    return a.strip()


def preprocessing(dataframe):  # preprocessing necessario per analizzare il dataframe (Pandas)
    dataframe = dataframe[dataframe['Temperature'] != '']  # rimuove i valori 'nulli'
    dataframe['Temperature'] = dataframe['Temperature'].apply(func=temp_to_int)  # converte la stringa con la
    # temperatura in intero
    dataframe['Time'] = dataframe['Time'].apply(func=format_date)  # aggiunge uno zero all'inizio di alcune date
    dataframe['Time'] = dataframe['Time'].apply(func=time_conversion)  # converte il tempo in AM/PM nel tempo in HH/mm
    dataframe['Pressure'] = dataframe['Pressure'].apply(func=format_pressure)
    dataframe['Humidity'] = dataframe['Humidity'].apply(func=format_humidity)
    dataframe['Wind Speed'] = dataframe['Wind Speed'].apply(func=format_wind)
    dataframe['Condition'] = dataframe['Condition'].astype(str)  # trasforma le condition in stringhe

    dataframe = dataframe.drop(columns="Precip.")
    dataframe = dataframe.drop(columns="Wind Gust")
    dataframe = dataframe.drop(columns="Wind")
    dataframe = dataframe.drop(columns="Dew Point")

    return dataframe


def preprocessing2(dataframe):  # Non fa trasformazioni, effettua solo il drop delle colonne
    dataframe = dataframe.drop(columns="Precip.")
    dataframe = dataframe.drop(columns="Wind Gust")
    dataframe = dataframe.drop(columns="Wind")
    dataframe = dataframe.drop(columns="Dew Point")

    return dataframe


def preprocessing_italy(dataframe):  # preprocessing necessario per analizzare il dataframe (Pandas)
    dataframe = dataframe[dataframe['Temperature'] != '']  # rimuove i valori 'nulli'
    dataframe['Temperature'] = dataframe['Temperature'].apply(func=temp_to_int)  # converte la stringa con la
    # temperatura in intero
    dataframe['Pressure'] = dataframe['Pressure'].apply(func=format_pressure)
    dataframe['Humidity'] = dataframe['Humidity'].apply(func=format_humidity)
    dataframe['Wind Speed'] = dataframe['Wind Speed'].apply(func=format_wind)

    dataframe = dataframe.drop(columns="Precip.")
    dataframe = dataframe.drop(columns="Wind Gust")
    dataframe = dataframe.drop(columns="Wind")
    dataframe = dataframe.drop(columns="Dew Point")

    return dataframe


def prepocessing_generate(df):  # Metodo usato nel data_generator, trasforma alcune colonne in numeriche da object
    df['Temperature'] = pd.to_numeric(df['Temperature'])
    df['Humidity'] = pd.to_numeric(df['Humidity'])
    df['Wind Speed'] = pd.to_numeric(df['Wind Speed'])
    df['Pressure'] = pd.to_numeric(df['Pressure'])

    return df
