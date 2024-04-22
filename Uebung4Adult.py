import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. Daten laden
df = pd.read_csv('adult.csv')
print("Erste Zeilen des DataFrames:")
print(df.head())

# 2. Transformation von Zeichenketten in numerische Werte
label_encoders = {}
for column in df.columns:
    if df[column].dtype == 'object':
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column].astype(str))
        label_encoders[column] = le

# 3. Ermittlung der optimalen Gruppenanzahl mit der Elbow-Methode
wcss = []
for i in range(1, 11):  # Testen von 1 bis 10 Clustern
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# Wählen Sie die optimale Clusteranzahl basierend auf dem Elbow-Diagramm
optimal_clusters = int(input("Geben Sie die optimale Anzahl von Clustern ein: "))

# 4. Gruppieren des Datensatzes
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
df['Label'] = kmeans.fit_predict(df)

# 5. Speichern der neuen Tabelle in einer CSV-Datei
df.to_csv('adults_labeled.csv', index=False)
print("Neue Tabelle wurde als 'adults_labeled.csv' gespeichert.")
