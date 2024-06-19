# RecSys/products.py   LOGICE
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel
import numpy as np

# Load the data
df = pd.read_csv("C:/Users/oudid/OneDrive/Bureau/DataBases/Zara-products-BD/PRODUCTS.csv")

# Fill missing descriptions with empty strings
df['DESCRIPTION'] = df['DESCRIPTION'].fillna('')

# Initialize the TF-IDF vectorizer
tfv = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), min_df=2, max_df=0.8)

# Fit and transform the descriptions to a TF-IDF matrix
tfv_matrix = tfv.fit_transform(df['DESCRIPTION'])

# Compute the sigmoid kernel
sig = sigmoid_kernel(tfv_matrix, tfv_matrix)

# Reverse mapping of indices and product names
indices = pd.Series(df.index, index=df['PRODUCT_NAME']).drop_duplicates()


def give_rec(PRODUCT_NAME, sig=sig):
    idx_list = indices[indices.index == PRODUCT_NAME].tolist()
    if not idx_list:
        return []

    sig_scores = np.mean([sig[idx] for idx in idx_list], axis=0)
    sig_scores = list(enumerate(sig_scores))

    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)
    sig_scores = sig_scores[1:20]

    product_indices = [i[0] for i in sig_scores]

    return df['PRODUCT_NAME'].iloc[product_indices].tolist()
