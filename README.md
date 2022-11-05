# Real estate prices vs. income: Analysis for Swiss housing market in year 2021

In this analysis we compare real estate prices (for rent and purchase) across cantons of Switzerland and put them in relation to income. We use web-scraped real estate data which is providing current market prices (rent and pruchase), income data, and some support data for enrichment (canton-zip lookup table). 

## The questions to answer
* For which canton are the most real estate ads published online?
* In which canton the median price per square meter is the highest compared to the income tax level?
* Is there any correlation between income tax level and the median price per square meter on canton level?

## Data sources
Used data sources are stored in projects "data" folder.
* Real estate rental prices: immoscout_rent_stage_v1.csv (web scraped from immoscout24.ch)
* Real estate pruchase prices: homegate_buy_stage_v1.csv (web scraped from homegate.ch)
* Income data per canton: income_data_src.xlsx (Income data by federal tax administration. Source: https://www.estv.admin.ch/estv/de/home/die-estv/steuerstatistiken-estv/allgemeine-steuerstatistiken/direkte-bundessteuer/dbst-np-kanton-ab-1983.html)
* ZIP-Canton lookup table: zip_canton_lookup.xlsx (PLZ_Verzeichnis, Die Post. Source: https://swisspost.opendatasoft.com/explore/dataset/plz_verzeichnis_v2/information/?disjunctive.postleitzahl)

## Processing data and deriving answers
Scripts used for processing data are stord in projects "processing" folder.
* t01_extract_incomes.py: Extract income data per canton from excel report provided by federal tax administration)
* t02_merging.py: Augment real estate data with canton code and merge all data given to a single data set
* t03_num_of_ads_per_canton.py: Answering question "For which canton are the most real estate ads published online?"
* t04_median_price_per_m2.py: Answering question "In which canton the median price per square meter is the highest compared to the income tax level?"
* t05_corr_income_vs_price.py: Answering question "Is there any correlation between income tax level and the median price per square meter on canton level?"

Figures produced as base to answer questions are stored in projects "figures" folder.

## Results
The results are kept in pdf-file "Real-Estate-vs-Income-Analysis-Outcomes.pdf".

## Comments
* Web scraping of real estate platforms (immoscout24.ch and homegate.ch) in order to get rental/purchase prices was conducted beforehand and is not part of the analysis project above.
* Real estate data sample used is not representative for Swiss housing market due to limited web scraping capacities.

