### Flask
* This templating functionality all comes thanks to Jinja. Now, Jinja is this awesome template engine which is created by the same people that have created Flask. However, Jinja is used in a lot of other projects than just Flask, it's pretty popular, and there's so many different options and functionality that you can use with Jinja.

* in Jinja, you just simply do two curly brackets, then type out the name of your variable, which in this case is 'name', and then two ending curly brackets. 

*  in Jinja, you just simply do two curly brackets, then type out the name of your variable, which in this case is 'name', and then two ending curly brackets. 

* ```html
  <h2>{{name}}</h2>
  ```

  ```python
  @app.route('/home')
  def home():
      return render_template('home.html', name='Jesus')
  ```

* request.args, and inside of this args, this args is a dictionary for different parameters that could be passed in as get parameters. So I'm going to go ahead and provide inside of here, code, which is the name. 

  ```python
  @app.route('/your-url')
  def your_url():
      return render_template('your_url.html', code=request.args['code'])
  
  ```

* . And instead of saying .args we're going to change this to .form. When we're working with a POST request to get any parameter information, we have to use a .form instead of a .args

  ```python
  @app.route('/your-url', methods=['GET','POST'])
  def your_url():
      if request.method == 'POST':
          return render_template('your_url.html', code=request.form['code']) #code=request.args['code']
      else:
          return jsonify(message='This is not valid ')
  
  ```

  

