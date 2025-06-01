# Title: Program #7
# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

"""
Program #7 (worth double)
Consider one of the following datasets (Athlete Events, Bios, Gas Prices, FIFA, Pokémon).
Write a python program to make various charts from this data.
Include at least one scatterplot, line graph, histogram, pie chart, and box plot.
"""

import pandas as pd
import matplotlib.pyplot as plt


def main():
    file_path = "pokemon_data.csv"

    # Read file in
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return

    # Scatterplot: Attack vs Defense
    fig = plt.figure(figsize=(8, 6))
    plt.scatter(data['Attack'], data['Defense'], alpha=0.7)
    fig.canvas.manager.set_window_title("Figure 1 - Attack vs Defense")
    plt.title('Attack vs Defense')
    plt.xlabel('Attack')
    plt.ylabel('Defense')
    plt.grid(True)
    plt.show()

    # Line graph: Average stats by Generation
    avg_stats = data.groupby('Generation').mean(numeric_only=True)
    fig = plt.figure(figsize=(8, 6))
    for stat in ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']:
        plt.plot(avg_stats.index, avg_stats[stat], label=stat, marker='o')
    fig.canvas.manager.set_window_title("Figure 2 - Average Stats by Generation")
    plt.title('Average Stats by Generation')
    plt.xlabel('Generation')
    plt.ylabel('Stat Value')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Histogram: Distribution of HP
    fig = plt.figure(figsize=(8, 6))
    plt.hist(data['HP'], bins=20)
    fig.canvas.manager.set_window_title("Figure 3 - Distribution of HP")
    plt.title('Distribution of HP')
    plt.xlabel('HP')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # Pie chart: Distribution of Primary Types (Type 1)
    type_counts = data['Type 1'].value_counts()
    fig = plt.figure(figsize=(7, 7))
    plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
    fig.canvas.manager.set_window_title("Figure 4 - Distribution of Primary Types (Type 1)")
    plt.title('Distribution of Primary Types (Type 1)')
    plt.show()

    # Box plot: Distribution of Total Stats
    total_stats = data[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].sum(axis=1)
    fig = plt.figure(figsize=(8, 6))
    plt.boxplot(total_stats, vert=False)
    fig.canvas.manager.set_window_title("Figure 5 - Distribution of Total Stats")
    plt.title('Distribution of Total Stats')
    plt.xlabel('Total Stats')
    plt.grid(True)
    plt.show()


# Call the main function
if __name__ == '__main__':
    main()
