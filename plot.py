import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Daten einlesen
df = pd.read_csv("iris.csv")

# Scatter Plot erstellen
plt.figure(figsize=(10, 6))  # Setze die Größe des Plots
scatter = sns.scatterplot(x='sepal.length', y='sepal.width', hue='species', data=df, palette='bright')
scatter.set_title('Scatter Plot von Sepal Length gegen Sepal Width nach Species')
scatter.set_xlabel('Sepal Length')
scatter.set_ylabel('Sepal Width')
plt.legend(title='Species')
plt.show()
