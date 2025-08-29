#!/usr/bin/env python3
"""
PLP Data Analysis Assignment
Analyzing the Iris dataset using pandas and matplotlib.

Author: Magret Faith
This script performs data analysis and visualization on the Iris dataset loaded from a CSV file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
from datetime import datetime

def load_data(csv_file):
    """
    Load and return the dataset from a CSV file.
    
    Args:
        csv_file (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Loaded dataset
    """
    try:
        df = pd.read_csv(csv_file)
        print("\n✅ Successfully loaded dataset from:", csv_file)
        return df
    except FileNotFoundError:
        print(f"\n❌ Error: The file {csv_file} was not found.")
        print("Please make sure the file exists and try again.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ An error occurred while loading the file: {str(e)}")
        sys.exit(1)

def explore_data(df):
    """
    Perform initial data exploration.
    
    Args:
        df (pd.DataFrame): Input dataset
    """
    print("\n=== Dataset Information ===")
    print(f"Dataset shape: {df.shape}")
    
    print("\n=== First 5 rows ===")
    print(df.head())
    
    print("\n=== Data Types ===")
    print(df.dtypes)
    
    print("\n=== Missing Values ===")
    print(df.isnull().sum())
    
    # Handle missing values if any
    if df.isnull().sum().sum() > 0:
        print("\nHandling missing values...")
        # Fill numeric columns with mean, categorical with mode
        for col in df.columns:
            if df[col].dtype in ['int64', 'float64']:
                df[col].fillna(df[col].mean(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)
        print("Missing values have been handled.")

def analyze_data(df):
    """
    Perform basic data analysis.
    
    Args:
        df (pd.DataFrame): Input dataset
    """
    print("\n=== Basic Statistics ===")
    print(df.describe())
    
    # Group by species and calculate mean for numerical columns
    if 'species' in df.columns:
        print("\n=== Mean Values by Species ===")
        print(df.groupby('species').mean(numeric_only=True))
        
        # Find interesting patterns
        print("\n=== Interesting Findings ===")
        print("1. Setosa has the smallest petal dimensions")
        print("2. Virginica has the largest petal dimensions")
        print("3. Sepal width is most consistent across all species")

def create_visualizations(df, output_dir='output'):
    """
    Create and save required visualizations.
    
    Args:
        df (pd.DataFrame): Input dataset
        output_dir (str): Directory to save visualizations
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Line Chart - Trends over time (using the date column)
    if 'date' in df.columns and 'sepal length (cm)' in df.columns:
        plt.figure(figsize=(12, 6))
        df.sort_values('date', inplace=True)
        for species in df['species'].unique():
            subset = df[df['species'] == species]
            plt.plot(subset['date'], subset['sepal length (cm)'], 
                    label=species, marker='o')
        plt.title('Sepal Length Over Time by Species')
        plt.xlabel('Date')
        plt.ylabel('Sepal Length (cm)')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'{output_dir}/sepal_length_trend.png')
        plt.close()
        print("\n✅ Created line chart: sepal_length_trend.png")
    
    # 2. Bar Chart - Average petal length by species
    if 'species' in df.columns and 'petal length (cm)' in df.columns:
        plt.figure(figsize=(10, 6))
        avg_petal = df.groupby('species')['petal length (cm)'].mean()
        avg_petal.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
        plt.title('Average Petal Length by Species')
        plt.xlabel('Species')
        plt.ylabel('Average Petal Length (cm)')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig(f'{output_dir}/avg_petal_length.png')
        plt.close()
        print("✅ Created bar chart: avg_petal_length.png")
    
    # 3. Histogram - Distribution of sepal width
    if 'sepal width (cm)' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x='sepal width (cm)', bins=15, kde=True, 
                    hue='species' if 'species' in df.columns else None)
        plt.title('Distribution of Sepal Width')
        plt.xlabel('Sepal Width (cm)')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/sepal_width_distribution.png')
        plt.close()
        print("✅ Created histogram: sepal_width_distribution.png")
    
    # 4. Scatter Plot - Sepal length vs Petal length
    if 'sepal length (cm)' in df.columns and 'petal length (cm)' in df.columns:
        plt.figure(figsize=(10, 6))
        if 'species' in df.columns:
            sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', 
                          hue='species', style='species', s=80)
        else:
            sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)')
        plt.title('Sepal Length vs Petal Length')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/sepal_vs_petal_length.png')
        plt.close()
        print("✅ Created scatter plot: sepal_vs_petal_length.png")

def main():
    """Main function to run the analysis."""
    # Configure console for UTF-8 output
    import sys
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    print("\n" + "="*50)
    print("📊 PLP Assignment: Data Analysis with Pandas and Matplotlib")
    print("="*50)
    
    # Define the data file
    csv_file = 'iris_data.csv'
    
    # Load the data
    print("\n🔍 Loading dataset...")
    df = load_data(csv_file)
    
    # Explore the data
    print("\n🔍 Exploring dataset...")
    explore_data(df)
    
    # Perform analysis
    print("\n📈 Analyzing data...")
    analyze_data(df)
    
    # Create visualizations
    print("\n🎨 Creating visualizations...")
    create_visualizations(df)
    
    print("\n" + "="*50)
    print("✅ Analysis complete! Check the 'output' directory for visualizations.")
    print("="*50)

if __name__ == "__main__":
    main()
