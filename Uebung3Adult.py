import pandas as pd

# 1. Daten einlesen: Lade den Datensatz 'adult.csv' in einen Pandas DataFrame.
df = pd.read_csv("adult.csv")
# Hinweis: Stellen Sie sicher, dass der Pfad zur Datei korrekt ist.

# 2. Datensatz erkunden: Zeige die ersten 5 und die letzten 5 Zeilen des DataFrames an.
print("Erste 5 Zeilen des DataFrames:")
print(df.head(5))  # Zeigt die ersten 5 Zeilen an
print("\nLetzte 5 Zeilen des DataFrames:")
print(df.tail(5))  # Zeigt die letzten 5 Zeilen an

# 3. Zusammenfassung: Erhalte eine Zusammenfassung des DataFrames.
print("\nZusammenfassung des DataFrames:")
df.info()
# Diese Funktion zeigt eine Zusammenfassung, einschließlich der Datentypen und der Anzahl der Nicht-Null-Einträge.

#-------------------------------------------------------------


# 1. Spalten auswählen: Wähle die Spalten 'age', 'occupation' und 'income' aus und zeige die ersten 10 Zeilen an.
selected_columns = df[['age', 'occupation', 'income']].head(10)
print("\nAusgewählte Spalten - Erste 10 Zeilen:")
print(selected_columns)

# 2. Bedingte Auswahl: Filtere die Daten, um nur die Zeilen anzuzeigen, bei denen das 'income' '>50K' ist.
high_income_rows = df[df['income'] == '>50K']
print("\nZeilen mit 'income' > 50K:")
print(high_income_rows)

# 3. Mehrere Bedingungen: Finde alle Einträge, bei denen das 'age' größer als 30 ist und das 'education' 'Bachelors' ist.
older_bachelors = df[(df['age'] > 30) & (df['education'] == 'Bachelors')]
print("\nEinträge mit 'age' > 30 und 'education' Bachelors:")
print(older_bachelors)

#-----------------------------------------------------------------------

# 1. Neue Spalte hinzufügen: Berechne das Alter in Jahrzehnten und füge es als neue Spalte 'age_decade' hinzu.
df['age_decade'] = df['age'] / 10

# 2. Werte ändern: Ersetze in der 'income'-Spalte die Werte '>50K' und '<=50K' durch 'high' und 'low'.
df['income'] = df['income'].replace({'>50K': 'high', '<=50K': 'low'})

# 3. Zeilen löschen: Entferne alle Zeilen, in denen die 'occupation' 'Unknown' ist.
df = df[df['occupation'] != 'Unknown']

#---------------------------------------------------------------------------

# 1. Deskriptive Statistiken: Zeige die deskriptiven Statistiken für die 'age' Spalte.
age_stats = df['age'].agg(['min', 'max'])
print("\nDeskriptive Statistiken für 'age':")
print(age_stats)

# 2. Gruppieren und Aggregieren: Berechne den Durchschnitt von 'age', gruppiert nach 'income'.
average_age_by_income = df.groupby('income')['age'].mean()
print("\nDurchschnittsalter nach 'income':")
print(average_age_by_income)

# 3. Einzigartige Werte: Finde alle einzigartigen Werte in der 'education'-Spalte.
unique_education = df['education'].unique()
print("\nEinzigartige Werte in 'education':")
print(unique_education)

#---------------------------------------------------------------------------------