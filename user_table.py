import pandas as pd
import numpy as np
import json

def transform_and_process_row(row_data, headers, row_index):
    """
    This function accepts the raw data from server.py,
    transforms it into a usable structure, and processes it.
    """
    print(f"\n⚙️ [Processor] Starting data transformation for Sheet Row {row_index}...")
    
    # 1. Convert the single row lists into a Pandas DataFrame
    df = pd.DataFrame([row_data], columns=headers)
    df.to_json('output.json', orient='records', indent=4)
    print(df)
    df = df.rename(columns={'Upload your photo!': 'Link', 'Which question is this photo for?': 'Question'})
    df.drop(columns=['Approved'], inplace=True)
    collapsed_df = pd.melt(df, id_vars=["Timestamp", "Link", "Question"], value_vars=[f"Person {i} ID" for i in range(1,6)], value_name="ID",).drop(columns=['variable'])
    collapsed_df["ID"] = (collapsed_df["ID"].astype(str).str.strip().replace(["", "None", "NaN", "nan"], np.nan))
    collapsed_df = collapsed_df.dropna(subset=["ID"])
    collapsed_df = collapsed_df[['ID', 'Link', 'Question', 'Timestamp']]

    with open('user_table.json', 'r') as file:
        user_table_list = json.load(file)
    
    user_table_new = collapsed_df.to_dict(orient='records')
    # print(user_table_new)
    user_table_join = user_table_list + user_table_new
    with open('user_table.json', 'w') as file:
        json.dump(user_table_join, file, indent=4)
    # collapsed_df.to_json('./user_table.json', orient='records', indent=4)
    #CHANGE TO APPEND TO THE USER_TABLE INSTEAD
    

    
    # 4. Trigger your actual core business logic here
    # (e.g., saving to a database, triggering a local script, sending an email, etc.)
    # execute_business_logic(usable_record)

def execute_business_logic(cleaned_data):
    """
    Put whatever your python script is supposed to 'check' or do with the data here.
    """
    print("🚀 [Processor] Running analysis workflow on the cleaned record...")
    
    #ADD ROW TO JSON FILE
    #FROM PANDAS DF TO LIST OF DICTS

    pass


#WHAT JSON FILE DOES TABLEAU USE TO POPULATE IT