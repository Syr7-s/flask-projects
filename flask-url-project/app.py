from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/your-url')
def your_url():
    return render_template('your_url.html', code=request.args['code'])


if __name__ == '__main__':
    app.run()
