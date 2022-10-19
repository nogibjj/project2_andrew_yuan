"""
# this application is going to sort the countries based on the total 
# cases and return the top 30 contries
"""
import sys
import pandas as pd


def fetch_country_info(df, country_name):

    country_data = df[df['Country'] == country_name]
    if len(country_data) ==0 :
        print("There is no data for this country")
        return "No data for this country"
    else:
        print(country_data.iloc[0,0:5])
        return country_data.iloc[0,0:5]




if __name__ == '__main__':
    df = pd.read_csv(sys.argv[1])
