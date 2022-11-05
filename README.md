# Real estate prices vs. income: Analysis of Swiss housing market

In this analysis we compare real estate prices (for rent and purchase) across cantons of Switzerland and put them in relation to income. We use web-scraped real estate data which provides current market prices, income data, and some support data for enrichment (canton-zip lookup table). 

## The questions to answer
* For which canton are the most real estate ads published online?
* In which canton the median price per square meter is the highest compared to the income level?
* Is there any correlation between income level and the median price per square meter on canton level?

## Data sources
Used data sources are stored in projects "data" folder.
* Real estate rental prices: immoscout_rent_stage_v1.csv (web scraped from immoscout24.ch)
* Real estate pruchase prices: homegate_buy_stage_v1.csv (web scraped from homegate.ch)
* Income data per canton: income_data_src.xlsx (Income data by federal tax administration. Source: https://www.estv.admin.ch/estv/de/home/die-estv/steuerstatistiken-estv/allgemeine-steuerstatistiken/direkte-bundessteuer/dbst-np-kanton-ab-1983.html)
* ZIP-Canton lookup table: zip_canton_lookup.xlsx (PLZ_Verzeichnis, Die Post. Source: https://swisspost.opendatasoft.com/explore/dataset/plz_verzeichnis_v2/information/?disjunctive.postleitzahl)

## Processing data and deriving answers
Scripts used for processing data are stored in projects "processing" folder.
* t01_extract_incomes.py: Extract income data per canton from excel report provided by federal tax administration
* t02_merging.py: Enrich real estate data with canton code and merge all data given to a single data set as analysis base
* t03_num_of_ads_per_canton.py: Answering question "For which canton are the most real estate ads published online?"
* t04_median_price_per_m2.py: Answering question "In which canton the median price per square meter is the highest compared to the income tax level?"
* t05_corr_income_vs_price.py: Answering question "Is there any correlation between income tax level and the median price per square meter on canton level?"

Figures produced as base to answer questions are stored in projects "figures" folder.

## Results
### For which canton are the most real estate ads published online?
Rent             |  Purchase
:-------------------------:|:-------------------------:
![](/figures/Ranking_rent_advertisements.png)  |  ![](/figures/Ranking_purchase_advertisements.png)
In the used sample the canton of Bern has the most rent advertisings online. | In the used sample the canton of Ticino has the most purchase advertisings online.

### In which canton the median price per square meter is the highest compared to the income level?
Rent             |  Purchase
:-------------------------:|:-------------------------:
![](/figures/Share_of_monthly_income_for_median_rental_price_m2.png)  |  ![](/figures/Share_of_yearly_income_for_median_purchase_price_m2.png)
Based on the used sample people in canton of Geneva have to pay the highest rent per square meter compared to their monthly income. | Based on the used sample people in canton of Uri must pay the highest purchase price per square meter compared to their yearly income.

### Is there any correlation between income level and the median price per square meter on canton level?
Rent             |  Purchase
:-------------------------:|:-------------------------:
![](/figures/corr_plot_rent_data_median_price_per_m2_vs_income.png)  |  ![](/figures/corr_plot_purchase_data_median_price_per_m2_vs_income.png)
There is a correlation between income level and median rent price per square. The R-value is 0.87. | There is a correlation between income level and median purchase price per square. But clearly there are some outliers. The R-value is 0.73.

The results are kept in pdf file "Real-Estate-vs-Income-Analysis-Outcomes.pdf".

## Comments
* Real estate data record date: December 2021
* Web scraping of real estate platforms (immoscout24.ch and homegate.ch) in order to get rental/purchase prices was conducted beforehand and is not part of the analysis project above.
* Real estate data sample used is not representative for Swiss housing market due to limited web scraping capacities.

