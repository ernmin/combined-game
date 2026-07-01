from flask import Flask, request, jsonify
from user_table import transform_and_process_row
from return_entries import return_entries
import pandas as pd

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_sheets_update():
    response_headers = {"ngrok-skip-browser-warning": "true"}
    
    payload = request.json
    row_index = payload.get('approvedRowIndex')
    headers = payload.get('headers', [])
    row_data = payload.get('rowData', [])
    cell_value = payload.get('cellValue')
    
    if not row_data:
        return jsonify({"status": "no data received"}), 400, response_headers

    # Method A: Convert to a clean single-row Pandas DataFrame
    # Wrap row_data in an outer list so Pandas reads it as a single row matrix [[val1, val2...]]
    df = pd.DataFrame([row_data], columns=headers)
    
    print(f"\n--- [ALERT] Row {row_index} Has Been Approved! ---")
    print(df)
    print("----------------------------------------------------\n")
    
    transform_and_process_row(row_data, headers, row_index, cell_value)
    
    # Example: Accessing a specific column from the approved row
    # if "Email" in df.columns:
    #     user_email = df["Email"].iloc[0]
    #     print(f"Triggering workflow for user: {user_email}")
    
    # ------------------------------------------------------------------
    # Place your single-row validation or processing logic here
    # ------------------------------------------------------------------

    return jsonify({"status": "success", "processed_row": row_index}), 200, response_headers

@app.route('/entries', methods=['GET']) # SHOULD THIS BE GET OR POST?
def get_entries():
    response_headers = {"ngrok-skip-browser-warning": "true"}
    received_var = request.args.get('requestedUser')
    print(f"Heroku sent me this variable: {received_var}")

    json_filtered_rows = return_entries(received_var)
    print(type(json_filtered_rows))
    print(json_filtered_rows)
    return json_filtered_rows

    # if request.method == 'GET':
    # return received_var


if __name__ == '__main__':
    app.run(port=5000, debug=True)