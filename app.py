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

@app.route('/show/<id>/')
def show(id):
    user = User.get_by_id({"id":id})
    return render_template("show_one.html",user=user)

@app.route('/edit/<id>/')
def edit(id):
    user = User.get_by_id({"id":id})
    return render_template("edit_user.html",user=user)

@app.route('/edit_user', methods=['POST'])
def method_name():
    data={
        'id':request.form['id'],
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }
    User.update(data)
    return redirect('/')

@app.route('/delete/<id>/')
def confirm_delete(id):
    user = User.get_by_id({"id":id})
    return render_template('confirm_delete.html',user=user)

@app.route('/delete_user', methods=['POST'])
def delete():
    User.delete({'id':request.form['user']})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)