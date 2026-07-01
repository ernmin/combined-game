from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/rows", methods=['POST'])
def rows():
    client_data = request.get_json()
    user_to_find = client_data.get('requestedUser', '')
    return jsonify({
            "status": "success",
            # "serverPayload": local_file_data.get('result', 'No match found')
            "result": 'Test Success'
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