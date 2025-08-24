"""
Module for performing statistical analysis on data.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os

def get_basic_stats(df, column):
    """
    Calculate basic statistics for a numeric column.
    
    Args:
        df (pandas.DataFrame): Input DataFrame
        column (str): Name of the column to analyze
        
    Returns:
        dict: Dictionary containing statistics
    """
    if df is None or df.empty:
        print("No data to analyze.")
        return None
    
    if column not in df.columns:
        print(f"Column '{column}' not found in the data.")
        return None
    
    # Check if column is numeric
    if not pd.api.types.is_numeric_dtype(df[column]):
        print(f"Column '{column}' is not numeric. Converting to numeric if possible.")
        try:
            df[column] = pd.to_numeric(df[column])
        except:
            print(f"Failed to convert '{column}' to numeric type.")
            return None
    
    # Calculate statistics
    stats = {
        'count': len(df[column]),
        'missing': df[column].isnull().sum(),
        'min': df[column].min(),
        'max': df[column].max(),
        'range': df[column].max() - df[column].min(),
        'mean': df[column].mean(),
        'median': df[column].median(),
        'mode': df[column].mode()[0],
        'std': df[column].std(),
        'variance': df[column].var(),
        'skewness': df[column].skew(),
        'kurtosis': df[column].kurt(),
        'q1': df[column].quantile(0.25),
        'q3': df[column].quantile(0.75),
        'iqr': df[column].quantile(0.75) - df[column].quantile(0.25)
    }
    
    return stats

def print_statistics(stats, column_name):
    """
    Print statistics in a readable format.
    
    Args:
        stats (dict): Dictionary of statistics
        column_name (str): Name of the column analyzed
    """
    if stats is None:
        return
    
    print("\n" + "=" * 50)
    print(f"Statistics for column: {column_name}")
    print("=" * 50)
    print(f"Count: {stats['count']}")
    print(f"Missing Values: {stats['missing']}")
    print(f"Minimum: {stats['min']:.2f}")
    print(f"Maximum: {stats['max']:.2f}")
    print(f"Range: {stats['range']:.2f}")
    print(f"Mean: {stats['mean']:.2f}")
    print(f"Median: {stats['median']:.2f}")
    print(f"Mode: {stats['mode']:.2f}")
    print(f"Standard Deviation: {stats['std']:.2f}")
    print(f"Variance: {stats['variance']:.2f}")
    print(f"Skewness: {stats['skewness']:.2f}")
    print(f"Kurtosis: {stats['kurtosis']:.2f}")
    print(f"1st Quartile (Q1): {stats['q1']:.2f}")
    print(f"3rd Quartile (Q3): {stats['q3']:.2f}")
    print(f"Interquartile Range (IQR): {stats['iqr']:.2f}")
    print("=" * 50)

def group_and_aggregate(df, group_by, agg_column, agg_func='mean'):
    """
    Group data by one column and aggregate another column.
    
    Args:
        df (pandas.DataFrame): Input DataFrame
        group_by (str): Column to group by
        agg_column (str): Column to aggregate
        agg_func (str): Aggregation function ('mean', 'sum', 'count', 'min', or 'max')
        
    Returns:
        pandas.DataFrame: Grouped and aggregated data
    """
    if df is None or df.empty:
        print("No data to group and aggregate.")
        return None
    
    if group_by not in df.columns:
        print(f"Column '{group_by}' not found in the data.")
        return None
    
    if agg_column not in df.columns:
        print(f"Column '{agg_column}' not found in the data.")
        return None
    
    # Check if aggregation column is numeric for mean, sum, min, max
    if agg_func in ['mean', 'sum', 'min', 'max'] and not pd.api.types.is_numeric_dtype(df[agg_column]):
        print(f"Warning: Column '{agg_column}' is not numeric. Trying to convert...")
        try:
            df[agg_column] = pd.to_numeric(df[agg_column])
        except:
            print(f"Failed to convert '{agg_column}' to numeric type. Using 'count' instead.")
            agg_func = 'count'
    
    # Perform grouping and aggregation
    valid_funcs = {'mean', 'sum', 'count', 'min', 'max'}
    if agg_func not in valid_funcs:
        print(f"Invalid aggregation function '{agg_func}'. Using 'mean' instead.")
        agg_func = 'mean'
    
    grouped = df.groupby(group_by)[agg_column].agg(agg_func).reset_index()
    grouped.columns = [group_by, f"{agg_func}_{agg_column}"]
    
    print(f"Data grouped by '{group_by}' with '{agg_func}' aggregation on '{agg_column}'.")
    return grouped

def time_series_analysis(df, date_column, value_column, freq='M'):
    """
    Perform time series analysis by resampling data at specified frequency.
    
    Args:
        df (pandas.DataFrame): Input DataFrame
        date_column (str): Name of the date column
        value_column (str): Name of the value column to analyze
        freq (str): Frequency for resampling ('D' for daily, 'W' for weekly, 'M' for monthly)
        
    Returns:
        pandas.DataFrame: Resampled time series data
    """
    if df is None or df.empty:
        print("No data for time series analysis.")
        return None
    
    if date_column not in df.columns:
        print(f"Date column '{date_column}' not found in the data.")
        return None
    
    if value_column not in df.columns:
        print(f"Value column '{value_column}' not found in the data.")
        return None
    
    # Convert date column to datetime if it's not already
    if not pd.api.types.is_datetime64_dtype(df[date_column]):
        try:
            df[date_column] = pd.to_datetime(df[date_column])
        except:
            print(f"Failed to convert '{date_column}' to datetime type.")
            return None
    
    # Convert value column to numeric if it's not already
    if not pd.api.types.is_numeric_dtype(df[value_column]):
        try:
            df[value_column] = pd.to_numeric(df[value_column])
        except:
            print(f"Failed to convert '{value_column}' to numeric type.")
            return None
    
    # Set date as index
    df_ts = df.set_index(date_column)
    
    # Define frequency mapping
    freq_map = {
        'D': 'Daily',
        'W': 'Weekly',
        'M': 'Monthly',
        'Q': 'Quarterly',
        'Y': 'Yearly'
    }
    
    freq_name = freq_map.get(freq, freq)
    
    # Resample data
    resampled = df_ts[value_column].resample(freq).agg(['sum', 'mean', 'count']).reset_index()
    resampled.columns = [date_column, f"{value_column}_sum", f"{value_column}_mean", f"{value_column}_count"]
    
    print(f"Performed {freq_name} time series analysis on '{value_column}'.")
    return resampled

def correlation_analysis(df, columns=None):
    """
    Calculate correlation matrix for numeric columns.
    
    Args:
        df (pandas.DataFrame): Input DataFrame
        columns (list): List of columns to include, or None for all numeric columns
        
    Returns:
        pandas.DataFrame: Correlation matrix
    """
    if df is None or df.empty:
        print("No data for correlation analysis.")
        return None
    
    # Get numeric columns if columns not specified
    if columns is None:
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    else:
        # Filter valid numeric columns from the provided list
        numeric_cols = []
        for col in columns:
            if col not in df.columns:
                print(f"Column '{col}' not found in the data.")
                continue
            
            if not pd.api.types.is_numeric_dtype(df[col]):
                print(f"Column '{col}' is not numeric and will be excluded.")
                continue
            
            numeric_cols.append(col)
    
    if not numeric_cols:
        print("No numeric columns found for correlation analysis.")
        return None
    
    # Calculate correlation matrix
    corr_matrix = df[numeric_cols].corr()
    
    print(f"Calculated correlation matrix for {len(numeric_cols)} numeric columns.")
    return corr_matrix

def save_analysis_results(result_df, analysis_type, output_dir="analysis_results"):
    """
    Save analysis results to a CSV file.
    
    Args:
        result_df (pandas.DataFrame): DataFrame with results
        analysis_type (str): Type of analysis performed
        output_dir (str): Directory to save results
        
    Returns:
        str: Path to the saved file, or None if saving fails
    """
    if result_df is None or result_df.empty:
        print("No results to save.")
        return None
    
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{analysis_type}_{timestamp}.csv"
        output_path = os.path.join(output_dir, filename)
        
        # Save results
        result_df.to_csv(output_path, index=True)
        print(f"Analysis results saved to {output_path}")
        return output_path
    
    except Exception as e:
        print(f"Error saving analysis results: {str(e)}")
        return None


if __name__ == "__main__":
    # Example usage
    from data_cleaner import load_csv
    
    file_path = "example_data/sample_sales.csv"
    df = load_csv(file_path)
    
    if df is not None:
        # Basic statistics
        revenue_stats = get_basic_stats(df, 'Revenue')
        print_statistics(revenue_stats, 'Revenue')
        
        # Group and aggregate
        region_sales = group_and_aggregate(df, 'Region', 'Revenue', 'sum')
        print(region_sales)
        
        # Time series analysis
        time_sales = time_series_analysis(df, 'Date', 'Revenue', 'M')
        print(time_sales)
        
        # Correlation analysis
        corr_matrix = correlation_analysis(df, ['Units', 'Revenue'])
        print(corr_matrix)