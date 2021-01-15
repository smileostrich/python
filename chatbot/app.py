from flask import Flask, request
import requests


app = Flask(__name__)

token = '1476408491:AAF4e5bVg-HRsqr1g67-jvmKzF6OgapHDzM/'
method = ['/getMe','/sendMessage', '/getUpdates']
chain = '&'
uri = 'https://api.telegram.org/bot' 


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test')
def link_test():
    return 'hello test!'


@app.route('/telegram', methods=['POST'])
def telegram():
    # print(request.get_json())
    response = request.get_json()
    chat_id = response['message']['from']['id']
    text = response['message']['text']
    if text == '안녕':
        answer = '안녕하세요!'
    else:
        answer = '무슨 말씀이신지...'
    # print(chat_id, text)
    requests.get(uri + token + f'sendMessage?chat_id={chat_id}&text={answer}')
    
    return '', 200


if __name__ == "__main__":
    app.run(debug=True)