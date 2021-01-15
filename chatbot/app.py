from flask import Flask, request
import requests


app = Flask(__name__)

token = 'input your token'
method = ['/getMe','/sendMessage', '/getUpdates']
chain = '&'
uri = 'https://api.telegram.org/bot' 


@app.route('/')
def hello_world():
    return 'Hello! this is main'


@app.route('/telegram', methods=['POST'])
def telegram():
    # print(request.get_json())
    response = request.get_json()
    chat_id = response['message']['from']['id']
    text = response['message']['text']
    if text == 'hi':
        answer = 'hi!'
    else:
        answer = 'idk what you say...'
    # print(chat_id, text)
    requests.get(uri + token + f'sendMessage?chat_id={chat_id}&text={answer}')
    
    return '', 200


if __name__ == "__main__":
    app.run(debug=True)
