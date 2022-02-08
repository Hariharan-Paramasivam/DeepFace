

from origin import predict,local_path
import os
from app import app
from flask import request,render_template
import time
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


ALLOWED_EXTENSIONS = set(['png','jpg','jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/",methods=['POST','GET'])
def home():
    return render_template('index.html')

@app.route("/result",methods=['POST','GET'])
def result():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
            print(filename)      
            print(file_path)
            file.save(file_path)
        #time taken to run
            t = time.process_time()
            result = predict(file_path)
            print(result)
            elapsed_time = time.process_time() - t
            if result == 0:
                file.save(os.path.join(local_path, secure_filename(file.name)))
    return render_template('result.html',res = result , time = elapsed_time,user_image = file_path)


if __name__ == "__main__":
    app.run()
