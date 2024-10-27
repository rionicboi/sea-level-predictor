import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Original Data", color="blue")
    # Create first line of best fit
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    
    x_extended = range(df["Year"].min(), 2051)
    y_pred = result.slope * x_extended + result.intercept
    plt.plot(x_extended, y_pred, 'r', label="Best Fit: All Years")

    # Create second line of best fit
    recent_df = df[df["Year"] >= 2000]
    result2 = linregress(recent_df["Year"], recent_df["CSIRO Adjusted Sea Level"])
    x_extended2 = range(2000, 2051)
    y_pred2 = result2.slope * x_extended2 + result2.intercept

    plt.plot(x_extended2, y_pred2, 'green', label="Best Fit: 2000 onwards")
    

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()