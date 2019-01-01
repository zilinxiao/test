from flask import Flask
from flask import render_template,redirect,jsonify,json,request
from os import path,walk
from datetime import timedelta

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
#增加本行刷新静态资源，需要在浏览器开发模式下的setting选择disable cache,并且刷新网页。
#另一种处理方式是在前端设置请求头中设置无缓存。
userlist = [
    {
        'name': 'xzl',
        'age': 36
    },
    {
        'name': 'ddp',
        'age': 38
    }
]


@app.route('/')
def hello():
    return render_template('index.html', users=userlist)
    
@app.route('/users')
def users():
    return jsonify(userlist)
@app.route('/users/<string:name>',methods=['GET'])
def user(name):
    users = []
    for user in userlist:
        if user['name'] == name:
            users.append(user)
    return jsonify(users)
@app.route('/add',methods=['POST'])
def add_user():
    data = request.get_json()
    # print(data)
    name,age = data['name'],data['age']
    # print(name+','+age)
    userlist.append({'name':name,'age':age})
    return jsonify(userlist),200

@app.route('/update',methods=['PUT'])
def update_user():#可以是与delete类似的方法
    print('update')
    data = request.get_json()
    name,age = data['name'],data['age']
    for user in userlist:
        if user['name'] == name:
            user['age'] = age
    return jsonify(userlist),200

@app.route('/delete/<string:name>',methods=['DELETE'])
def delete_user(name):#可以是与updae类似的做法
    l = len(userlist)-1
    for i in range(l,-1,-1):
        if userlist[i]['name'] == name:
            userlist.pop(i)
    return jsonify(userlist), 200

if __name__ == '__main__':
    app.run(debug=False)
# debug=True,如果你启用了调试支持，服务器会在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器。
