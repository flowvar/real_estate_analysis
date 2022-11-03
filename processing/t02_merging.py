# ----------------------------------------------------------------------------------------------------------------------
# -------------- Merge given data sets to a single df which will be used to answer the research questions --------------
# ---------------------------- In addition, augment real estate data with canton codes ---------------------------------
# ----------------------------------------------------------------------------------------------------------------------

import pandas as pd

# For developing reasons show all columns
pd.set_option("display.max_columns", 100)

# Define path to real estate, income, and zip-canton lookup table
path_rent_data_set = "./data/immoscout_rent_stage_v1.csv"
path_buy_data_set = "./data/homegate_buy_stage_v1.csv"
path_income_data_set = "./data/income_stage.csv"
path_zip_canton_df = "./data/zip_canton_lookup.xlsx"

# Load real estate and income data as dfs
df_rent = pd.read_csv(path_rent_data_set, sep=";", header=0)
df_buy = pd.read_csv(path_buy_data_set, sep=";", header=0)
df_income = pd.read_csv(path_income_data_set, sep=",", header=0)

# Load zip-canton lookup data. extract only columns needed and remove duplicates (-> stable lookup table)
df_zip_canton = pd.read_excel(path_zip_canton_df)
df_zip_canton = df_zip_canton[["POSTLEITZAHL", "KANTON"]]
df_zip_canton = df_zip_canton.drop_duplicates()

# add new column "price_per_m2" to real estate data
df_rent["price_per_m2"] = df_rent["price"] / df_rent["m2"]
df_buy["price_per_m2"] = df_buy["price"] / df_buy["m2"]


# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------- Define functions to apply on both dfs ---------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Merge real estate data with canton codes from zip-canton lookup table
def canton_lookup(df_re: pd.DataFrame, lookup_df: pd.DataFrame=df_zip_canton) -> pd.DataFrame:
    df = df_re.merge(lookup_df, how="left", left_on="zip_code", right_on="POSTLEITZAHL")
    df = df[["num_rooms", "m2", "price", "price_per_m2", "KANTON"]]
    df = df.rename(columns={"KANTON":"canton_code"})
    df["canton_code"] = df["canton_code"].str.lower()
    return df

# Group real estate data by canton. Calculate median value
def canton_agg(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby(["canton_code"]).median()
    return df.add_suffix("_median").reset_index()

# Merge real estate data with income KPIs from income df
def merge_re_income(df_re, df_income: pd.DataFrame=df_income):
    df = df_re.merge(df_income, how="left", left_on="canton_code", right_on="canton")
    return df[["canton_code", "num_tax_payers", "income_for_taxation",
             "pure_income", "amount_of_tax_2018", "avg_income", "price_per_m2_median"]]


# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------- Apply functions to get dfs as analysis base ------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

df_rent_final = merge_re_income(  
                        canton_agg(
                            canton_lookup(
                                df_rent)))

df_buy_final = merge_re_income(
                        canton_agg(
                            canton_lookup(
                                df_buy)))


# Output merged data sets as csv
df_rent_final.to_csv("./data/rent_final_merged_stage.csv", index=False)
df_buy_final.to_csv("./data/buy_final_merged_stage.csv", index=False)
