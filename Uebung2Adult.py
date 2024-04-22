import pandas as pd


#Übung 1: Daten einlesen und inspizieren--------------------------------------------------

# Daten einlesen: Lade den Datensatz adult.csv in einen Pandas DataFrame
df = pd.read_csv("adult.csv")

# Datensatz erkunden: Zeige die ersten 5 und die letzten 5 Zeilen des DataFrames an
print("Erste 5 Zeilen des DataFrames:")
print(df.head(5))  # Zeigt die ersten 5 Zeilen an

print("\nLetzte 5 Zeilen des DataFrames:")
print(df.tail(5))  # Zeigt die letzten 5 Zeilen an

# Zusammenfassung: Erhalte eine Zusammenfassung des DataFrames
print("\nZusammenfassung des DataFrames:")
df.info()

# Übung 2: Auswahl und Filterung----------------------------------------------------

import pandas as pd

# Daten einlesen
df = pd.read_csv("adult.csv")

# Spalten auswählen: Wähle die Spalten age, occupation und income aus und zeige die ersten 10 Zeilen an
selected_columns = df[['age', 'occupation', 'income']].head(10)
print("Ausgewählte Spalten (age, occupation, income) - Erste 10 Zeilen:")
print(selected_columns)

# Bedingte Auswahl: Filtere die Daten, um nur die Zeilen anzuzeigen, bei denen das income '>50K' ist
high_income_rows = df[df['income'] == '>50K']
print("\nZeilen, bei denen das income '>50K' ist:")
print(high_income_rows)

# Mehrere Bedingungen: Finde alle Einträge, bei denen das age größer als 30 ist und das education 'Bachelors' ist
older_bachelors = df[(df['age'] > 30) & (df['education'] == 'Bachelors')]
print("\nEinträge mit age > 30 und education 'Bachelors':")
print(older_bachelors)


# Übung 3: Datenbearbeitung-------------------------------------------------

import pandas as pd

# Daten einlesen
df = pd.read_csv("adult.csv")

# Neue Spalte hinzufügen: Berechne das Alter in Jahrzehnten und füge es als neue Spalte age_decade hinzu
df['age_decade'] = df['age'] / 10
print("DataFrame mit neuer Spalte 'age_decade':")
print(df.head())

# Werte ändern: Ersetze in der income-Spalte die Werte '>50K' und '<=50K' durch 'high' und 'low'
df['income'] = df['income'].replace({'>50K': 'high', '<=50K': 'low'})
print("\nDataFrame mit geänderten 'income'-Werten:")
print(df.head())

# Zeilen löschen: Entferne alle Zeilen, in denen die occupation 'Unknown' ist
df = df[df['occupation'] != 'Unknown']
print("\nDataFrame nach Entfernen von Zeilen mit occupation 'Unknown':")
print(df.head())


# Übung 4: Einfache Datenanalyse----------------------------------------------

import pandas as pd

# Daten einlesen
df = pd.read_csv("adult.csv")

# Deskriptive Statistiken: Zeige die deskriptiven Statistiken (Min, Max) für die age Spalte
age_min_max = df['age'].agg(['min', 'max'])
print("Minimales und maximales Alter:")
print(age_min_max)

# Gruppieren und Aggregieren: Berechne den Durchschnitt von age, gruppiert nach income
average_age_by_income = df.groupby('income')['age'].mean()
print("\nDurchschnittsalter, gruppiert nach Einkommen:")
print(average_age_by_income)

# Einzigartige Werte: Finde alle einzigartigen Werte in der education-Spalte
unique_education = df['education'].unique()
print("\nEinzigartige Bildungsabschlüsse:")
print(unique_education)

