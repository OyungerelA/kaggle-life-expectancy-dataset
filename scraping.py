import pandas as pd
import numpy as np

df = pd.read_csv("API_SP.DYN.LE00.IN_DS2_en_csv_v2_4901681.csv", skiprows=4)
new_cols = df[["Country Name", "Country Code", "Indicator Name", "2010"]]
new_cols.to_csv("life_expectancy_2010.csv", encoding="utf-8", index=False)
