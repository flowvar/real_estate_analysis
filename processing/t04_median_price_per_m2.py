# ----------------------------------------------------------------------------------------------------------------------
# -------- In which canton the median price per square meter is the highest compared to the income tax level? ----------
# ----------------------------------------------------------------------------------------------------------------------

# import merged data sets and bar_plot function
from t02_merging import df_rent_final, df_buy_final
from t03_num_of_ads_per_canton import bar_plot

# Note:
# price / income --> "one median m2 is XX% of yearly income" --> 8000 [CHF/m2] / 79144.13204 [CHF] = 10%

# Add new column "income_price_ratio" to dfs
# calculate ratio for rent price using monthly income --> divide by 12
df_rent_final["income_price_ratio"] = df_rent_final["price_per_m2_median"] / (df_rent_final["avg_income"] / 12)
df_buy_final["income_price_ratio"] = df_buy_final["price_per_m2_median"] / df_buy_final["avg_income"]

# Calculate share of yearly income to buy/rent one median m2. Add result as column "income_price_share"
df_rent_final["income_price_share"] = df_rent_final["income_price_ratio"] * 100
df_buy_final["income_price_share"] = df_buy_final["income_price_ratio"] * 100

# Sort dfs for better plot design (order: largest values on top)
df_rent_final = df_rent_final.sort_values(['income_price_share'], ascending=False).reset_index(drop=True)
df_buy_final= df_buy_final.sort_values(['income_price_share'], ascending=False).reset_index(drop=True)

# apply function to plot figure showing rental data
bar_plot(
            df=df_rent_final,
            x_ax_naming="Share of monthly income [%]",
            y_ax_naming="Canton",
            title="Share of monthly income for median rental price/m2",
            x_ax_df="income_price_share",
            y_ax_df="canton_code",
            file_name="Share_of_monthly_income_for_median_rental_price_m2"
        )

# apply function to plot figure showing purchase data
bar_plot(
            df=df_buy_final,
            x_ax_naming="Share of yearly income [%]",
            y_ax_naming="Canton",
            title="Share of yearly income for median purchase price/m2",
            x_ax_df="income_price_share",
            y_ax_df="canton_code",
            file_name="Share_of_yearly_income_for_median_purchase_price_m2"
        )
