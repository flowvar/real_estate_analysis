# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------- Load data into MariaDB ---------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------- MariaDB was configured before using terminal and DB "cip" was created through terminal -------------------

# import libraries
import os
import sys

import mariadb
from sqlalchemy import create_engine

# import final merged dfs (rent and purchase) to load into DB:
from processing.t02_merging import df_rent_final, df_buy_final

# Init credentials
user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')
database = os.getenv('DATABASE')


# --------------------------------------------- load df into DB "cip" --------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# set up and create engine with sqlalchemy
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{user}:{password}@localhost:{port}/{database}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# load df_rent_final (final merge) into DB cip as table "final_rent_merged"
df_rent_final.to_sql(name="final_rent_merged", con=engine, if_exists="replace", index=False)

# load df_buy_final (final merge) into DB cip as table "final_purchase_merged"
df_buy_final.to_sql(name="final_purchase_merged", con=engine, if_exists="replace", index=False)


# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------- access mariadb for queries --------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Direct connection to mariadb to execute sql commands
def db_curl_exe(sql_command):
    # Instantiate Connection
    try:
         conn = mariadb.connect(
            user=user,
            password=password,
            host=host,
            port=port
            )

         # Instantiate Cursor
         cur = conn.cursor()

         cur.execute(sql_command)
         if not cur:
             print("no return")
         else:
            for element in cur:
             print(element)

         # Close Connection
         conn.close()

    except mariadb.Error as e:
          print(f"Error connecting to MariaDB: {e}")
          sys.exit(1)


# Execute SQL
db_curl_exe("SHOW DATABASES;")
