"""
Python Data Analyzer - Main Module

This module provides a command-line interface for analyzing CSV data files.
It combines functionality from the data_cleaner, statistics_helper, and visualizer modules.
"""

import os
import sys
import argparse
from datetime import datetime

# Import our modules
from data_cleaner import load_csv, clean_data, save_cleaned_data
from statistics_helper import (get_basic_stats, print_statistics, group_and_aggregate,
                               time_series_analysis, correlation_analysis, save_analysis_results)
from visualizer import (create_bar_chart, create_line_chart, create_pie_chart,
                        create_histogram, create_scatter_plot, create_heatmap)

def print_dataset_info(df):
    """
    Print basic information about the dataset.
    
    Args:
        df: pandas DataFrame to analyze
    """
    if df is None or df.empty:
        print("No data to analyze.")
        return
    
    print("\n" + "=" * 50)
    print("DATASET OVERVIEW")
    print("=" * 50)
    print(f"Number of rows: {len(df)}")
    print(f"Number of columns: {len(df.columns)}")
    print("\nColumns:")
    
    for i, col in enumerate(df.columns, 1):
        dtype = df[col].dtype
        n_missing = df[col].isnull().sum()
        n_unique = df[col].nunique()
        
        print(f"{i}. {col} (Type: {dtype})")
        print(f"   - Missing values: {n_missing} ({n_missing/len(df)*100:.1f}%)")
        print(f"   - Unique values: {n_unique}")
        
        # Print sample values for categorical data with few unique values
        if n_unique <= 10 and n_unique < len(df) / 2:
            print(f"   - Values: {', '.join(str(x) for x in df[col].unique()[:10])}")
        
        # Print range for numeric data
        if str(dtype).startswith(('int', 'float')):
            print(f"   - Range: {df[col].min()} to {df[col].max()}")
    
    print("=" * 50)

def run_analysis(file_path, options):
    """
    Run the data analysis process.
    
    Args:
        file_path: Path to the CSV file
        options: Dictionary of analysis options
    """
    # Step 1: Load the data
    print(f"\nLoading data from {file_path}...")
    df = load_csv(file_path)
    
    if df is None:
        print("Failed to load data. Exiting.")
        return
    
    # Print dataset info
    print_dataset_info(df)
    
    # Step 2: Clean the data if requested
    if options['clean']:
        print("\nCleaning data...")
        df = clean_data(df)
        
        if options['save_cleaned']:
            cleaned_path = save_cleaned_data(df)
            if cleaned_path:
                print(f"Cleaned data saved to {cleaned_path}")
    
    # Step 3: Statistical analysis
    if options['stats']:
        print("\nPerforming statistical analysis...")
        
        # Get numeric columns for stats
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        
        if not numeric_cols:
            print("No numeric columns found for statistical analysis.")
        else:
            # If specific columns are provided, filter the numeric columns
            if options['columns']:
                columns = [c for c in options['columns'] if c in numeric_cols]
                if not columns:
                    print("None of the specified columns are numeric.")
                    columns = numeric_cols
            else:
                columns = numeric_cols
            
            # Basic statistics for each column
            for column in columns:
                stats = get_basic_stats(df, column)
                if stats:
                    print_statistics(stats, column)
            
            # Correlation analysis
            if len(columns) >= 2:
                print("\nCalculating correlation matrix...")
                corr_matrix = correlation_analysis(df, columns)
                if corr_matrix is not None and options['save_results']:
                    save_analysis_results(corr_matrix, "correlation")
    
    # Step 4: Group analysis if requested
    if options['group_by'] and options['agg_column']:
        print(f"\nGrouping data by '{options['group_by']}' and aggregating '{options['agg_column']}'...")
        grouped_data = group_and_aggregate(df, options['group_by'], options['agg_column'], options['agg_func'])
        
        if grouped_data is not None:
            print("\nGrouped Data:")
            print(grouped_data)
            
            if options['save_results']:
                save_analysis_results(grouped_data, f"grouped_by_{options['group_by']}")
            
            # Create visualization for grouped data
            if options['visualize']:
                chart_path = create_bar_chart(
                    grouped_data, 
                    options['group_by'], 
                    f"{options['agg_func']}_{options['agg_column']}",
                    title=f"{options['agg_func'].title()} of {options['agg_column']} by {options['group_by']}"
                )
    
    # Step 5: Time series analysis if requested
    if options['time_column'] and options['value_column']:
        print(f"\nPerforming time series analysis on '{options['value_column']}' over '{options['time_column']}'...")
        ts_data = time_series_analysis(df, options['time_column'], options['value_column'], options['time_freq'])
        
        if ts_data is not None:
            print("\nTime Series Analysis:")
            print(ts_data)
            
            if options['save_results']:
                save_analysis_results(ts_data, f"time_series_{options['value_column']}")
            
            # Create visualization for time series
            if options['visualize']:
                chart_path = create_line_chart(
                    ts_data, 
                    options['time_column'], 
                    f"{options['value_column']}_sum",
                    title=f"{options['value_column']} over Time"
                )
    
    # Step 6: Visualizations if requested
    if options['visualize']:
        print("\nCreating visualizations...")
        
        # Directory for visualizations
        vis_dir = "visualizations"
        os.makedirs(vis_dir, exist_ok=True)
        
        # Basic numeric visualizations
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        if numeric_cols:
            # Histogram of first numeric column
            create_histogram(
                df, 
                numeric_cols[0], 
                bins=10,
                title=f"Distribution of {numeric_cols[0]}",
                save_path=os.path.join(vis_dir, f"histogram_{numeric_cols[0]}.png")
            )
            
            # If we have multiple numeric columns
            if len(numeric_cols) >= 2:
                # Scatter plot of first two numeric columns
                create_scatter_plot(
                    df, 
                    numeric_cols[0], 
                    numeric_cols[1],
                    title=f"{numeric_cols[1]} vs {numeric_cols[0]}",
                    save_path=os.path.join(vis_dir, f"scatter_{numeric_cols[0]}_{numeric_cols[1]}.png")
                )
                
                # Correlation heatmap
                create_heatmap(
                    df, 
                    numeric_cols,
                    title="Correlation Matrix",
                    save_path=os.path.join(vis_dir, "correlation_heatmap.png")
                )
        
        # Categorical visualizations
        categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
        if categorical_cols and numeric_cols:
            # Bar chart of first categorical column vs first numeric column
            create_bar_chart(
                df, 
                categorical_cols[0], 
                numeric_cols[0],
                title=f"{numeric_cols[0]} by {categorical_cols[0]}",
                save_path=os.path.join(vis_dir, f"bar_{categorical_cols[0]}_{numeric_cols[0]}.png")
            )
            
            # Pie chart
            create_pie_chart(
                df, 
                categorical_cols[0], 
                numeric_cols[0],
                title=f"{numeric_cols[0]} Distribution by {categorical_cols[0]}",
                save_path=os.path.join(vis_dir, f"pie_{categorical_cols[0]}_{numeric_cols[0]}.png")
            )
    
    print("\nAnalysis completed.")

def main():
    """Main function to run the data analyzer from command line."""
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Analyze CSV data files")
    
    # Required arguments
    parser.add_argument("file", help="Path to the CSV file to analyze")
    
    # Optional arguments
    parser.add_argument("--clean", action="store_true", help="Clean and preprocess the data")
    parser.add_argument("--save-cleaned", action="store_true", help="Save the cleaned data to a new file")
    parser.add_argument("--stats", action="store_true", help="Perform statistical analysis")
    parser.add_argument("--columns", nargs="+", help="Specific columns to analyze")
    parser.add_argument("--group-by", help="Column to group by")
    parser.add_argument("--agg-column", help="Column to aggregate")
    parser.add_argument("--agg-func", default="mean", choices=["mean", "sum", "count", "min", "max"],
                       help="Aggregation function")
    parser.add_argument("--time-column", help="Column containing date/time data")
    parser.add_argument("--value-column", help="Column to analyze over time")
    parser.add_argument("--time-freq", default="M", choices=["D", "W", "M", "Q", "Y"],
                       help="Time frequency (D=daily, W=weekly, M=monthly, Q=quarterly, Y=yearly)")
    parser.add_argument("--visualize", action="store_true", help="Create visualizations")
    parser.add_argument("--save-results", action="store_true", help="Save analysis results to files")
    
    args = parser.parse_args()
    
    # Create options dictionary
    options = {
        'clean': args.clean,
        'save_cleaned': args.save_cleaned,
        'stats': args.stats,
        'columns': args.columns,
        'group_by': args.group_by,
        'agg_column': args.agg_column,
        'agg_func': args.agg_func,
        'time_column': args.time_column,
        'value_column': args.value_column,
        'time_freq': args.time_freq,
        'visualize': args.visualize,
        'save_results': args.save_results
    }
    
    # If no specific analysis is requested, perform basic analysis
    if not (args.clean or args.stats or args.group_by or args.time_column or args.visualize):
        print("No specific analysis requested. Performing basic analysis...")
        options['clean'] = True
        options['stats'] = True
        options['visualize'] = True
    
    # Run the analysis
    run_analysis(args.file, options)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAnalysis interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)