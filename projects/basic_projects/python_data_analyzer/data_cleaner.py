"""
Module for cleaning and preprocessing CSV data.
"""

import pandas as pd
import numpy as np
import os
from datetime import datetime

def load_csv(file_path):
    """
    Load data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pandas.DataFrame: Loaded data or None if loading fails
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            print(f"Error: File {file_path} not found.")
            return None
        
        # Check file extension
        if not file_path.lower().endswith('.csv'):
            print(f"Error: File {file_path} is not a CSV file.")
            return None
        
        # Load the data
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {len(df)} rows from {file_path}")
        return df
    
    except pd.errors.EmptyDataError:
        print(f"Error: {file_path} is empty.")
        return None
    
    except pd.errors.ParserError:
        print(f"Error: Unable to parse {file_path}. Check if it's a valid CSV.")
        return None
    
    except Exception as e:
        print(f"Error loading {file_path}: {str(e)}")
        return None

def clean_data(df):
    """
    Clean and preprocess the data.
    
    Args:
        df (pandas.DataFrame): DataFrame to clean
        
    Returns:
        pandas.DataFrame: Cleaned DataFrame
    """
    if df is None or df.empty:
        print("No data to clean.")
        return None
    
    # Make a copy to avoid modifying the original
    cleaned_df = df.copy()
    numeric_cols = cleaned_df.select_dtypes(include=[np.number]).columns
    
    # 1. Remove duplicate rows
    original_rows = len(cleaned_df)
    cleaned_df = cleaned_df.drop_duplicates()
    if len(cleaned_df) < original_rows:
        print(f"Removed {original_rows - len(cleaned_df)} duplicate rows.")
    
    # 2. Handle missing values
    missing_values = cleaned_df.isnull().sum().sum()
    if missing_values > 0:
        print(f"Found {missing_values} missing values.")
        
        # For numeric columns, fill with mean
        numeric_cols = cleaned_df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            if cleaned_df[col].isnull().any():
                mean_val = cleaned_df[col].mean()
                cleaned_df[col].fillna(mean_val, inplace=True)
                print(f"Filled missing values in {col} with mean ({mean_val:.2f}).")
        
        # For categorical columns, fill with mode
        categorical_cols = cleaned_df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            if cleaned_df[col].isnull().any():
                mode_val = cleaned_df[col].mode()[0]
                cleaned_df[col].fillna(mode_val, inplace=True)
                print(f"Filled missing values in {col} with mode ({mode_val}).")
    
    # 3. Convert date columns to datetime
    date_columns = [col for col in cleaned_df.columns if 'date' in col.lower()]
    for col in date_columns:
        try:
            cleaned_df[col] = pd.to_datetime(cleaned_df[col])
            print(f"Converted {col} to datetime format.")
        except:
            print(f"Warning: Failed to convert {col} to datetime format.")
    
    # 4. Handle outliers in numeric columns using IQR method
    for col in numeric_cols:
        Q1 = cleaned_df[col].quantile(0.25)
        Q3 = cleaned_df[col].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = ((cleaned_df[col] < lower_bound) | (cleaned_df[col] > upper_bound)).sum()
        if outliers > 0:
            print(f"Found {outliers} outliers in {col}.")
            
            # Cap the outliers instead of removing them
            cleaned_df[col] = cleaned_df[col].clip(lower=lower_bound, upper=upper_bound)
            print(f"Capped outliers in {col} to range [{lower_bound:.2f}, {upper_bound:.2f}].")
    
    print("Data cleaning completed successfully.")
    return cleaned_df

def save_cleaned_data(df, output_path=None):
    """
    Save the cleaned data to a new CSV file.
    
    Args:
        df (pandas.DataFrame): DataFrame to save
        output_path (str): Path to save the file, or None to generate automatically
        
    Returns:
        str: Path to the saved file, or None if saving fails
    """
    if df is None or df.empty:
        print("No data to save.")
        return None
    
    try:
        # Generate output path if not provided
        if output_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_dir = "cleaned_data"
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f"cleaned_data_{timestamp}.csv")
        
        # Save the data
        df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")
        return output_path
    
    except Exception as e:
        print(f"Error saving cleaned data: {str(e)}")
        return None


if __name__ == "__main__":
    # Example usage
    file_path = "example_data/sample_sales.csv"
    df = load_csv(file_path)
    
    if df is not None:
        cleaned_df = clean_data(df)
        if cleaned_df is not None:
            save_cleaned_data(cleaned_df)