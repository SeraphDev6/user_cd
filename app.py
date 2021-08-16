from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
from user import User
@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html',users=users)

@app.route('/user_form')
def user_form():
    return render_template('user_form.html')

@app.route('/submit_user', methods=['POST'])
def submit_user():
    data={
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)