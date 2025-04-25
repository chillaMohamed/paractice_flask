from flask import Flask, url_for, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/user/<name>/<int:age>/<slug>', )
def user(name, age, slug):
    return 'hello, %s!, age=%s, slug=%s' % (name, age, slug)

@app.route('/success/<name>')
def success(name):
    return 'Hello, %s!' % name


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == '0000':
            return redirect(url_for('success', name='admin'))
        else:
            return render_template("login.html", errors=["please check your username and password"])

if __name__ == '__main__':
    app.run(debug=True)






