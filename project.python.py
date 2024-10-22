import pandas as pd

# Define file paths for the dataset
filepath_dict = {
    'yelp': 'data/sentiment_analysis/yelp_labelled.txt',
    'amazon': 'data/sentiment_analysis/amazon_cells_labelled.txt',
    'imdb': 'data/sentiment_analysis/imdb_labelled.txt'
}

# Load the data into a Pandas DataFrame
df_list = []
for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=['sentence', 'label'], sep='\t')
    df['source'] = source  # Add a column with the data source name
    df_list.append(df)

# Concatenate all dataframes into one
df = pd.concat(df_list)

# Print the first row to verify
print(df.iloc[0])
