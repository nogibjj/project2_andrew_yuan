import pandas as pd

def fetch_country_info(df, country_name):
    if not isinstance(country_name,str):
        print("Please input a valid country name")
        return "Bad input, NO data return"
    country_data = df[df['Country'] == country_name]
    if len(country_data) ==0 :
        print("There is no data for this country")
        return "No data for this country"
    else:
        print(country_data.iloc[0,0:5])
        return country_data.iloc[0,0:5]

def sort_top_30_by_ts(df):
    df.sort_values(by=['Total Cases'], ascending=False)
    print(df['Country'].head(30))
    pass

def colomn_name_sanity(df):
    for i in range(len(df.columns)):
        # i is the column name
        df.columns.values[i] = df.columns.values[i].replace("\n", " ")
    pass