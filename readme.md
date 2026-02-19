# Infectious diseases data

The goal of the project is to make infectious diseases data easily accessible. 

Specifically the data available is from [Statens Serum Institut](https://www.ssi.dk) in Denmark and only data from Denmark is provided (for now at least).

The data is from the [SSI dashboards](https://experience.arcgis.com/template/099eb5c9acea4e18b411997815be2f98). Data for covid-19, influenza and RSV is available.

Data on [the site of this project](https://steenhulthin.github.io/infectious-diseases-data/) is updated at Wednesdays at 14.10 which is 10 minutes after the weekly data update by SSI. Data history is available from 2025-02-18 through the power of git.

Unlike in most of the original data the here is all in UTF-8 encoding. Except for this data is not altered. This includes leaving the separater as ';' (and not ','). 

[![Latest CSV Files](https://github.com/steenhulthin/infectious-diseases-data/actions/workflows/download_on_schedule_test.yml/badge.svg)](https://github.com/steenhulthin/infectious-diseases-data/actions/workflows/download_on_schedule_test.yml)

# usage

## from python

You can load the data directly into a dataframe with 

```python
import pandas as pd

# URL to the data - this is a csv file with semicolon as separator
url = "https://steenhulthin.github.io/infectious-diseases-data/01_influenza_noegletal_saeson_region_agegrp.csv"

# From pandas 0.17.0 - before this you need to google how to do (it's still pretty straight forward). 
df = pd.read_csv(url, sep=";")

#do something with the data
print(df.head())
```

## other usage

Just fetch the csv via the URL in code (remember it's ';'-separated). Do your thing with it. 
