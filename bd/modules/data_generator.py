import bd.modules.preprocessing as pr
from bd.modules.web_scraping import *

pd.set_option('display.max_columns', None)  # Ogni stampa di un dataframe mostrerà tutte le colonne


def expand_time(start, finish, freq):  # Genera orario da start a finish con frequenza
    # formato start e finish: "hh:mm"
    # formato freq: "10min" per 10 minuti e così via
    time_range = pd.date_range(start, finish, freq=freq)
    time_range = time_range.astype(str)
    time = []
    for t in time_range:
        time.append(t[11:16])
    return time


def generate_time(dataset, freq):  # Genera più istanti di tempo a partire dal dataset processato
    df = dataset.iloc[[0, -1]]
    return expand_time(df.iloc[0]['Time'], df.iloc[1]['Time'], freq=freq)


def expand_dataset(dataset, freq):
    # Espande gli istanti di tempo del dataset in base alla frequenza indicata
    time = generate_time(dataset, freq=freq)
    df = pd.DataFrame(columns=dataset.columns)
    df['Time'] = time
    # Effettua la join dei due dataset
    for i in range(0, df['Time'].shape[0]):
        t1 = df['Time'].iloc[i]
        for j in range(0, dataset['Time'].shape[0]):
            t2 = dataset['Time'].iloc[j]
            if t1 == t2:
                df['Temperature'].iloc[i] = dataset['Temperature'].iloc[j]
                df['Humidity'].iloc[i] = dataset['Humidity'].iloc[j]
                df['Wind Speed'].iloc[i] = dataset['Wind Speed'].iloc[j]
                df['Pressure'].iloc[i] = dataset['Pressure'].iloc[j]

    df = pr.prepocessing_generate(df)

    # Genera i dati mancanti
    for column in df.columns:
        df[column].interpolate(method='polynomial', order=2, inplace=True,
                               limit_direction='backward')  # interpolazione polinomiale di secondo grado

    df = df.round(2) # Eliminazione delle cifre superflue

    return df
