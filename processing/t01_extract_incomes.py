# ----------------------------------------------------------------------------------------------------------------------
# -------------- Extracting income data from xlsx report provided by federal bereau of statistics ----------------------
# ----------------------------------------------------------------------------------------------------------------------

import pandas as pd

# Prerequisits: pipenv install openpyxl
xlsx_file = pd.ExcelFile("./data/income_data_src.xlsx")

# Init dict to map sheet name and df
sheet_to_df_map = {}

# Map sheet name and sheet content as df in dict
for sheet in xlsx_file.sheet_names:
    sheet_to_df_map[sheet] = xlsx_file.parse(sheet)

# Init empty lists for storing values of interest
canton_ls = []
num_tax_payers_ls = []
income_for_taxation_ls = []
pure_income_ls =[]
amount_of_tax_2018_ls = []

# Iterate over dict (sheets, dfs). Append canton code from sheet name and extract values from row index 59
for sheet_name, df in sheet_to_df_map.items():
    canton_ls.append(sheet_name)
    num_tax_payers_ls.append(df.iloc[59,2])
    income_for_taxation_ls.append(df.iloc[59,3])
    pure_income_ls.append(df.iloc[59,5])
    amount_of_tax_2018_ls.append(df.iloc[59,6])

# Create df from resulting lists
df_income = pd.DataFrame({"canton":canton_ls, "num_tax_payers": num_tax_payers_ls, \
                          "income_for_taxation":income_for_taxation_ls, "pure_income":pure_income_ls, \
                          "amount_of_tax_2018_":amount_of_tax_2018_ls})
