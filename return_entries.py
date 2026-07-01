import pandas as pd
import json

def return_entries(requestedUser):
    with open('user_table.json', 'r') as file:
        user_table_list = json.load(file)
    # target_id = int(requestedUser)
    df = pd.DataFrame(user_table_list)
    df_filtered = df[df['ID'] == requestedUser]
    df_filtered_no_time = df_filtered[['ID', 'Link', 'Question']]
    json_filtered = df_filtered_no_time.to_dict(orient='records')
    return json_filtered
    
