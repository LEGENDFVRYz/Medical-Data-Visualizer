import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
df.head(5) # Confirming if the data set is already read.

# Add 'overweight' column
df['overweight'] = (df['weight'] / ((df['height'] * 0.01) ** 2))    # Calculate the BMI
df['overweight'] = (df['overweight'] > 25).astype(int)              # Check if overweight and represent it as int

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)     
df['gluc'] = (df['gluc'] > 1).astype(int)                   
df.head(10)         # Checking if the was normalized correctly


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(
        id_vars = 'cardio',
        value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
        value_name = 'value',
        var_name = 'variable'
    )

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'variable']).value_counts()).reset_index()
    df_cat.rename(columns={0: 'total'}, inplace=True)       # rename the missing column title after counting by


    # Draw the catplot with 'sns.catplot()'
    cat = sns.catplot(
        data = df_cat,
        kind = 'bar',               # Type of the graph
        col = 'cardio',             # Split by cardio, so 2 charts will be the output
        x='variable', y='total',    # X and Y values
        hue = 'value'               # 'value' will be reference for the color
    )

    # Get the figure for the output
    fig = cat.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
