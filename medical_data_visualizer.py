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
        data = df_cat,              # import the data frame
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
    df_heat = df[df['ap_lo'] <= df['ap_hi']]                        # diastolic pressure is higher than systolic
    df_heat = df_heat[df['height'] >= df['height'].quantile(0.025)] # height is less than the 2.5th percentile
    df_heat = df_heat[df['height'] <= df['height'].quantile(0.975)] # height is more than the 97.5th percentile
    df_heat = df_heat[df['weight'] >= df['weight'].quantile(0.025)] # weight is less than the 2.5th percentile
    df_heat = df_heat[df['weight'] <= df['weight'].quantile(0.975)] # weight is more than the 97.5th percentile

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.ones_like(df_heat.corr(), dtype=bool)   # Create a copy of corr where all values is ones
    mask = np.triu(mask, 0)                           # mask out correct portion of the triangle


    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(
        data = corr,                    # import data
        mask = mask,                    # masking the heatmap to look like a triangle
        vmax = 0.30,                    # max val for colors
        annot = True,                   # show text in each boxes
        annot_kws = {'fontsize' : 5},   # modifying fontsize
        fmt=".1f",                      # format annot in one digit after the decimal point
        linewidths = 0.2,               # line width that closely to reference
        linecolor = 'white',            # color white to make it look like a gap
        cbar_kws = {"shrink" : .5},     # shrink color bar
        square = True                   # making sure each boxes is square
    )


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
