import pandas as pd
import matplotlib
matplotlib.use('Agg')  # safe backend for Mac
import matplotlib.pyplot as plt
import os

# Load CSV
csv_file = 'movies.csv'
df = pd.read_csv(csv_file)
df.columns = [c.strip() for c in df.columns]

# Make output folder
if not os.path.exists('output'):
    os.makedirs('output')

print("Columns in CSV:", df.columns.tolist())

# Top grossing plot
gross_col = None
title_col = None
for c in df.columns:
    if 'gross' in c.lower() or 'revenue' in c.lower():
        gross_col = c
    if 'title' in c.lower():
        title_col = c

if gross_col and title_col:
    top_grossing = df.sort_values(by=gross_col, ascending=False)[[title_col, gross_col]].head(10)
    plt.figure(figsize=(10,6))
    plt.barh(top_grossing[title_col], top_grossing[gross_col])
    plt.xlabel(gross_col)
    plt.title('Top 10 Highest Grossing Movies')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('output/top_grossing.png')
    plt.close()
    print("Top grossing plot saved to output/top_grossing.png")
else:
    print("Could not find suitable columns for gross/title plot.")

# IMDB rating distribution
rating_col = None
for c in df.columns:
    if 'rating' in c.lower():
        rating_col = c

if rating_col:
    plt.figure(figsize=(8,6))
    plt.hist(df[rating_col], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel(rating_col)
    plt.ylabel('Count')
    plt.title('Distribution of IMDB Ratings')
    plt.tight_layout()
    plt.savefig('output/rating_distribution.png')
    plt.close()
    print("IMDB rating distribution saved to output/rating_distribution.png")
else:
    print("Could not find rating column for plot.")

# Save summary stats
summary_file = 'output/summary_stats.csv'
df.describe(include='all').to_csv(summary_file)
print("Summary stats saved to", summary_file)
