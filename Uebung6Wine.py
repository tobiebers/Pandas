import pandas as pd

# Datensatz korrekt mit Semikolon als Trennzeichen laden
df = pd.read_csv('wine.csv', delimiter=';')

# Erste und letzte 5 Zeilen anzeigen
print("Erste 5 Zeilen des DataFrames:")
print(df.head())
print("\nLetzte 5 Zeilen des DataFrames:")
print(df.tail())

# Anzahl der Zeilen und Spalten sowie die Datentypen der Spalten überprüfen
print("\nAnzahl der Zeilen und Spalten:", df.shape)
print("\nDatentypen der Spalten:")
print(df.dtypes)
#---------------------------------------------------

# Überprüfen auf fehlende Werte
print("\nAnzahl fehlender Werte pro Spalte:")
print(df.isnull().sum())

# Fehlende Werte behandeln (hier: Entfernen)
df.dropna(inplace=True)  # Oder ersetzen mit df.fillna(Methode)

# Duplikate entfernen
df.drop_duplicates(inplace=True)

# Konvertieren von Datentypen, falls notwendig
# Beispiel: df['column_name'] = pd.to_numeric(df['column_name'], errors='coerce')

#---------------------------------------------------------------


# Statistische Kennzahlen für jede numerische Spalte
print("\nStatistische Kennzahlen für numerische Spalten:")
print(df.describe())

# Korrelation zwischen der Qualität des Weins und anderen chemischen Eigenschaften
correlation = df.corr()
print("\nKorrelation zwischen Qualität und anderen chemischen Eigenschaften:")
print(correlation['quality'].sort_values())

#------------------------------------------------------------

import matplotlib.pyplot as plt

# Histogramme für einige chemische Eigenschaften
df['alcohol'].hist()
plt.title('Verteilung des Alkoholgehalts')
plt.xlabel('Alkoholgehalt')
plt.ylabel('Häufigkeit')
plt.show()

# Streudiagramm für die Beziehung zwischen Alkoholgehalt und Qualität
plt.scatter(df['alcohol'], df['quality'])
plt.title('Alkoholgehalt vs. Qualität des Weins')
plt.xlabel('Alkoholgehalt')
plt.ylabel('Qualität')
plt.show()

# Boxplots für die Qualität in Bezug auf verschiedene chemische Eigenschaften
df.boxplot(column='quality', by='alcohol')
plt.title('Boxplot der Qualität basierend auf Alkoholgehalt')
plt.xlabel('Qualität')
plt.ylabel('Alkoholgehalt')
plt.show()


#-------------------------------------------------------