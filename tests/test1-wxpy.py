from wxpy import *
import requests
import json

bot = Bot(cache_path=True)

def auto_replay(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "1134a68111b643948c49e2d68827fcb7"
    payload = {'key': api_key,
               'info': text,
               'userid': 'rebot'}
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return result['text']

def auto_ai(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "1134a68111b643948c49e2d68827fcb7"
    payload = {'key': api_key,
               'info': text,
               'userid': 'rebot'}
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    return result['text']

friend = bot.friends().search('王汝辉')[0]


@bot.register()
def my_msg(msg):
    print('[接收]' +str(msg))
    if msg.type!='Text':
        ret='你给我看了什么！'
    else:
        ret=auto_ai(msg.text)
    print('[发送]' + str(ret))
    return ret

embed()