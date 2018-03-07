import requests
from flask import Flask,request
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

def send(message):
    url="https://hooks.slack.com/services/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"
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json"
        }
    s='{\"text\":'+'\"'+message+'\"}'

    response = requests.request("POST", url, data=s, headers=headers)

send('this is slack')

class Read(Resource):
    def post(self):
        data=request.get_json()
        print data
        val= request.args.get('key1', default ='*', type = str)
        print val
        send('i have read you')
        return {"text":"fine"}

    
api.add_resource(Read,'/')
app.run(port=800)
