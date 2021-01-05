import pandas as pd
import numpy as np
from sklearn import preprocessing
from scipy.stats import chi2_contingency

def data_ecoder(source_table):
    # exclude columns
    columns_removed = []
    raw_data = source_table[[i for i in source_table.columns if i not in columns_removed]]

    # label encoding
    label = preprocessing.LabelEncoder()
    data_encoded = pd.DataFrame() 

    for _column in raw_data.columns:
        data_encoded[_column] = label.fit_transform( raw_data[_column] )

    return data_encoded

def cramers_V(var1,var2) :
    crosstab =np.array(pd.crosstab(var1,var2, rownames=None, colnames=None)) # Cross table building
    chi2_result = chi2_contingency(crosstab)
   
    stat = chi2_result[0] # Keeping of the test statistic of the Chi2 test
    stat = stat ** .5
    obs = np.sum(crosstab) # Number of observations
    mini = min(crosstab.shape)-1 # Take the minimum value between the columns and the rows of the cross table
    
    crm = (stat/(obs*mini))
    
    # print( crosstab, chi2_result, stat, obs, mini, crm )
    return crm

def run_stats(data_encoded):
    rows= []
    for var1 in data_encoded:
        col = []
        for var2 in data_encoded:
            # print(var1,var2)
            cramers =cramers_V(data_encoded[var1], data_encoded[var2]) # Cramer's V test
            col.append(round(cramers,2)) # Keep rounded value from Cramer's V  
        rows.append(col)

    cramers_results = np.array(rows)
    cramer_v_df = pd.DataFrame(cramers_results, columns = data_encoded.columns, index =data_encoded.columns)
    return cramer_v_df

def main():
    # read data
    source_table = pd.read_csv("path/to/data.csv")
    data_encoded = data_ecoder(source_table)
    cramer_v_df = run_stats(data_encoded)
    # print(cramer_v_df.head)
    cramer_v_df.to_csv('cramer_v_df.csv' )
    return 

if __name__ == '__main__':
    cramer_v_df = main()
