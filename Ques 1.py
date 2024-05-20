#file  # type: ignore

import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
wine_data = load_wine(as_frame=True)
wine_df = wine_data.frame
wine_df

print(wine_df.isnull().sum())
wine_df.fillna(wine_df.mean(), inplace=True)

Q1 = wine_df.quantile(0.25)
Q3 = wine_df.quantile(0.75)
IQR = Q3 - Q1
outliers = np.where((wine_df < (Q1 - 1.5 * IQR)) | (wine_df > (Q3 + 1.5 * IQR)))
wine_df['outliers'] = wine_df.median()

inconsistent_values = wine_df[wine_df['alcohol'] < 0]
wine_df.loc[inconsistent_values.index, 'alcohol'] = wine_df['alcohol'].median()
wine_df

validation_rules = {
'alcohol': {'min': 0, 'max': 20},
'malic_acid': {'min': 0, 'max': 5},
'magnesium': {'min': 0, 'max': 150},
'alcalinity_of_ash': {'min': 0, 'max': 50},
}

for column, rules in validation_rules.items():
if wine_df[column].min() < rules['min'] or wine_df[column].max() >␣
↪rules['max']:
print(f"Validation failed for column {column}")
else:
print(f"Validation passed for column {column}")
