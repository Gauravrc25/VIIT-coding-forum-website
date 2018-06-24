from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/static/<path:path>')
def send_statics(path):
    return send_from_directory('static', path)

if __name__=='__main__':
    app.run()
