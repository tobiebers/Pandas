import pandas as pd

#Übung 1-------------------------------------

# Daten einlesen: Lade den Datensatz iris.csv in einen Pandas DataFrame
df = pd.read_csv("iris.csv")

# Datensatz erkunden: Zeige die ersten und die letzten Zeilen des DataFrames an
print("Erste Zeilen des DataFrames:")
print(df.head())  # Zeigt die ersten 5 Zeilen an

print("\nLetzte Zeilen des DataFrames:")
print(df.tail())  # Zeigt die letzten 5 Zeilen an

# Zusammenfassung: Erhalte eine Zusammenfassung des DataFrames
print("\nZusammenfassung des DataFrames:")
df.info()

#Übung 2----------------------------------

import pandas as pd

import pandas as pd

# Daten einlesen
df = pd.read_csv("iris.csv")

# Spalten auswählen: Wähle die Spalten sepal.length und sepal.width aus und zeige die ersten 10 Zeilen an
selected_columns = df[['sepal.length', 'sepal.width']].head(10)
print("Ausgewählte Spalten (sepal.length, sepal.width) - Erste 10 Zeilen:")
print(selected_columns)

# Bedingte Auswahl: Filtere die Daten, um nur die Zeilen anzuzeigen, bei denen die species 'Setosa' ist
setosa_rows = df[df['species'] == 'Setosa']
print("\nZeilen, bei denen die species 'Setosa' ist:")
print(setosa_rows)

# Mehrere Bedingungen: Finde alle Einträge, bei denen die petal.length größer als 1.5 ist und die species 'Versicolor' ist
versicolor_large_petals = df[(df['petal.length'] > 1.5) & (df['species'] == 'Versicolor')]
print("\nEinträge mit petal.length > 1.5 und species 'Versicolor':")
print(versicolor_large_petals)


# Übung 3----------------------------------------------

import pandas as pd

# Daten einlesen
df = pd.read_csv("iris.csv")

# Neue Spalte hinzufügen: Berechne die Fläche des Sepal (Sepal Length * Sepal Width) und füge sie als neue Spalte hinzu
df['sepal_area'] = df['sepal.length'] * df['sepal.width']
print("DataFrame mit neuer Spalte 'sepal_area':")
print(df.head())

# Werte ändern: Ersetze in der species-Spalte die Werte 'Setosa', 'Versicolor' und 'Virginica' durch 'S', 'Ve' und 'Vi'
df['species'] = df['species'].replace({'Setosa': 'S', 'Versicolor': 'Ve', 'Virginica': 'Vi'})
print("\nDataFrame mit geänderten 'species'-Werten:")
print(df.head())

# Zeilen löschen: Entferne alle Zeilen, in denen die sepal.length kleiner als 4.5 ist
df = df[df['sepal.length'] >= 4.5]
print("\nDataFrame nach Entfernen von Zeilen mit sepal.length < 4.5:")
print(df.head())


#übung 4 ---------------------------------

import pandas as pd

# Daten einlesen
df = pd.read_csv("iris.csv")

# Deskriptive Statistiken: Zeige die deskriptiven Statistiken (Min, Max) für jede numerische Spalte
min_max_stats = df.describe().loc[['min', 'max']]
print("Deskriptive Statistiken (Min, Max) für jede numerische Spalte:")
print(min_max_stats)

# Gruppieren und Aggregieren: Berechne den Durchschnitt von sepal.length, gruppiert nach species
average_sepal_length = df.groupby('species')['sepal.length'].mean()
print("\nDurchschnitt von sepal.length, gruppiert nach species:")
print(average_sepal_length)

# Einzigartige Werte: Finde alle einzigartigen Werte in der species-Spalte
unique_species = df['species'].unique()
print("\nEinzigartige Werte in der species-Spalte:")
print(unique_species)
