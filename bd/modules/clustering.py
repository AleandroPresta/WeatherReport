from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SQLContext
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("darkgrid")
plt.rcParams.update({"grid.linewidth": 0.5, "grid.alpha": 0.5})


def my_kmeans_cities(df, k):
    sc = SparkContext("local[2]", "ClusteringExample")
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    df = spark.createDataFrame(df)

    sqlContext = SQLContext(sc)

    FEATURES_COL = ["Temperature", "Humidity", "Wind Speed", "Pressure"]
    for col in df.columns:
        if col in FEATURES_COL:
            df = df.withColumn(col, df[col].cast('float'))

    vecAssembler = VectorAssembler(inputCols=FEATURES_COL, outputCol="features")
    df_kmeans = vecAssembler.transform(df).select('City', 'features')

    kmeans = KMeans().setK(k).setSeed(1).setFeaturesCol("features")
    model = kmeans.fit(df_kmeans)
    centers = model.clusterCenters()

    print("Cluster Centers: ")
    for center in centers:
        print(center)

    transformed = model.transform(df_kmeans).select('City', 'prediction')
    rows = transformed.collect()
    print(rows[:3])
    df_pred = sqlContext.createDataFrame(rows)

    df_pred = df_pred.join(df, 'City')

    df = df_pred.toPandas()

    sns_plot = sns.pairplot(data=df, hue="prediction")
    sns.set(rc={'figure.figsize': (15, 8)})
    sns_plot.figure.savefig("../out/clustering_plot.png")
    sc.stop()
    return df
