
from flask import Flask,request,abort
import requests
from app.Config import *
import json

app=Flask(__name__)

@app.route('/webhook',methods=['POST','GET'])

def webhook():
    if request.method=='POST':
        payload =request.json
        Reply_token=payload['events'][0]['replyToken']
        message=payload['events'][0]['message']['text']
        Reply_text="คุณกำลังบอกว่า: "+message
        ReplyMessage(Reply_token,Reply_text,Channel_access_token)
        return request.json,200
    elif request.method=='GET':
        return "this is method GET!!!",200
    else:
        abort(400)


def ReplyMessage(Reply_token,TextMessage,Line_Acees_Token):
    LINE_API='https://api.line.me/v2/bot/message/reply/'
    
    Authorization='Bearer {}'.format(Line_Acees_Token)
    print(Authorization)
    headers={
        'Content-Type':'application/json; char=UTF-8',
        'Authorization':Authorization
    }

    data={
        "replyToken":Reply_token,
        "messages":[{
            "type":"text",
            "text":TextMessage
        }
        ]
    }
    data=json.dumps(data) # ทำเป็น json
    r=requests.post(LINE_API,headers=headers,data=data)
    return 200