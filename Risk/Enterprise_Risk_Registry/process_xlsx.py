#!/c/Users/erica/Anaconda3/python

import pandas as pd
import sqlite3 as lite

# Source of mock data.

# Previously defined list of descriptor valuse associated with each risk metric
descriptor_dictionary = {
        'likelihood' : { '1': 'Rare', '2': 'Unlikely', '3': 'Possible', '4': 'Likely', '5': 'Almost Certain'
        },
        'Opportunity' : { '5' : 'Transformative', '4' : 'Outstanding', '3' : 'Intermidiate', '2' : 'Adaquate', '1' : 'Incidental'
        },
        'Threat' : {  '5' : 'Critical', '4' : 'Major', '3' : 'Moderate', '2' : 'Minor', '1' : 'Negligible'
        },
        'control' : {'5' : 'Minimally effective', '4' : 'Marginally effective', '3' : 'Moderately effective', '2' : 'Effective', '1' : 'Very effective'
        }
    }

def database_connect(database):
    """
    Connects to existing database, or creates a database and connects.
    Input: database file path
    output: connection (con) object
    """
    con = lite.connect(database)
    return con

def read_xlsx(xlsx_file):
    """
    Reads excel file into dataframe(memory). 
    """
    df = pd.read_excel(xlsx_file)
    return df

def risk_descriptor(df,field):
    # Label new field
    new_field_name = field +' Descriptor'
    # Change data type of input field
    df[field] = df[field].apply(str)
    # Create new list object
    result = []
    for index,row in df.iterrows():
        descriptor = descriptor_dictionary[row['Risk Class']][row[field]]
        result.append(descriptor)
    # Merge list object to dataframe
    df[new_field_name] = result
    return

def stats_descriptor(df,field,key):
    
    new_field_name = field +' Descriptor'
    
    df[field] = df[field].apply(str)
    df[new_field_name] = df[field].map(descriptor_dictionary[key])

def describe_risk_metrics(df):

    stats_descriptor(df,'Inherent Likelihood','likelihood')
    risk_descriptor(df,'Inherent Impact')
    stats_descriptor(df,'Residual Likelihood','likelihood')
    risk_descriptor(df,'Residual Impact')
    stats_descriptor(df,'Controls Effectiveness','control')
    return

def color_mapper(df):
    result = []
    for index, row in df.iterrows():
        if row['Risk Class'] == 'Opportunity':
            scale = -1
        else:
            scale = 1
        product = row['Residual Impact']**2 * row['Residual Likelihood']**2 * scale
        result.append(product)
    df['Residual_Mapper'] = result
    return

def main(xlsx_file):
    """
    Read data to table from excel file into memory
    Perform transformation of data as need
    Produce a xlsx file with new data
    input: xlsx file,
    output: xlsx file
    """
    # read the original data file
    df = read_xlsx(xlsx_file)

    #Process data as needed
    color_mapper(df)
    describe_risk_metrics(df)

    # write processed data table to xlsx file
    df.to_excel(f'./proccesses_{xlsx_file}', index=False)
    return
    
if __name__ == '__main__':

    try:
        main(xlsx_file = 'mock_data.xlsx')

    except Exception as Error:
        print(Error)