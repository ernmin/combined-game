import pandas as pd
import json

def return_entries(requestedUser):
    with open('user_table.json', 'r') as file:
        user_table_list = json.load(file)
    # target_id = int(requestedUser)
    df = pd.DataFrame(user_table_list)
    df_filtered = df[df['ID'] == requestedUser]
    df_filtered_no_time = df_filtered[['ID', 'Photo', 'Question']]
    df_filtered_no_time = df_filtered_no_time.sort_values(by='Question')
    json_filtered = df_filtered_no_time.to_dict(orient='records')
    return json_filtered
    
def return_all_entries():
    with open('output.json', 'r') as file:
        photo_list = json.load(file)
    # target_id = int(requestedUser)
    df = pd.DataFrame(photo_list)
    df = df.rename(columns={'Upload your photo!': 'Photo', 'Which question is this photo for?': 'Question'})
    df['ID'] = '-'
    df = df[['ID', 'Photo', 'Question']]
    json_filtered = df.to_dict(orient='records')
    return json_filtered
