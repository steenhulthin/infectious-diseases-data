import pandas as pd

# URL to the data - this is a csv file with semicolon as separator
url = "https://steenhulthin.github.io/infectious-diseases-data/01_influenza_noegletal_saeson_region_agegrp.csv"

# From pandas 0.17.0 - before this you need to google how to do (it's still pretty straight forward). 
df = pd.read_csv(url, sep=";")

#do something with the data
print(df.head())