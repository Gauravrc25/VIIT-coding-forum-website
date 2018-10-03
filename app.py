from flask import Flask , render_template, session, request, redirect, url_for
from controllers import auth_controller
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def authorization():
    email=request.form['email']
    password=request.form['password']
    #return email+' '+password
    auth_status, isAdmin, id = auth_controller.login(email, password)
    if(auth_status and isAdmin):
        session['isAdmin'] = True
        session['id'] = id
    return redirect(url_for('admin_render'))

@app.route('/admin', methods=['GET'])
def admin_render():
    try:
        if(session['isAdmin']):
            return render_template('admin.html')
        else:
            return "Unauthorized Access"
    except:
        return "Unauthorized Access"

@app.route('/static/<path:path>')
def send_statics(path):
    return send_from_directory('static', path)

if __name__=='__main__':
    app.secret_key = os.environ['SECRET_KEY']
    app.run(debug=True, host='0.0.0.0')
