from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, abort, session
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'h432hisdf5465akjafsdsd65asdwca'


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/home')
def home():
    return render_template('home.html', codes=session.keys())


@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        urls = {}
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        if request.form['code'] in urls.keys():
            flash(message='That short name has already been taken, Please select another name')
            return redirect(url_for('home'))
        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url': request.form['url']}
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save("C:\\Users\\Casper\Desktop\\flask-projects\\flask-url-project\\static\\user_files\\" + full_name)
            urls[request.form['code']] = {'file': full_name}
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
            session[request.form['code']] = True
        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('home'))


@app.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else:
                    return redirect(url_for('static', filename='user_files/' + urls[code]['file']))
    return abort(404)


# return render_template('error.html', code=code)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route('/api')
def session_api():
    return jsonify(session=list(session.keys()))


"""
@app.route('/not_found/<string:code>')
def not_found(code: str):
    return render_template('error.html', code=code)
"""

if __name__ == '__main__':
    app.run()
