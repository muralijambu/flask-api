from flask import Flask,redirect,url_for,render_template,request,jsonify
import requests
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/course')
def courses():
    return '<h1>courses page</h1>'
@app.route('/admin')
def admin():
    return redirect(url_for('courses'))
@app.route('/<name>')
def name(name):
    return f'hello {name}'
@app.route('/fetch', methods=['GET'])
def fetch_data():
    name = request.args.get('name', 'Guest')  # Get 'name' from query parameters
    return f"Hello, {name}!"

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        user1 =request.form['usrname']
        return redirect(url_for('user', usr=user1))
    return render_template('login.html')
@app.route('/<usr>')
def user(usr):
    return f'hello {usr}'

if __name__=='__main__':
    app.run(debug=True)
