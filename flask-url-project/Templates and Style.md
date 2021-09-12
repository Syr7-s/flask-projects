### Templates and Style

#### Implementing session and cookies

* One of the great features of Flask is how easy it makes it to save information into a cookie so that when a user comes back to a website, we can have some data ready for them to see, so if you don't know how sessions or cookies work, essentially it's a way to store some information into a user's browser, it uses it as a key value store to say, hey I want to store this particular thing so that whenever I come back I can get that information. If you've ever used a keep me signed in button on a website, that utilizes cookies in order to make that happen, so in our particular Flask app here, if we want to use cookies

* ```python
  from flask import Flask
  ```

* Session, and session allows us to access those cookies, so we'll go ahead and add that up at the top. Now, the question is, how do we want to use cookies inside of our site. Well, I think it would be really neat for the user to know everything that they've uploaded before, and they can quickly see a list of all their different short codes, maybe they forgot to save it somewhere.

* we ultimately write that back into a JSON file, we also want to at this point, save that into a cookie, so to do that, we simply just type session, and then inside of the square brackets here, we provide the key that we want to save into the dictionary, so in this case, let's use the code that they've entered up to this point, so we can copy up from here,we really don't need to store a value associated with this code, so I'm going to set this equal to just a Boolean that is true for the time being, but you could think about some creative ways, like maybe you could save a timestamp of when the user saved this, so you could easily display that information to the user, but for our situation, we'll just simply set true so that we can get those codes saved into the cookies. Now that we've done that, that's where we want to save the session information.

* ```python
  session[request.form['code']] = True
  ```

* The question is, where are we going to display the session information, and I think it would be appropriate to show this on the homepage, so let's go ahead and look at the route that we have for our homepage. 

* So let's go ahead and besides saying that we want home.html, let's say that we also want to provide all the different codes that come as part of the cookies, so we're going to go ahead and say here, codes is equal to, and this is where we want to get access to that session, we're going to say session.keys, so when we say .keys that gets us just all the values that are there on sort of the left side of the dictionary, right, all the values that say true, that we're setting them equal too, we don't really care about those, that's why we're saying keys. So with this in place, that information is now being passed forward to our home.html.

* ```python
  @app.route('/home')
  def home():
      return render_template('home.html', codes=session.keys())
  ```

* ```html
  <div>
      {% if codes %}
          <h2>Codes you have created</h2>
          <ul>
              {% for code in codes %}
                  <a href="{{ url_for('redirect_to_url',code=code) }}">
                      <li>{{ code }}</li>
                  </a>
              {% endfor %}
          </ul>
      {% endif %}
  </div>
  ```



#### Creating JSON APIs

* You can imagine someone who created a whole lot of codes, could have a really long list of things, and this could be a great place to introduce an API into our project. And one of the awesome things about Flask is it makes it so easy to set up an API. So if we want to turn this feature that we just created into an API, it's as simple as this. 

* We just need to return back those session keys in a list. And make sure that it's in the JSON format. So, for this Flask has an awesome tool call jsonify.

* ```python
  from flask import Flask, jsonify
  ```

* if you ever need to create an API, you can get more complex than this, but that jsonify can again take dictionaries or lists and turn them into the appropriate values that you want to return.

* ```python
  @app.route('/api')
  def session_api():
      return jsonify(session=list(session.keys()))
  
  ```

#### Templates block and Base Templates

* then we want to create what's called a block. So if we go ahead and do our curly brackets with percentage signs, we can say block, and then we give some name to this block. So I'm going to call this the main block. Again, there's nothing special about that name, you could totally customize it, make it whatever you want, but whenever you start a block, you have to end that block. So I'm going to say end block at the end of this, no spaces or anything. So, with this in place, now I can take this main block and say I'm going to save this, and now come to my homepage for instance, and at the very top of my homepage, I want to extend that base template.

* ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Base Page</title>
  </head>
  <body>
      <h1>This is Base</h1>
      {% block main %}
      {% endblock %}
  </body>
  </htm
  ```

  