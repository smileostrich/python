import requests
import pprint

token = '1476408491:AAF4e5bVg-HRsqr1g67-jvmKzF6OgapHDzM'
method = ['/getMe','/sendMessage', '/getUpdates']
chain = '&'
uri = 'https://api.telegram.org/bot' 


def get_chatid():
    get_updates = uri + token + method[2]
    data = requests.get(get_updates).json()
    chat_id = str(data['result'][0]['message']['chat']['id'])
    return chat_id


def send_message(text):
    send_message = uri + token + method[1] + '?' + 'chat_id=' + get_chatid() + chain + 'text=' + text
    requests.get(send_message)
    # result = requests.get(send_message).json()
    

get_me = uri + token + method[0]
data = requests.get(get_me).json()

send_message('안녕~')
# pprint.pprint(data3)
print(get_chatid())