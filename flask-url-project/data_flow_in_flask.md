### Data Flow in Flask

* And the fact that it's still up in the URL is a little bit tough for them. So this is a good situation of rather than just rendering the home template, we actually want to redirect to the home page, which will not only show the home page material, but also change the URL to show that it's at the home page.

  ```python
  @app.route('/your-url', methods=['GET', 'POST'])
  def your_url():
      if request.method == 'POST':
          return render_template('your_url.html', code=request.form['code'])
      else:
          return render_template('home.html')
  
  ```

* We're going to add another comma and we're going to import the redirect, and with this we're going to now say rather than rendering a template, we want to redirect, and it's looking for a URL that it can redirect to. So if we go ahead and inside of a string just put a slash, which is the same path that we have up here for our route, it'll redirect to the home page.

  ```python
  @app.route('/your-url', methods=['GET', 'POST'])
  def your_url():
      if request.method == 'POST':
          return render_template('your_url.html', code=request.form['code'])
      else:
          return redirect('/home')
  ```

* there's a little bit more that we can do here. If we go back and look at our code, we sort of have manually typed out that we want to redirect to the home page with just that slash when really it's just that we want this home function. The home page may change directions here if we were to actually type out something like slash home or whatnot.

*  So when we do our redirect, we can use a new function called url_for which creates the URL for us based on the function name.

  ```python
  @app.route('/your-url', methods=['GET', 'POST'])
  def your_url():
      if request.method == 'POST':
          return render_template('your_url.html', code=request.form['code'])
      else:
          return redirect(url_for('home'))
  
  ```

* Saving to Json file.

  * The purpose of our URL shortener, is for someone to enter in a website URL, as well as it's nickname or short name for that URL, so they can quickly access it in the future. We need some way to save this information, and Flask is not a great option when it comes to saving data with a database. You have to do all the work yourself. You often end up writing SQL statements. But for this situation, where we just simply have to name what a website URL is, and then what the nickname is for it, an instance like a JSON file would be perfect for saving our data.

  *  So this is going to be the situation when someone is doing a post request. So we'll go ahead and just make a new line here. And the first thing that we want to do is create a dictionary that can store the information. If you sort of think abstractly about what we're doing, we want to save the code that the user has passed in. That short name as the key, and then the value will be the URL that they ultimately want to get to. Now down the road with our URL shortener, we're going to be accepting files. So we have to make sure that we signify weather it's going to be a URL or a file. But just think of it very top level, as a dictionary, where we have the codes as Ps, and then those URL as values. So we'll go ahead and make a variable called URLs that will simply just be an empty dictionary.

  *  if we have any duplicates written inside of this file. In fact, if we go back to our homepage, and we put in some sort of new website, and we use the same short name, and we go back to our code editor, we can see that it's overwritten the data here inside of or JSON dictionary. So we have to have some sort of check to see if the code already exists. 

  * ```python
    @app.route('/your-url', methods=['GET', 'POST'])
    def your_url():
        if request.method == 'POST':
            urls = {} #empty dictionary
            urls[request.form['code']] = {'url': request.form['url']}
            with open('urls.json', 'w') as url_file:
                json.dump(urls, url_file)
            return render_template('your_url.html', code=request.form['code'])
        else:
            return redirect(url_for('home'))
    
    ```

    ```json
    {"google": {"url": "http://www.google.com"}}
    ```

  * To prevent users from overwriting existing data inside of our urls.json, we need to do a check inside of our code to say, hey if this key already exists and has a url, don't update it.After we create our url's dictionary, let's check and see if we already have a urls.json file.

  * We have an existing key go so we'll move back to our homepage. We will try a new url for the name of go. Hit shorten and look at that. It keeps us here on the homepage which tells us it detected that.

    ```python
    @app.route('/your-url', methods=['GET', 'POST'])
    def your_url():
        if request.method == 'POST':
            urls = {}
            if os.path.exists('urls.json'):
                with open('urls.json') as urls_file:
                    urls = json.load(urls_file)
            if request.form['code'] in urls.keys():
                return redirect(url_for('home'))
            urls[request.form['code']] = {'url': request.form['url']}
            with open('urls.json', 'w') as url_file:
                json.dump(urls, url_file)
            return render_template('your_url.html', code=request.form['code'])
        else:
            return redirect(url_for('home'))
    
    
    ```

  * So if someone uses a short name that's already been taken, like in this case with go and they hit the shorten button, it still keeps them on the homepage and clears the data. You need to pick a new short name for your URL. So this is a great chance to introduce flash inside of flask. It's a great way to display messages or information to your users as you move on to new web pages.  And inside of this flash function, we provide a string that we want to display to the user.

    ```python
    @app.route('/your-url', methods=['GET', 'POST'])
    def your_url():
        if request.method == 'POST':
            urls = {}
            if os.path.exists('urls.json'):
                with open('urls.json') as urls_file:
                    urls = json.load(urls_file)
            if request.form['code'] in urls.keys():
                flash(message='That short name has already been taken,Please select another name')
                return redirect(url_for('home'))
            urls[request.form['code']] = {'url': request.form['url']}
            with open('urls.json', 'w') as url_file:
                json.dump(urls, url_file)
            return render_template('your_url.html', code=request.form['code'])
        else:
            return redirect(url_for('home'))
    
    ```

  * We have to check and see if we have any flashed messages. So we're going to go ahead and do a curly bracket and a percentage sign inside of Jinja. This is when you run any kind of code. It's not technically Python code, it's jinjas own way of writing code. But inside of here we're going to be doing a for loop. And we're going to say for and we want message in and we want to do get_flashed_messages. Now this is a special name inside of the template that we'll check for to see if there are any messages. If they are they will be stored inside of this variable. Now the way to end this for loop is we've got to do a curly bracket with the two percentage signs in it and at the bottom of this, we're going to say endfor no spaces in that. But the code in between is going to be looped for for every message that we have inside of that variable. So here, we can display our message by simply doing our two curly brackets and same message, which is the name that we provided up on line three. And to see that the user can really notice this, let's go ahead and wrap it inside of an h2 tag. So we'll do an opening h2 and an ending h2. Now, just before we go ahead and move on, because we're using message flashing

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>FLASK - URL Shortener</title>
    </head>
    <body style="background-color: darkkhaki">
    <h1 style="text-align: center">FLASK - URL Shortener.</h1>
    <div>
        {% for message in get_flashed_messages() %}
            <h2>{{ message }}</h2>
        {% endfor %}
        <form action="/your-url" style="text-align: center;" method="POST">
            <label for="url">Web Site Url : </label>
            <input type="url" name="url" value="" required>
            <br>
            <br>
            <label for="code">Short Name :  </label>
            <input type="text" name="code" value="" required>
            <br>
            <br>
            <input type="submit" value="Shorten">
        </form>
    </div>
    </body>
    </html
    ```

  * After we create our app variable, we also need to say app.secret_key. This allows us to securely send messages back and forth from the user to make sure that those trying to snooping on the connection cannot see this information. So we need to provide some sort of random string for the time being, just because we're in development you can just type some gibberish. But when it comes to production, you would want to find a very random key and make it long so that no one could guess the secret key. 

    ```python
    app.secret_key = 'h432hisdf5465akjafsdsd65asdwca'
    ```

  * . So in the top form tag here on our second form, we're going to add an extra field here called enctype, and make sure that it's set to multi-part slash form data. Essentially what this says is that this form is allowed to have file uploads.

  *  So the first step for us is when we want to save this, is we've got to decide whether the user has sent us a URL or whether they've sent us a file. Because in either situation, in either form, it's going to the same your URL function. So what we're going to do is after we've checked to make sure that the key doesn't already exist, because whether it's a file or URL, we still want to make that check, now we can check and see, okay, is this the file or is it a URL? So for this check we're going to say if URL, the string, we want to see if this is inside the form keys here. So we're going to say if URL in request dot form dot keys, this simply goes through all the keys inside of the form dictionary and says, "Hey, is there something called a URL?". So if there is something, well then we want to take the following line of code and run that. And that's simply to say "Hey, inside of our URL's dictionary, "add the following URL for this code key". Now the else part of this is that there is a file that's trying to be uploaded. So in this case we first have to one, save the file, and then second, save that into the URL's dictionary. So first let's go ahead and grab the file from the form and put it inside a temporary variable. So we're going to say F, which is short for file, is equal to request dot files, and inside of here we'll just simply provide the key file, remember we did that lower case file name there. Now in order to save our file, we have to pick a name in order to save it to. And the issue that we have here is that users might be uploading files with the exact same name, and we've got to make sure that we don't overwrite information similarly to like we've found with the URLs. So one way to fix this is to say, we know that the codes are going to be unique, so if we take the code that the user has provided us and the file name that they've given us, we can combine those two things and make sure that these won't collide with each other. So we'll go ahead and create a new variable here called full underscore name, this is where we're going to save that file name. And we're going to say this is equal to the request dot form and inside of there we want to go ahead and grab whatever the code is that they provided. And in addition to this, we want to take our file and get it's file name. So we'll say dot file name on that. And one issue that we're going to have here is that this file name may come with some bad intentioned people, right? They may say I'm going to try and delete something on this server's system, or I want to install this script, if we can make sure that none of that happens, we'll be a lot more confident in the uploads that we receive. So, we need to bring a new tool into our project. If we scroll up to the top, now stay with me, this is a little bit of a interesting word here, we're going to say from werkzeug, as best as I can pronounce this, but W-E-R-K-Z-E-U-G, and then we're going to say, dot utils, import, and we want to go ahead and import something called secure underscore file name. Now this werkzeug is something that comes from the same people that have created Flask that has a lot of great different tools inside of it. But this one in particular allows us to make sure any file that's uploaded we can check and make sure that it's safe to save. And we get this werkzeug package because it is a dependency in Flask, so we don't have to go ahead and manually bring that in, which is nice for us. So now that we have that secure file function, we can come now and wrap up this F dot file name with a secure file. We'll go ahead and wrap that, just like that. We'll make sure that we've got secure file name so that, and I forgot that up at the top, secure file name, there we go. And now that we have this in place, this will be the full name that we want to save it to, but we have to decide where it is that we're going to save this file. So if we do F dot save, we've got to provide a path where we want to save our project so if we come back over to our terminal, let's go ahead and stop it with a control C, do PWD to figure out exactly where you are, and you can see here's my path, yours is going to be different from mine. But copy whatever path you have, come back, paste it into a string, add an ending slash on the end of that string, and then we're going to add to this whatever full underscore name is. So it's saying "Hey go save to "this specific spot on our computer, "with this specific name". Now once we've done that, that'll save the file, but then we need to update our URLs dot json with this new information. So we'll go ahead and copy that line, and we'll paste it down below. We're going to keep all of this the same on the left, but here instead of URL, we'll change this to file. And then instead of request dot form for URL, we simply just want to take whatever the full name is of that file. So we'll take full underscore name and then we can go ahead and save this. So now with this in place, let's go ahead and test out our website. So we'll reload our home page. Oh, and the reason we're not getting anything is we forgot to restart our server. So let's move back to our terminal, do a Flask run, get that started again. Now reload our home page, and we need to choose some sort of file. So here inside of the Exercise files, I have this picture of a house, the situation I'm thinking is someone's thinking of buying this house at 67 Cherry Lane and they want to show it off to their friends. You can upload any picture that you want, video, json file, whatever it is, or you can do the same as me. But go ahead and pick some file, give it a short name, I'm going to choose image in this situation, and I'm going to go ahead and hit shorten, and now once I've done that you can see, it successfully showed us what code we provided, and if we go back to our project, look what has been uploaded. withcer292030_screenshots_20200814195705_1.jpg. So it combined those two things, saved it into our directory, and if we look at our URLs dot json, we now have a new key, house, that is specified as a file with the file name attached to it.

    ```python
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
                f.save("C:\\Users\\Casper\Desktop\\flask-projects\\flask-url-project\\"+full_name)
                urls[request.form['code']] = {'file': full_name}
            #urls[request.form['code']] = {'url': request.form['url']}
            with open('urls.json', 'w') as url_file:
                json.dump(urls, url_file)
            return render_template('your_url.html', code=request.form['code'])
        else:
            return redirect(url_for('home'))
    ```

* We have to have the ability so that when someone visits our website slash house, that we display the following file or if they visit our site slash go, it will redirect them to yahoo dot com. So, how do we do this? Well, we need a new route to find these situations when someone has specified these unique urls.  There's millions of different combinations that could come through for the code and how do we account for these situations? Well, inside of our route, we can use something called a variable route to say, hey, look for a string and then whatever that string is it can be passed into the function and then used to determine what to give back to the user.

  ```python
  @app.route('/<string:code>')
  def redirect_to_url(code):
      if os.path.exists('urls.json'):
          with open('urls.json') as urls_file:
              urls = json.load(urls_file)
              if code in urls.keys():
                  if 'url' in urls[code].keys():
                      return redirect(urls[code]['url'])
  ```

* We have the functionality so that if someone provides a short name, they can get back a URL, if that's what they provided. Now, if they provided a file, well, we don't have that functionality yet. And the reason is we don't know how to serve static files. But let's talk about how we can do that in Flask. So there's a couple of steps here. The first one is we have to create a directory in our project called static.Static, this is a special name that Flask is going to look for whenever you have static files, and any static files that you have, they might be things like JavaScript from your website, you might have CSS, maybe a logo for your website, those are all going to go inside of the static folder. 

*  The next step for us is to say when someone's trying to retrieve that file, if we know that it's a URL, we'll return that URL, but the else part of that situation is to say, you know, they're actually looking for a file. So in this case, we need to get the URL for that static file. And this is how you serve static files in Flask. We say URL_for, and then we first provide a string static, that says I'm looking for a static file. And then we have to specify the file name. So I'm going to say filename, and I'm going to set this equal to first, the directory that they're under, which is user files. So I'm going to do a string that says user_files with a slash. And then I'm going to add on to this, also the file name, which is going to come from the dictionary. So I'm going to copy this and paste it and instead of providing URL for the key, I'm going to do file for that, and we can tell if we go to our urls.json with a URL, we have the key URL there, but for a file.

* , this is just a URL. Remember, we need to redirect and return that redirect back to the user, so we're going to say return a redirect to the following URL. Let's go ahead and wrap that up in parentheses, and we'll now save this

  ```python
  @app.route('/<string:code>')
  def redirect_to_url(code):
      if os.path.exists('urls.json'):
          with open('urls.json') as urls_file:
              urls = json.load(urls_file)
              if code in urls.keys():
                  if 'url' in urls[code].keys():
                      return redirect(urls[code]['url'])
                  else:
                      return redirect(url_for('static', filename='user_files' + urls[code]['file']))
  ```

*  So our URL Shortener is able to give back files or URLs for names that people have submitted. Well, let's say that someone submits a name that we don't have something for. I'm just going to type some gibberish here. If I hit Enter on this, well we get a really nasty looking error, which really isn't something we should be sending back to the user. We want to have a more clean page that says "This was not found," or something like that, and specifically for this case, we want to use something called a 404 page. You may have seen that on other websites. 404 means we couldn't find what it is that you were looking for. So if we go ahead and move back to our app.pie, in order to do this we need to bring in some new code from Flask, so we're going to add more to our import line here. We are going to add "abort", and this abort allows us to, when something goes wrong, send a special error message depending on what it is. Now there's more than 404 errors. You can read all about the different HTTP error codes if you're interested, but specifically.

* Redirect error page.(If key is not find, User will redirect to error page.)

  ```python
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
              else:
                  return redirect(url_for('not_found', code=code))
  
  # return render_template('error.html', code=code)
  
  
  @app.route('/not_found/<string:code>')
  def not_found(code: str):
      return render_template('error.html', code=code)
  
  ```

* The only last thing that I would like to change here is that again, we've talked about this before, is that what if the routes for our different resources change? It's not great to just put a slash here to say go to the home page. We'd rather say, let's get the URL for the home page, and ultimately redirect them there. So we can do this inside of Jinja. Instead of doing the slash, we're going to do our curly brackets, and inside of there we're going to say "url" underscore "for", and then inside of the parentheses we're going to add the string home. 

  ```python
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
  ```

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Page Not Found</title>
  </head>
  <body style="background-color: darkkhaki; text-align: center">
      <h1>Page Not Found.</h1>
      <p>We could not find what you are looking for. Come visit our homepage. :) </p>
     <!-- <p><a href="/home">Home</a></p>-->
      <p><a href="{{ url_for('home') }}">Home</a></p>
  </body>
  </html>
  ```

  