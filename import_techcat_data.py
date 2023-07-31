# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:55:17 2023

@author: b247234
"""

import pandas as pd
import requests
from io import BytesIO
pd.options.display.max_colwidth = 300

#%% Technology catalogues

#0: data_sheets_for_renewable_fuels.xlsx
#1: energy_transport_datasheet.xlsx
#2: technology_data_catalogue_for_energy_storage.xlsx
#3: technology_data_for_carbon_capture_transport_storage.xlsx
#4: technology_data_for_el_and_dh.xlsx
#5: technology_data_for_industrial_process_heat.xlsx
#6: technology_data_heating_installations.xlsx

#Choose your technology catalogue
techcatalogue = 0


#%%
# File names in the repository
datalist = [
        'data_sheets_for_renewable_fuels.xlsx',
        'energy_transport_datasheet.xlsx',
        'technology_datasheet_for_energy_storage.xlsx',
        'technology_data_for_carbon_capture_transport_storage.xlsx',
        'technology_data_for_el_and_dh.xlsx',
        'technology_data_for_industrial_process_heat.xlsx',
        'technology_data_heating_installations.xlsx'
]

# GitHub repository URL
github_url = "https://github.com/DEATechData/technology_catalogues"

# Function to read all sheets from an Excel file on GitHub and filter out unwanted sheets
def read_selected_sheets_from_github(url):
    response = requests.get(url)
    if response.status_code == 200:
        sheets_dict = pd.read_excel(BytesIO(response.content), sheet_name=None)
        return sheets_dict
    else:
        raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")

# Read selected sheets for each file and store in a dictionary
data_dict = {}
for file_name in datalist:
    file_url = f"{github_url}/raw/main/{file_name}"
    data_dict[file_name] = read_selected_sheets_from_github(file_url)

# Now you have the data in data_dict, where keys are the file names and values are dictionaries of DataFrames.
# You can access them like this:
# data_dict["filename1.xlsx"]["sheet1"]
# data_dict["filename1.xlsx"]["sheet2"]
# data_dict["filename2.xlsx"]["sheet1"]
# data_dict["filename2.xlsx"]["sheet2"]
# ...

# Example: Print the first few rows of 'alldata_flat' in 'data_sheets_for_renewable_fuels.xlsx'
print(data_dict[datalist[0]]['alldata_flat'].head())
