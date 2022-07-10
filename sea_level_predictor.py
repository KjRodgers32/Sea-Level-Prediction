import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    y = df['CSIRO Adjusted Sea Level']
    x = df['Year']

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x,y)


    # Create first line of best fit
    reg = linregress(x,y)
    x_predict = pd.Series([i for i in range(1880,2051)])
    y_predict = reg.slope * x_predict + reg.intercept
    plt.plot(x_predict,y_predict,'r')


    # Create second line of best fit
    present_df = df.loc[df['Year'] >= 2000]
    present_x = present_df['Year']
    present_y = present_df['CSIRO Adjusted Sea Level']
    present_reg = linregress(present_x,present_y)
    x_predict2 = pd.Series([i for i in range(2000,2051)])
    y_predict2 = present_reg.slope * x_predict2 + present_reg.intercept
    plt.plot(x_predict2,y_predict2,'yellow')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()