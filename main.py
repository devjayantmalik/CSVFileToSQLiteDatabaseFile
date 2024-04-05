from YamlConfig import YamlData
import sqlite3
import pandas as pd
from fix import fix_pandas



if __name__ == '__main__':
    # Fix pandas code to ignore duplicates
    fix_pandas()

    config = YamlData()

    # Step 1:
    # ==========
    # Execute sql from provided file
    db = sqlite3.connect("./db.sqlite")
    try:
        with open(config.step1.sql_filepath, mode="r") as file:
            result = db.execute(file.read())
    except Exception as ex:
        print(f"Error in step1: {ex}")

    # Step 2:
    # ===========
    # Read CSV File
    for csv_filepath in config.step2.csv_filepaths:
        csvfile = pd.read_csv(csv_filepath)
        # Replace column names with sqlite ones.
        csvfile.rename(columns=config.step2.columns_map, inplace=True)

        # Insert data
        try:
            sql = csvfile.to_sql(name=config.step2.table_name, con=db, if_exists="append", index=False)
        except Exception as ex:
            print(f"Exception in Step2 SQL Execution: {ex}")

    # Step 3:
    # ============
    # Execute SQL Query on Database and Store Results in file.
    with open(config.step3.sql_query_filepath, mode='r') as file:
        result = db.execute(file.read())
        with open(config.step3.sql_result_filepath, mode='w+') as outfile:
            outfile.write(result.fetchall().__str__())







