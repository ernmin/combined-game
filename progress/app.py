from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/rows", methods=['POST'])
def rows():
    site_data = request.get_json()
    user_to_find = site_data.get('requestedUser', '') # the second argument is the fallback

    ngrok_url = "https://stereo-estrogen-valid.ngrok-free.dev/entries"
    payload = site_data
    try:
        response = requests.get(ngrok_url, params=payload, timeout=5)
        if response.status_code == 200:
            print("Success!")
            print(response.json())

    except requests.exceptions.RequestException as error:
        print(f"Error: {error}")


    return jsonify({
            "status": "success",
            # "serverPayload": local_file_data.get('result', 'No match found')
            "result": user_to_find
        })
#     url = 'https://stereo-estrogen-valid.ngrok-free.dev/get_entries'


# app.py and progress file will be deployed on heroku
# Once server and ngrok url is live, a user can access the site on heroku to query my server.
# Since the JSON file is being updated on my computer (server), it will just return the latest information to the heroku deployed app

# IN THIS APP, AFTER RECEIVING THE FORM DATA, IT SHOULD SEND IT TO server.py but at the url https://stereo-estrogen-valid.ngrok-free.dev/get_entries
# This will be a different app.route in server.py
# There will be a function that executes from 
    
if __name__ == "__main__":
    app.run(debug=True)