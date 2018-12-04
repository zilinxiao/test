from flask import Flask
from flask import render_template
app = Flask(__name__)

userlist =[{
            'name':'xzl',
            'age':36
            },
            {
                'name':'ddp',
                'age':38
            }
            ]


@app.route('/')
def hello():
    return render_template('index.html',users=userlist)



if __name__ == '__main__':
    app.run(debug=True)
#debug=True,如果你启用了调试支持，服务器会在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器。