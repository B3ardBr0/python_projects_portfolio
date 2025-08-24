"""
Module for visualizing data using matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from datetime import datetime

def create_bar_chart(df, x_column, y_column, title=None, color='blue', save_path=None):
    """
    Create a bar chart visualization.
    
    Args:
        df (pandas.DataFrame): Input DataFrame
        x_column (str): Column for x-axis
        y_column (str): Column for y-axis (must be numeric)
        title (str): Chart title or None to auto-generate
        color (str): Color for the bars
        save_path (str): Path to save the chart or None to display
        
    Returns:
        str: Path to the saved chart or None if not saved
    """
    if df is None or df.empty:
        print("No data to visualize.")
        return None
    
    if x_column not in df.columns:
        print(f"Column '{x_column}' not found in the data.")
        return None
    
    if y_column not in df.columns:
        print(f"Column '{y_column}' not found in the data.")
        return None
    
    # Make sure y_column is numeric
    if not pd.api.types.is_numeric_dtype(df[y_column]):
        print(f"Column '{y_column}' is not numeric. Attempting to convert...")
        try:
            df[y_column] = pd.to_numeric(df[y_column])
        except:
            print(f"Failed to convert '{y_column}' to numeric type.")
            return None
    
    # Create figure
    plt.figure(figsize=(10, 6))
    
    # Create bar chart
    bars = plt.bar(df[x_column], df[y_column], color=color, alpha=0.7)
    
    # Add title and labels
    if title is None:
        title = f"{y_column} by {x_column}"
    plt.title(title, fontsize=14)
    plt.xlabel(x_column, fontsize=12)
    plt.ylabel(y_column, fontsize=12)
    
    # Add data labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{height:.1f}', ha='center', va='bottom')
    
    # Rotate x labels if there are many categories
    if len(df[x_column].unique()) > 5:
        plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    
    # Save or display the chart
    if save_path is not None:
        try:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            print(f"Bar chart saved to {save_path}")
            return save_path
        except Exception as e:
            print(f"Error saving chart: {str(e)}")
            plt.close()
            return None
    else:
        plt.show()
        plt.close()
        return None

def create_line_chart(df, x_column, y_column, title=None, color='blue', save_path=None):
    """
    Create a line chart visualization.
    
    Args:
        df (pandas.DataFrame): Input DataFrame
        x_column (str): Column for x-axis (preferably date/time)
        y_column (str): Column for y-axis (must be numeric)
        title (str): Chart title or None to auto-generate
        color (str): Color for the line
        save_path (str): Path to save the chart or None to display
        
    Returns:
        str: Path to the saved chart or None if not saved
    """
    if df is None or df.empty:
        print("No data to visualize.")
        return None
    
    if x_column not in df.columns:
        print(f"Column '{x_column}' not found in the data.")
        return None
    
    if y_column not in df.columns:
        print(f"Column '{y_column}' not found in the data.")
        return None
    
    # Make sure y_column is numeric
    if not pd.api.types.is_numeric_dtype(df[y_column]):
        print(f"Column '{y_column}' is not numeric. Attempting to convert...")
        try:
            df[y_column] = pd.to_numeric(df[y_column])
        except:
            print(f"Failed to convert '{y_column}' to numeric type.")
            return None
    
    # Convert x_column to datetime if it contains date-like strings
    x_is_datetime = False
    if pd.api.types.is_object_dtype(df[x_column]):
        try:
            df[x_column] = pd.to_datetime(df[x_column])
            x_is_datetime = True
        except:
            # Not a datetime, continue with original data
            pass
    elif pd.api.types.is_datetime64_dtype(df[x_column]):
        x_is_datetime = True
    
    # Sort data by x_column
    df_sorted = df.sort_values(by=x_column)
    
    # Create figure
    plt.figure(figsize=(12, 6))
    
    # Create line chart
    plt.plot(df_sorted[x_column], df_sorted[y_column], color=color, marker='o', 
             linestyle='-', linewidth=2, markersize=6, alpha=0.7)
    
    # Add title and labels
    if title is None:
        title = f"{y_column} over {x_column}"
    plt.title(title, fontsize=14)
    plt.xlabel(x_column, fontsize=12)
    plt.ylabel(y_column, fontsize=12)
    
    # Format x-axis if it's datetime
    if x_is_datetime:
        plt.gcf().autofmt_xdate()
    
    # Add grid
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    
    # Save or display the chart
    if save_path is not None:
        try:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            print(f"Line chart saved to {save_path}")
            return save_path
        except Exception as e:
            print(f"Error saving chart: {str(e)}")
            plt.close()
            return None
    else:
        plt.show()
        plt.close()
        return None

def create_pie_chart(df, category_column, value_column=None, title=None, save_path=None):
    """
    Create a pie chart visualization.
    
    Args:
        df (pandas.DataFrame): Input DataFrame
        category_column (str): Column for categories
        value_column (str): Column for values or None to count occurrences
        title (str): Chart title or None to auto-generate
        save_path (str): Path to save the chart or None to display
        
    Returns:
        str: Path to the saved chart or None if not saved
    """
    if df is None or df.empty:
        print("No data to visualize.")
        return None
    
    if category_column not in df.columns:
        print(f"Column '{category_column}' not found in the data.")
        return None
    
    # Prepare data for pie chart
    if value_column is None:
        # Count occurrences of each category
        data = df[category_column].value_counts()
        value_label = 'Count'
    else:
        if value_column not in df.columns:
            print(f"Column '{value_column}' not found in the data.")
            return None
        
        # Make sure value_column is numeric
        if not pd.api.types.is_numeric_dtype(df[value_column]):
            print(f"Column '{value_column}' is not numeric. Attempting to convert...")
            try:
                df[value_column] = pd.to_numeric(df[value_column])
            except:
                print(f"Failed to convert '{value_column}' to numeric type.")
                return None
        
        # Group by category and sum values
        data = df.groupby(category_column)[value_column].sum()
        value_label = value_column
    
    # Create figure
    plt.figure(figsize=(10, 8))
    
    # Create pie chart
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90, 
            shadow=True, explode=[0.05] * len(data), 
            wedgeprops={'edgecolor': 'white', 'linewidth': 1})
    
    # Add title
    if title is None:
        title = f"{category_column} Distribution"
    plt.title(title, fontsize=14)
    
    # Add legend
    plt.legend(data.index, loc="best", bbox_to_anchor=(1, 0.5))
    
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.tight_layout()
    
    # Save or display the chart
    if save_path is not None:
        try:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            print(f"Pie chart saved to {save_path}")
            return save_path
        except Exception as e:
            print(f"Error saving chart: {str(e)}")
            plt.close()
            return None
    else:
        plt.show()
        plt.close()
        return None

def create_histogram(df, column, bins=10, title=None, color='skyblue', save_path=None):
    """
    Create a histogram visualization.
    
    Args:
        df (pandas.DataFrame): Input DataFrame
        column (str): Column to analyze (must be numeric)
        bins (int): Number of bins for the histogram
        title (str): Chart title or None to auto-generate
        color (str): Color for the bars
        save_path (str): Path to save the chart or None to display
        
    Returns:
        str: Path to the saved chart or None if not saved
    """
    if df is None or df.empty:
        print("No data to visualize.")
        return None
    
    if column not in df.columns:
        print(f"Column '{column}' not found in the data.")
        return None
    
    # Make sure column is numeric
    if not pd.api.types.is_numeric_dtype(df[column]):
        print(f"Column '{column}' is not numeric. Attempting to convert...")
        try:
            df[column] = pd.to_numeric(df[column])
        except:
            print(f"Failed to convert '{column}' to numeric type.")
            return None
    
    # Create figure
    plt.figure(figsize=(10, 6))
    
    # Create histogram
    n, bins, patches = plt.hist(df[column], bins=bins, color=color, alpha=0.7, edgecolor='black')
    
    # Add a line for the average
    plt.axvline(df[column].mean(), color='red', linestyle='dashed', linewidth=2, label=f'Mean: {df[column].mean():.2f}')
    plt.axvline(df[column].median(), color='green', linestyle='dashed', linewidth=2, label=f'Median: {df[column].median():.2f}')
    
    # Add title and labels
    if title is None:
        title = f"Distribution of {column}"
    plt.title(title, fontsize=14)
    plt.xlabel(column, fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    
    # Add grid and legend
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    
    # Save or display the chart
    if save_path is not None:
        try:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            print(f"Histogram saved to {save_path}")
            return save_path
        except Exception as e:
            print(f"Error saving chart: {str(e)}")
            plt.close()
            return None
    else:
        plt.show()
        plt.close()
        return None

def create_scatter_plot(df, x_column, y_column, title=None, color='blue', save_path=None):
    """
    Create a scatter plot visualization.
    
    Args:
        df (pandas.DataFrame): Input DataFrame
        x_column (str): Column for x-axis (must be numeric)
        y_column (str): Column for y-axis (must be numeric)
        title (str): Chart title or None to auto-generate
        color (str): Color for the points
        save_path (str): Path to save the chart or None to display
        
    Returns:
        str: Path to the saved chart or None if not saved
    """
    if df is None or df.empty:
        print("No data to visualize.")
        return None
    
    if x_column not in df.columns:
        print(f"Column '{x_column}' not found in the data.")
        return None
    
    if y_column not in df.columns:
        print(f"Column '{y_column}' not found in the data.")
        return None
    
    # Make sure both columns are numeric
    for col, name in [(x_column, 'x'), (y_column, 'y')]:
        if not pd.api.types.is_numeric_dtype(df[col]):
            print(f"Column '{col}' is not numeric. Attempting to convert...")
            try:
                df[col] = pd.to_numeric(df[col])
            except:
                print(f"Failed to convert '{col}' to numeric type.")
                return None
    
    # Create figure
    plt.figure(figsize=(10, 6))
    
    # Create scatter plot
    plt.scatter(df[x_column], df[y_column], color=color, alpha=0.6, edgecolor='black')
    
    # Add trend line
    z = np.polyfit(df[x_column], df[y_column], 1)
    p = np.poly1d(z)
    plt.plot(df[x_column], p(df[x_column]), "r--", alpha=0.8)
    
    # Calculate correlation coefficient
    corr = df[x_column].corr(df[y_column])
    
    # Add title and labels
    if title is None:
        title = f"{y_column} vs {x_column} (Correlation: {corr:.2f})"
    plt.title(title, fontsize=14)
    plt.xlabel(x_column, fontsize=12)
    plt.ylabel(y_column, fontsize=12)
    
    # Add correlation text
    plt.annotate(f"Correlation: {corr:.2f}", 
                xy=(0.05, 0.95), xycoords='axes fraction',
                fontsize=10, ha='left', va='top',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.5))
    
    # Add grid
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save or display the chart
    if save_path is not None:
        try:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            print(f"Scatter plot saved to {save_path}")
            return save_path
        except Exception as e:
            print(f"Error saving chart: {str(e)}")
            plt.close()
            return None
    else:
        plt.show()
        plt.close()
        return None

def create_heatmap(df, columns=None, title=None, cmap='coolwarm', save_path=None):
    """
    Create a correlation heatmap visualization.
    
    Args:
        df (pandas.DataFrame): Input DataFrame
        columns (list): List of columns to include or None for all numeric columns
        title (str): Chart title or None to auto-generate
        cmap (str): Colormap for the heatmap
        save_path (str): Path to save the chart or None to display
        
    Returns:
        str: Path to the saved chart or None if not saved
    """
    if df is None or df.empty:
        print("No data to visualize.")
        return None
    
    # Get numeric columns if not specified
    if columns is None:
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    else:
        # Verify all columns exist and are numeric
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
        print("No numeric columns found for correlation heatmap.")
        return None
    
    if len(numeric_cols) < 2:
        print("At least two numeric columns are required for a correlation heatmap.")
        return None
    
    # Calculate correlation matrix
    corr_matrix = df[numeric_cols].corr()
    
    # Create figure (adjust size based on number of columns)
    size = max(8, len(numeric_cols) * 0.8)
    plt.figure(figsize=(size, size))
    
    # Create heatmap
    plt.imshow(corr_matrix, cmap=cmap, interpolation='none', aspect='equal')
    
    # Add colorbar
    plt.colorbar(label='Correlation Coefficient')
    
    # Add title
    if title is None:
        title = "Correlation Matrix Heatmap"
    plt.title(title, fontsize=14)
    
    # Add labels and annotations
    plt.xticks(range(len(numeric_cols)), numeric_cols, rotation=45, ha='right')
    plt.yticks(range(len(numeric_cols)), numeric_cols)
    
    # Add correlation values in the cells
    for i in range(len(numeric_cols)):
        for j in range(len(numeric_cols)):
            text_color = 'black' if abs(corr_matrix.iloc[i, j]) < 0.7 else 'white'
            plt.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}', 
                    ha='center', va='center', color=text_color)
    
    plt.tight_layout()
    
    # Save or display the chart
    if save_path is not None:
        try:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
            print(f"Correlation heatmap saved to {save_path}")
            return save_path
        except Exception as e:
            print(f"Error saving chart: {str(e)}")
            plt.close()
            return None
    else:
        plt.show()
        plt.close()
        return None

def save_visualization(fig, chart_type, output_dir="visualizations"):
    """
    Save a visualization to a file.
    
    Args:
        fig: Matplotlib figure object
        chart_type (str): Type of chart
        output_dir (str): Directory to save visualizations
        
    Returns:
        str: Path to the saved file, or None if saving fails
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{chart_type}_{timestamp}.png"
        output_path = os.path.join(output_dir, filename)
        
        # Save figure
        fig.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close(fig)
        print(f"Visualization saved to {output_path}")
        return output_path
    
    except Exception as e:
        print(f"Error saving visualization: {str(e)}")
        plt.close(fig)
        return None


if __name__ == "__main__":
    # Example usage
    from data_cleaner import load_csv
    
    file_path = "example_data/sample_sales.csv"
    df = load_csv(file_path)
    
    if df is not None:
        # Create a bar chart
        create_bar_chart(df, 'Region', 'Revenue', title='Revenue by Region')
        
        # Create a line chart
        create_line_chart(df, 'Date', 'Revenue', title='Revenue over Time')
        
        # Create a pie chart
        create_pie_chart(df, 'Product', 'Revenue')
        
        # Create a histogram
        create_histogram(df, 'Revenue', bins=10)
        
        # Create a scatter plot
        create_scatter_plot(df, 'Units', 'Revenue')
        
        # Create a heatmap
        create_heatmap(df, ['Units', 'Revenue'])