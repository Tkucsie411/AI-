from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

#載入.env檔案中的環境變數
load_dotenv()

app = Flask(__name__)
CORS(app) #允許前端請求後端API

#設定openAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

#建立網站首頁
@app.route('/')
def home(): #用來回應網站首頁連線的函式
    return render_template('index.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=5000)