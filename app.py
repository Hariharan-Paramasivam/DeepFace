from flask import Flask

UPLOAD_FOLDER = r'./static/input_database/'

app = Flask(__name__,static_folder = r'./static/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024