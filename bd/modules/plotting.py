import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')


def plot_temperature_today(df):
    sns_plot = sns.lineplot(data=df, x="Time", y="Temperature")
    plt.xticks(rotation=45)
    fig = sns_plot.get_figure()
    fig.set_size_inches(15, 8)
    fig.suptitle('Temperature over time')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°F)')
    fig.savefig("../out/today_temperature_chart.png")
    plt.clf()


def plot_humidity_today(df):
    sns_plot = sns.lineplot(data=df, x="Time", y="Humidity")
    plt.xticks(rotation=45)
    fig = sns_plot.get_figure()
    fig.set_size_inches(15, 8)
    fig.suptitle('Humidity over time')
    plt.xlabel('Time')
    plt.ylabel('Humidity (%)')
    fig.savefig("../out/today_humidity_chart.png")
    plt.clf()


def plot_wind_speed_today(df):
    sns_plot = sns.lineplot(data=df, x="Time", y="Wind Speed")
    plt.xticks(rotation=45)
    fig = sns_plot.get_figure()
    fig.set_size_inches(15, 8)
    fig.suptitle('Wind Speed over time')
    plt.xlabel('Time')
    plt.ylabel('Wind Speed (mph)')
    fig.savefig("../out/today_wind_speed_chart.png")
    plt.clf()


def plot_pressure_today(df):
    sns_plot = sns.lineplot(data=df, x="Time", y="Pressure")
    plt.xticks(rotation=45)
    fig = sns_plot.get_figure()
    fig.set_size_inches(15, 8)
    fig.suptitle('Pressure over time')
    plt.xlabel('Time')
    plt.ylabel('Pressure (in)')
    fig.savefig("../out/today_pressure_chart.png")
    plt.clf()


def plot_condition_today(df):
    plot = df.groupby('Condition').size().plot(kind='pie', autopct='%.2f')
    fig = plot.get_figure()
    fig.set_size_inches(15, 8)
    fig.suptitle('Conditions today')
    frame1 = plt.gca()
    frame1.axes.get_yaxis().set_visible(False)
    fig.savefig("../out/today_condition_chart.png")
    plt.clf()
