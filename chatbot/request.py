import requests


token = '1476408491:AAF4e5bVg-HRsqr1g67-jvmKzF6OgapHDzM'
uri = 'https://api.telegram.org/bot' 
ngrok_uri = 'https://ilminmoon.pythonanywhere.com/'

set_uri = uri + token + '/setWebhook?url=' + ngrok_uri + 'telegram'
print(requests.get(set_uri).json())
# print(set_uri)