"""
# this application is going to sort the countries based on the total 
# cases and return the top 30 contries
"""
import sys
import getopt
import pandas as pd
from data_processing import fetch_country_info, sort_top_30_by_ts,colomn_name_sanity



if __name__ == '__main__':
    # Remove 1st argument from the
    # list of command line arguments
    argumentList = sys.argv[1:]
    # Options
    # ":" follows by the option means that option should have a corresponding value next to it
    options = "d:s"
    # Long options
    long_options = ["Display=", "Sort"]
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        df = pd.read_csv(values[0])
        df.columns.values[0] = 'index'
        df.columns.values[1] = 'Country'
        colomn_name_sanity(df)
        # checking each argument
        for currentArgument, currentValue in arguments:
    
            if currentArgument in ("-d", "--Display"):
                print("Display")
                print (("The country name is % s") % (currentValue))
                fetch_country_info(df,currentValue)
                
            elif currentArgument in ("-s", "--Sort"):
                print ("Sort")
                sort_top_30_by_ts(df)
                
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))
    
    
