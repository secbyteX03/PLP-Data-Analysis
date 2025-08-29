#!/usr/bin/env python3
"""
Helper script to generate the Iris dataset as a CSV file with dates.
This is used to meet the assignment requirement of loading data from a CSV file.

Author: Magret Faith
"""

from sklearn import datasets
import pandas as pd

def create_iris_csv():
    """Save the Iris dataset as a CSV file."""
    # Load the Iris dataset
    iris = datasets.load_iris()
    
    # Create a DataFrame
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    # Add a date column for time series visualization
    dates = pd.date_range(start='2023-01-01', periods=len(df), freq='D')
    df['date'] = dates
    
    # Save to CSV
    df.to_csv('iris_data.csv', index=False)
    print("Iris dataset saved as 'iris_data.csv'")

if __name__ == "__main__":
    create_iris_csv()
