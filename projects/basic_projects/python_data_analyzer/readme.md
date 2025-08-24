# Python Data Analyzer

A beginner-friendly Python application that analyzes CSV files, performs statistical calculations, and creates visualizations. This project showcases fundamental Python programming skills without requiring any external API connections.

## Features

- Import and clean CSV files
- Perform statistical analysis (mean, median, range, etc.)
- Group and aggregate data
- Generate visualizations
  - Bar charts
  - Line charts
  - Pie charts
  - Histograms
  - Scatter plots
  - Correlation heatmaps
- Export results to new files
- Simple command-line interface

## Project Structure

```
data_analyzer/
├── README.md                  # Documentation
├── requirements.txt           # Dependencies
├── data_analyzer.py           # Main module
├── data_cleaner.py            # Data cleaning functions
├── statistics_helper.py       # Statistical analysis
├── visualizer.py              # Data visualization
└── example_data/              # Sample data files
    └── sample_sales.csv
```

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/python-data-analyzer.git
   cd python-data-analyzer
   ```

2. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Analyze a CSV file with basic statistics and visualizations:

```
python data_analyzer.py example_data/sample_sales.csv
```

### Cleaning Data

Clean and preprocess the data before analysis:

```
python data_analyzer.py example_data/sample_sales.csv --clean --save-cleaned
```

### Statistical Analysis

Perform statistical analysis on specific columns:

```
python data_analyzer.py example_data/sample_sales.csv --stats --columns Revenue Units
```

### Group Analysis

Group data by a category and calculate aggregates:

```
python data_analyzer.py example_data/sample_sales.csv --group-by Region --agg-column Revenue --agg-func sum
```

### Time Series Analysis

Analyze how values change over time:

```
python data_analyzer.py example_data/sample_sales.csv --time-column Date --value-column Revenue --time-freq M
```

### Visualizations

Generate visualizations of the data:

```
python data_analyzer.py example_data/sample_sales.csv --visualize
```

### Combined Options

You can combine multiple options:

```
python data_analyzer.py example_data/sample_sales.csv --clean --stats --visualize --save-results
```

## Python Skills Demonstrated

- **Pandas** for data manipulation
- **NumPy** for numerical operations
- **Matplotlib** for data visualization
- File I/O operations
- Error handling and input validation
- Command-line argument parsing with **argparse**
- Object-oriented programming with modular design
- Statistical calculations
- Data cleaning and preprocessing

## Example Outputs

### Statistical Analysis
```
==================================================
Statistics for column: Revenue
==================================================
Count: 30
Missing Values: 0
Minimum: 4800.00
Maximum: 15000.00
Range: 10200.00
Mean: 9923.33
Median: 10000.00
Mode: 7200.00
Standard Deviation: 2780.56
Variance: 7731505.75
Skewness: 0.00
Kurtosis: -0.91
1st Quartile (Q1): 7700.00
3rd Quartile (Q3): 11925.00
Interquartile Range (IQR): 4225.00
==================================================
```

### Group Analysis
```
Grouped Data:
    Region  sum_Revenue
0    East        59700
1   North        64700
2   South        61500
3    West        74000
```

### Time Series Analysis
```
Time Series Analysis:
         Date  Revenue_sum  Revenue_mean  Revenue_count
0  2023-01-31       54000       10800.0              5
1  2023-02-29       50200       10040.0              5
2  2023-03-31       50700       10140.0              5
3  2023-04-30       47800        9560.0              5
4  2023-05-31       49900        9980.0              5
5  2023-06-30        6800        6800.0              1
```

## Sample Visualizations

The Data Analyzer generates various visualizations to help you understand your data better. Here are examples of visualizations created from the sample sales data:

### Bar Chart
![Bar Chart Example](visualizations/bar_Region_Units.png)
*Units by Region*

The bar chart shows the distribution of units sold across different regions. Each bar represents multiple data points for a region. The West region shows the highest maximum sales (30 units), while all regions demonstrate a comparable range of unit sales.

### Correlation Heatmap
![Heatmap Example](visualizations/correlation_heatmap.png)
*Correlation Matrix*

The correlation heatmap visualizes relationships between numeric variables. For the sample data, it shows a moderate positive correlation (0.49) between Units and Revenue, indicating that as unit sales increase, revenue tends to increase as well, but the relationship isn't perfectly linear.

### Histogram
![Histogram Example](visualizations/histogram_Units.png)
*Distribution of Units*

The histogram displays the frequency distribution of values in a column. In this example, units sold range from approximately 8 to 30, with a fairly even distribution. The mean (17.83) and median (17.50) are very close, suggesting a symmetric distribution.

### Pie Chart
![Pie Chart Example](visualizations/pie_Region_Units.png)
*Units Distribution by Region*

The pie chart shows the percentage breakdown by category. In the sample data, units are remarkably evenly distributed across all four regions (South: 26.2%, North: 25.0%, East: 24.7%, West: 24.1%), with only about a 2% difference between the highest and lowest regions.

### Scatter Plot
![Scatter Plot Example](visualizations/scatter_Units_Revenue.png)
*Revenue vs Units*

The scatter plot reveals relationships between two numeric variables. This visualization confirms the moderate positive correlation between units sold and revenue (0.49). The variability of points around the trend line suggests that other factors (like product type or pricing strategies) also significantly influence revenue.

## Interpreting the Results

The visualizations provide several insights into the sample sales data:

1. **Regional Performance**: Sales are remarkably balanced across all regions, suggesting effective market penetration.

2. **Units-Revenue Relationship**: While more units generally mean more revenue, the relationship is not perfectly linear (correlation coefficient of 0.49).

3. **Distribution Patterns**: The units sold follow a fairly symmetric distribution centered around 17-18 units.

4. **Product Pricing Variations**: The scatter plot shows varying revenue for similar unit counts, indicating different price points or product values.

All visualizations are saved in the `visualizations` directory. You can customize the analysis by specifying different columns or grouping options using the command-line parameters described earlier in this README.