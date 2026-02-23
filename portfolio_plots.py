import matplotlib
matplotlib.use('Agg')  
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
plt.close('all')

# Load your data
df = pd.read_csv("movies.csv")  # replace with your CSV file

# Clean Gross column
df['Gross'] = df['Gross'].replace('[\$,]', '', regex=True)
df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce')

# --- Top 10 Directors ---
director_rating = df.groupby('Director')['IMDB_Rating'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=director_rating.index, y=director_rating.values)
plt.xticks(rotation=45)
plt.title("Top 10 Directors by Average IMDB Rating")
plt.ylabel("Average IMDB Rating")
plt.tight_layout()
plt.savefig("top_directors.png")
plt.close()

# --- Top 10 Grossing Movies ---
top_grossing = df.sort_values(by='Gross', ascending=False)[['series_title', 'Gross']].head(10)
plt.figure(figsize=(10,6))
sns.barplot(x='series_title', y='Gross', data=top_grossing)
plt.xticks(rotation=45)
plt.title("Top 10 Grossing Movies")
plt.ylabel("Gross ($)")
plt.tight_layout()
plt.savefig("top_grossing.png")
plt.close()

# --- Top 10 Genres ---
df['Genre_List'] = df['Genre'].str.split(', ')
all_genres = df.explode('Genre_List')
top_genres = all_genres['Genre_List'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_genres.index, y=top_genres.values)
plt.xticks(rotation=45)
plt.title("Top 10 Movie Genres")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("top_genres.png")
plt.close()
