import pandas as pd
df = pd.read_csv("/content/homelessness_shelter_data.csv")
df.columns = df.columns.str.strip()
df["date"] = pd.to_datetime(df['date'])

df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True) 

shelter_dim = df[['shelter_name', 'city', 'state', 'notes']].drop_duplicates().reset_index(drop=True)
shelter_dim.insert(0, 'shelter_id', shelter_dim.index + 1)
season_dim = df[["season"]].drop_duplicates().reset_index(drop=True)
season_dim.insert(0, 'season_id', season_dim.index + 1)
date_dim = pd.DataFrame({'date': df['date'].unique()})
date_dim.sort_values(by='date', inplace=True)
date_dim.reset_index(drop=True, inplace=True)
date_dim.insert(0, 'date_id', date_dim.index + 1)
date_dim['year'] = date_dim['date'].dt.year
date_dim['month'] = date_dim['date'].dt.month
date_dim['day'] = date_dim['date'].dt.day
date_dim['day_of_week'] = date_dim['date'].dt.day_name()
fact_df = df.merge(shelter_dim, on=['shelter_name', 'city', 'state', 'notes'])
fact_df = fact_df.merge(season_dim, on='season')
fact_df = fact_df.merge(date_dim, on='date')

shelter_occupancy_fact = fact_df[[
    'id', 'shelter_id', 'season_id', 'date_id',
    'total_capacity', 'occupied_beds', 'available_beds',
    'occupancy_rate', 'average_age', 'male_percentage', 'female_percentage'
]].rename(columns={'id': 'occupancy_id'})

shelter_occupancy_fact.to_csv("shelter_occupancy_fact.csv", index=False)
date_dim.to_csv("date_dim.csv", index=False)
shelter_dim.to_csv("shelter_dim.csv", index=False)
season_dim.to_csv("season_dim.csv", index=False)
