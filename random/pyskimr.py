import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_dataframe(df):
    # Count number of rows and columns
    num_rows, num_cols = df.shape
    print("Number of rows:", num_rows)
    print("Number of columns:", num_cols)

    # List out frequency of data types in each column
    print("\nData type frequency:")
    print(df.dtypes.value_counts())

    # Initialize results dataframe
    results_df = pd.DataFrame(columns=["Data Type", "Column Name", "Missing Values", "% Non-missing",
                                        "Minimum Value", "Maximum Value", "Number of Empty Rows", 
                                        "Number of Unique Values", "Mean", "Median", "Mode", 
                                        "Standard Deviation", "25th Percentile", "50th Percentile", 
                                        "75th Percentile", "100th Percentile", "Unique Words"])

    # Analyze each column
    for col in df.columns:
        data_type = str(df[col].dtype)

        # Count missing data, % of data not missing, minimum value, maximum value, number of empty rows
        missing_data = df[col].isna().sum()
        percent_non_missing = round(1 - (missing_data / num_rows), 4) * 100
        min_value = df[col].min()
        max_value = df[col].max()
        empty_rows = df[col].eq('').sum()

        # Initialize values for data type specific analysis
        unique_vals = None
        mean_val = None
        median_val = None
        mode_val = None
        std_dev_val = None
        p25 = None
        p50 = None
        p75 = None
        p100 = None
        unique_words = None

        # Analyze based on data type
        if data_type == "object" or data_type == 'pandas.core.series.Series':
            # Count number of unique observations, words per row, total words, list all unique words
            unique_vals = df[col].nunique()
            words_per_row = df[col].str.split().str.len()
            total_words = words_per_row.sum()
            unique_words = pd.Series(' '.join(df[col]).split()).value_counts()
    

        elif data_type == "float64" or data_type == "int64":
            # Find % of data not missing, mean, median, mode, standard deviation, percentile (25, 50, 75, 100), 
            percent_non_missing = round(1 - (missing_data / num_rows), 4) * 100
            mean_val = df[col].mean()
            median_val = df[col].median()
            mode_val = df[col].mode()
            std_dev_val = df[col].std()
            p25 = df[col].quantile(0.25)
            p50 = df[col].quantile(0.50)
            p75 = df[col].quantile(0.75)
            p100 = df[col].quantile(1)

            # Visualize histogram for each unique observation
            plt.hist(df[col], bins=10)
            plt.title(col)
            plt.show()

        elif data_type == "datetime64":
            # Find % of data not missing, min date, max date, and number of unique observation
            percent_non_missing = round(1 - (missing_data / num_rows), 4) * 100
            min_val = df[col].min()
            max_val = df[col].max()
            unique_vals = df[col].nunique()

        elif data_type == "bool":
            # Count True/False values
            value_counts = df[column].value_counts(dropna=False)
            true_count = value_counts[True] if True in value_counts else 0
            false_count = value_counts[False] if False in value_counts else 0
            missing_count = df[column].isnull().sum()
            total_count = len(df[column])
            percent_missing = missing_count / total_count * 100
            percent_nonmissing = 100 - percent_missing
            
            # Print results
            print(f"Column: {column}")
            print(f"Data type: bool")
            print(f"Number of True values: {true_count}")
            print(f"Number of False values: {false_count}")
            print(f"Number of missing values: {missing_count}")
            print(f"Percent missing: {percent_missing:.2f}%")
            print(f"Percent non-missing: {percent_nonmissing:.2f}%\n")



# New function to count words in a column
def count_words(df):
    # Count the number of unique observations in the series and list them
    unique_obs = df.value_counts()
    print(f"Unique observations in the series:\n{unique_obs}\n")


# Create Data Frame
# Generate some example data for each column
col1 = np.random.randint(low=0, high=100, size=500)
col2 = np.random.normal(loc=50, scale=10, size=500)
col3 = np.random.choice(['Action', 'Comedy', 'Drama', 'Horror'], size=500)
col4 = np.random.choice([True, False], size=500)
col5 = pd.date_range(start='2022-01-01', end='2022-12-31', periods=500)
col6 = np.random.randint(low=0, high=100, size=500)
col7 = np.random.normal(loc=50, scale=10, size=500)
col8 = np.random.choice(['Action', 'Comedy', 'Drama', 'Horror'], size=500)
col9 = np.random.choice([True, False], size=500)
col10 = pd.date_range(start='2022-01-01', end='2022-12-31', periods=500)

# Create the dataframe
df = pd.DataFrame({
    'Title': ['Movie ' + str(i) for i in range(1, 501)],
    'Year': pd.to_datetime(col5).year,
    'Month': pd.to_datetime(col5).month,
    'Day': pd.to_datetime(col5).day,
    'Runtime (mins)': col2,
    'Budget ($mil)': col7,
    'Box Office ($mil)': col1,
    'IMDB Rating': col8,
    'Genre': col3,
    'Director': ['Director ' + str(i) for i in range(1, 501)],
})

