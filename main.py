import pandas as pd

df = pd.DataFrame(data={'cc': ['US', 'FR', 'DE'], 'val': [1, 2, 3]})

df['new_col'] = df['val'].apply(lambda x: x * 100)
df['continent'] = ['North America' if x == 'US' else 'Europe' for x in df['cc']]
print(df)