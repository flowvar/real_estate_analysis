# ----------------------------------------------------------------------------------------------------------------------
# ------------------------- For which canton the most real estate ads are published online? ----------------------------
# ----------------------------------------------------------------------------------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from t02_merging import df_rent, df_buy
from t02_merging import canton_lookup

# Apply look up for canton code on raw real estate data and assign output to new df variables
df_buy_incl_canton = canton_lookup(df_buy)
df_rent_incl_canton = canton_lookup(df_rent)

# Define function to group rent & buy data df by canton and count items.
# Return aggregated df sorted by num of advertisements.
def count_items(df: pd.DataFrame) -> pd.DataFrame:
    df = df.groupby(["canton_code"]).count()
    df = df.add_suffix("_count").reset_index()
    df = df.sort_values(by=["num_rooms_count"], ascending=False)
    df = df.rename(columns= {"num_rooms_count": "num_of_ads"})
    return df[["canton_code", "num_of_ads"]]


# Applying function and get dfs for further plotting
df_rent_count = count_items(df_rent_incl_canton)
df_buy_count = count_items(df_buy_incl_canton)


# Define function to plot bar plot
def bar_plot(df: pd.DataFrame, x_ax_naming: str, y_ax_naming: str, title: str, x_ax_df: str, y_ax_df: str, file_name:str, format:str = "png"):
    """
    :param df: data frame used as base for plot
    :param x_ax_naming: Naming for x-axis in output plot
    :param y_ax_naming: Naming for y-axis in output plot
    :param title: Title for output plot
    :param x_ax_df: Column in df used as x-axis values
    :param y_ax_df: Column in df used as y-axis values
    :param file_name: Filename used for storing/naming plot
    :param format: Format of file (png, jpeg etc. without dot)
    :return: string as confirmation plotting executed
    """
    # process canton column --> upper case letters for nicer look as axis labels
    df[y_ax_df] = df[y_ax_df].str.upper()
    # configure plot: style, axis lables, title
    sns.set_theme(style="whitegrid")
    rent_ad_count_graph = sns.barplot(x=x_ax_df, y=y_ax_df, data=df, ci=None, palette="Blues_d")
    rent_ad_count_graph.set(xlabel=x_ax_naming, ylabel=y_ax_naming)
    rent_ad_count_graph.set_title(title)
    rent_ad_count_graph.tick_params(labelsize=10)
    # storing
    plt.savefig(f"./figures/{file_name}.{format}")
    # Clear the current figure
    plt.clf()
    return print("Figure plotted")


# apply function on real estate rent data and save figure
bar_plot(df=df_rent_count,
        x_ax_naming="Number of advertisings",
        y_ax_naming="Canton",
        title="Ranking by number of rent advertisements per canton",
        x_ax_df="num_of_ads",
        y_ax_df="canton_code",
        file_name="Ranking_rent_advertisements")


# apply function on real estate buy data and save figure
bar_plot(df_buy_count,
        x_ax_naming="Number of advertisings",
        y_ax_naming="Canton",
        title="Ranking by number of purchase advertisements per canton",
        x_ax_df="num_of_ads",
        y_ax_df="canton_code",
        file_name="Ranking_purchase_advertisements")
