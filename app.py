from flask import Flask, request, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=5000)