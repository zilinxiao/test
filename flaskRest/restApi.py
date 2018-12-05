from flask import Flask
from flask import render_template,request,jsonify,json

app = Flask(__name__)

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

@app.route('/add',methods=['POST'])
def add_user():
    name,age = request.json['name'],request.json['age']
    userlist.append({'name':name,'age':age})
    return jsonify(userlist)

@app.route('/update',methods=['PUT'])
def update_user(user):
    name,age = request.json['name'],request.json['age']
    for user in userlist:
        if user['name'] == name:
            user['age'] = age
    return jsonify(userlist)

@app.route('/delete',methods=['DELETE'])
def delete_user(name):

    for user in userlist.reverse():
        if user['name'] == name:
            userlist.pop(user)
    return jsonify(userlist)

if __name__ == '__main__':
    app.run(debug=True)
# debug=True,如果你启用了调试支持，服务器会在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器。
