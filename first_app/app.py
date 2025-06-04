from flask import Flask, url_for, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/success/<name>')
def success(name):
    return 'Hello, %s!' % name


@app.route("/login", methods=['GET', 'POST'])
def login():
    # if get render login page
    if request.method == 'GET':
        return render_template("login.html")
    # if post get username and password and check if therer exist in the database
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # TODO  replace this with database request when have one
        if username == 'admin' and password == '0000':
            # if its okay log the user and redirect him to main page
            return redirect(url_for('success', name='admin'))
        else: # if not exist render login with error msg
            return render_template("login.html", errors=["please check your username and password"])

if __name__ == '__main__':
    app.run(debug=True)

