from flask import Flask, Response, render_template, request
import json
import pandas as pd
import dataframe_image as dfi

app = Flask(__name__)

##INIT
#Read persistent:
with open('persistence/oversikt.json') as file:
    content=file.read()
    if(content):
        print(content)
        total=json.loads(content)
    else:
        total={"total":[]}

##Methods
@app.route('/', methods=['GET'])
def get_home():
    return "Nothing to see here...."

@app.route('/oversikt', methods=['GET'])
def get_oversikt():
    return render_template('index.html')

@app.route('/oversiktjson', methods=['GET'])
def get_oversiktjson():
    jsonString=json.dumps(total,ensure_ascii=False)
    return (Response(jsonString,content_type="application/json; charset=utf-8"))

@app.route('/register',methods=['POST'])
def post_register():
    try:
        request_data=request.get_json()
        who=request_data['who']
        what=request_data['what']
        duplicate=False
        for i in total['total']:
            if(what in i['what']):
                print(i)
                duplicate=True
        if(not duplicate):
            total['total'].append({'who':who,'what':what})
            writeToJsonFile({'who':who,'what':what})
            makeImage()
            return '''{} added {}'''.format(who,what)
        else:
            return ''''Someone is already bringing: {}'''.format(what)
    except Exception as e:
        print("ERROR:",e)
        return '''Invalid input, submit valid JSON with attributes like: {"who":"yourname","what":"whatyouarebringing"}'''
def writeToJsonFile(new,file='persistence/oversikt.json'):
    with open('persistence/oversikt.json','r+')as file:
        json.dump(total,file,ensure_ascii=False)
    print(total)

def makeImage():
    dfi.export(pd.DataFrame.from_dict(total['total']),'static/images/output.png')


if __name__ == '__main__':
    makeImage()
    app.run(host="0.0.0.0", port=1705, debug=True)