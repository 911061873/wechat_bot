from urllib.parse import quote
import random, requests, json, time, hashlib

appid = '2131862455'
appkey = ''
url = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'


def time_stamp():
    return str(int(time.time()))


def gen_random_str():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    a = ''
    for i in range(random.randint(1, 32)):
        a += random.choice(alphabet)
    return a


def getReqSign(params, appkey):
    params_sorted = sorted(params)
    a = ''
    for i in params_sorted:
        if params[i] != '':
            a += i + '=' + quote(params[i]) + '&'
    a += 'app_key=' + appkey
    m = hashlib.md5(a.encode()).hexdigest()
    return m.upper()


def chat(userid:str, question):
    data = {'app_id': appid, 'session': userid, 'question': question, 'time_stamp': time_stamp(),
            'nonce_str': gen_random_str(), 'sign': ''}
    data['sign'] = getReqSign(data, appkey)
    try:
        response = requests.post(url, data=data)
    except Exception as e:
        return e
    else:
        response = json.loads(response.text)
        if response['ret'] == 0:
            return response['data']['answer']
        elif response['ret'] == 16394:
            return random.choice(('我不知道说什么好了，再试一次吧！', '你触及到了我的知识盲区。'))
        else:
            return '哦哦出错了，错误代码{}'.format(str(response['ret']))
