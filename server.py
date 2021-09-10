from flask import Flask, render_template,  request, redirect, session

app = Flask(__name__)
app.secret_key = 'nana nana Batman!' # set a secret key for security purposes

@app.route('/')
def index():
    print(session)
    return render_template("index.html")

@app.route('/users', methods=['POST']) # Never render a template on a POST request.
def create_user():
    print("Got Post Info")
    print(request.form)
    print(request.form['name'])
    print(request.form['loc'])

    name = request.form['name']
    loc = request.form['loc']
    lang = request.form['lang']
    comment = request.form['comment']

    session['username'] = name
    session['location'] = loc
    session['language'] = lang
    session['comments'] = comment

    return redirect('/result')
   
@app.route('/result')
def show_user():
    print("Show the User Info From the Form")
    print(request.form)
    print(session)
    return render_template('result.html', username = session['username'], location = session['location'], language = session['language'], comments = session['comments'] )
    

@app.route('/clear') # futur log out wipe session
def clear_session():
    session.clear()
    return redirect('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.