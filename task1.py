import pandas as pd
import matplotlib.pyplot as plt


data_path = 'API_SP.POP.TOTL_DS2_en_csv_v2_9949.csv'
population_df = pd.read_csv(data_path, skiprows=4)  

year_columns =  population_df.columns[4:-1]  
global_population_trend = population_df[year_columns].sum()
global_population_trend_df = pd.DataFrame(global_population_trend).reset_index()
global_population_trend_df.columns = ['Year', 'Global Population']
global_population_trend_df['Year'] = global_population_trend_df['Year'].astype(int)


plt.figure(figsize=(12, 6))
plt.plot(global_population_trend_df['Year'], global_population_trend_df['Global Population'] / 1e9, marker='o', color='b')
plt.title("Global Population Trend (1960-2023)")
plt.xlabel("Year")
plt.ylabel("Population (Billions)")
plt.grid(True)
plt.show()
