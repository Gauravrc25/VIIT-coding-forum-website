from flask import Flask , render_template

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

@app.route('/static/<path:path>')
def send_statics(path):
    return send_from_directory('static', path)

if __name__=='__main__':
    app.run()
