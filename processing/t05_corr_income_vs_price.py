# ----------------------------------------------------------------------------------------------------------------------
# ------ Is there any correlation between income tax level and the median price per square meter on canton level? ------
# ------------------------------------- Calculate correlation coefficient ----------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from t02_merging import df_rent_final, df_buy_final


# Pearson standard correlation coefficient. Returns the pearson r-value without p-value
def corr_determ_wo_pv(df: pd.DataFrame, col_1: pd.Series, col_2: pd.Series):
    return print("r-value:", df[col_1].corr(df[col_2]))

# Apply above function with "MEDIAN_PRICE_PER_M2" and "AVG_INCOME"
corr_determ_wo_pv(df_rent_final, "price_per_m2_median", "avg_income")
corr_determ_wo_pv(df_buy_final, "price_per_m2_median", "avg_income")


# Define function to plot linear model MEDIAN_PRICE_PER_M2" vs. "AVG_INCOME"
def lm_plot(df: pd.DataFrame, x_col: str, y_col: str, plot_title: str, file_name: str, format: str= "png"):
    figur = sns.lmplot(x=x_col, y=y_col, data=df)
    figur.set(xlabel="median price per m2", ylabel="avg income")
    figur.fig.suptitle(plot_title)
    plt.savefig(f"./figures/{file_name}.{format}", dpi=600)
    # Clear current figure
    plt.clf()
    return print("Figure plotted")


# apply above function to plot linear models
lm_plot(
            df=df_rent_final,
            x_col="price_per_m2_median",
            y_col="avg_income",
            plot_title="Median rental price per m2 vs \n avg income (on canton level)",
            file_name="corr_plot_rent_data_median_price_per_m2_vs_income"
        )

lm_plot(
            df_buy_final,
            x_col="price_per_m2_median",
            y_col="avg_income",
            plot_title="Median purchase price per m2 vs \n avg income (on canton level)",
            file_name="corr_plot_purchase_data_median_price_per_m2_vs_income"
        )
