import os

import numpy as np
import pandas as pd

from datetime import datetime

def assign_values():
    # Define the variables
    farm_ID     = np.random.randint(100,999)
    project_ID  = np.random.randint(1000,9999)
    start_year  = np.random.randint(2000,2020)
    end_year    = int(start_year + np.random.normal(3,.5,1))
    status      = 'Complete'
     
    now = datetime.now()
    if end_year > now.year:
        status = 'Open'

    # Return a dictionary
    return { 'farm_ID'      : farm_ID
             ,'project_ID'  : project_ID
             ,'status'      : status
             ,'start_year'  : start_year
             ,'end_year  '  : end_year   }

def generate_project_data(row_count,xlsx_name):
    # build a dataset
    list_of_dicts = []
    for row in range(row_count):
        temp_dict = assign_values()
        list_of_dicts.append(temp_dict)
    # write dataset to xlsx file    
    df = pd.DataFrame(list_of_dicts)
    df.to_excel(xlsx_name,index=False)

def main():
    xlsx_name = os.getcwd() + '/Mock_Data_Generators/Data/project_mock_data.xlsx'
    generate_project_data(1000, xlsx_name)
    return xlsx_name

if __name__ == '__main__':
    run_time_start = datetime.now()
    file_location = main()
    Windows_file_location = file_location.replace('/','\\')
    Unix_file_location = '/' + file_location.replace('\\','/').replace(':','')

    run_time_finish = datetime.now()
    runtime = run_time_finish - run_time_start
    print('\n')
    print(f'Script complete in {runtime}')
    print(f'Data file located at:\n Windows {Windows_file_location} \n Unix {Unix_file_location}')

# $ python Mock_Data_Generators/project_completion.py 
# Script complete in 0:00:00.245150