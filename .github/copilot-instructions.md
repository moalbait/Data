# AI Coding Instructions for CIMT Project

## Project Overview
This is a **data analysis and processing project** using Jupyter Notebooks with Python, pandas, and scientific computing libraries (numpy, scipy, matplotlib). The active work involves ETL (Extract-Transform-Load) operations on CSV datasets.

## Key Files & Structure
- `myenv/Scripts/Untitled-1.ipynb` - Main data analysis notebook (in development)
- `myenv/Scripts/BL-Flickr-Images-Book.csv.csv` - Source data file (British Library Flickr Images metadata)
- `myenv/` - Python 3.11 virtual environment with pandas, numpy, matplotlib, scipy, jupyter

## Data Processing Patterns
**DataFrame Operations Pattern:**
- Load CSV with `pd.read_csv()` - preserve index column with `index_col=0` when needed
- Drop unwanted columns using list syntax: `df.drop(columns_list, axis=1, inplace=True)`
- Rename/set index with `df.set_index('column_name')`
- Always call `.head()` after transformations to verify data structure

**Example from notebook:**
```python
columns_to_drop = ['Edition Statement','Corporate Author', 'Corporate Contributors', ...]
df = df.drop(columns_to_drop, axis=1, inplace=True)
df = df.set_index('Identifier')
```

## Development Workflow
1. **Environment Setup**: Use `myenv/Scripts/activate.ps1` (PowerShell) or `activate.bat` to activate virtual environment
2. **Running Notebooks**: Execute cells sequentially; verify outputs with `.head()` or `.info()` after each transformation
3. **Dependencies**: Core stack includes pandas, numpy, matplotlib, jupyter, scikit-learn (scipy)

## Notebook-Specific Conventions
- Each cell should be focused: data loading, transformation logic, or visualization
- Use comments above complex transformations to document purpose
- Print data structure verification (`.head()`, `.shape`, `.dtypes`) after major changes
- Store intermediate dataframes with descriptive names (e.g., `df_cleaned`, `df_aggregated`)

## Common Issues & Solutions
- **CSV File Issues**: Double extension (`.csv.csv`) is intentional - preserve filename as-is
- **inplace=True**: Used for DataFrame operations - returns None, doesn't create new object
- **Index Column**: Flickr dataset uses 'Identifier' as natural key - set as index for efficient lookups

## External Dependencies
- Remote data source: `https://cocl.us/datascience_survey_data` (online surveys data)
- Local data: `BL-Flickr-Images-Book.csv.csv` (metadata for 14K+ British Library Flickr images)
