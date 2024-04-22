import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. Daten laden
df = pd.read_csv('wine.csv')
print("Erste Zeilen des DataFrames:")
print(df.head())

# 2. Überführen aller nichtnumerischen Werte in numerische
label_encoders = {}
for column in df.columns:
    if df[column].dtype == object:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le

# 3. Ermittlung der optimalen Clusteranzahl mit der Elbow-Methode
wcss = []
for i in range(1, 11):  # Testen von 1 bis 10 Clustern
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)

# Automatische Ermittlung des Elbow Points
wcss_diff = np.diff(wcss)  # Erste Differenz der WCSS-Werte
wcss_diff2 = np.diff(wcss_diff)  # Zweite Differenz der WCSS-Werte
optimal_clusters = np.argmax(wcss_diff2) + 2  # Index des größten Knickpunkts + 2, da zweite Differenz

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.axvline(x=optimal_clusters, color='red', linestyle='--')
plt.show()

print(f"Automatisch bestimmte optimale Clusteranzahl: {optimal_clusters}")

# 4. Clustern der Daten
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
df['Label'] = kmeans.fit_predict(df)

# Ausgabe der ersten Zeilen des geclusterten DataFrames zur Überprüfung
print("\nGeclusterte Daten:")
print(df.head())
