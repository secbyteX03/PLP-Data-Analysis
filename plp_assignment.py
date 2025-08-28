#!/usr/bin/env python3
"""
PLP Assignment: Data Analysis with Iris Dataset
This script performs data analysis and visualization on the Iris dataset.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
import os

def load_data():
    """Load and return the Iris dataset as a pandas DataFrame."""
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    return df

def explore_data(df):
    """Display basic information about the dataset."""
    print("\n=== Dataset Information ===")
    print(f"Dataset shape: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())
    
    print("\n=== Basic Statistics ===")
    print(df.describe())
    
    print("\n=== Class Distribution ===")
    print(df['species'].value_counts())

def create_visualizations(df):
    """Create and save visualizations of the dataset."""
    # Create output directory if it doesn't exist
    os.makedirs('output', exist_ok=True)
    
    # Visualization 1: Pairplot
    print("\nCreating pairplot...")
    pair_plot = sns.pairplot(df, hue='species')
    pair_plot.fig.suptitle('Iris Dataset - Pairplot', y=1.02)
    plt.savefig('output/iris_pairplot.png', bbox_inches='tight')
    plt.close()
    
    # Visualization 2: Boxplot
    print("Creating boxplot...")
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df.drop('species', axis=1))
    plt.title('Feature Distribution')
    plt.xticks(rotation=45)
    plt.savefig('output/iris_boxplot.png', bbox_inches='tight')
    plt.close()
    
    # Visualization 3: Correlation Heatmap
    print("Creating correlation heatmap...")
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.savefig('output/iris_heatmap.png', bbox_inches='tight')
    plt.close()
    
    # Visualization 4: Violin Plot
    print("Creating violin plot...")
    plt.figure(figsize=(12, 6))
    sns.violinplot(x='species', y='petal length (cm)', data=df)
    plt.title('Petal Length Distribution by Species')
    plt.savefig('output/iris_violinplot.png', bbox_inches='tight')
    plt.close()

def main():
    """Main function to run the analysis."""
    print("Starting Iris Dataset Analysis...")
    
    # Load the data
    df = load_data()
    
    # Perform exploratory data analysis
    explore_data(df)
    
    # Create visualizations
    create_visualizations(df)
    
    print("\nAnalysis complete! Check the 'output' directory for visualizations.")

if __name__ == "__main__":
    main()
