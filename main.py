from flask import Flask
from website import *

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True      
app.jinja_env.auto_reload = True

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3060', debug=False)
