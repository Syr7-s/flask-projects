from flask import Flask

app = Flask(__name__)

host = "localhost"
port = 8080


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login/<string:name>/<int:age>/')
def login(name, age):
    return 'hello ' + name + ', is ' + str(age) + ' years old ? Really'


if __name__ == '__main__':
    app.run()
# use_reloader = True
