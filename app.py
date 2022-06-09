import os
from flask import Flask,  flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from analysis import analyze_data
from utils import unzip, run_shell

app = Flask(__name__)
 
UPLOAD_FOLDER = 'assets/'
 
app.secret_key = "daredata"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['tar', 'gz', 'zip'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No file selected for uploading')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename("file.zip")
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # unzip file
        unzip()

        # run shell script
        run_shell()

        result = analyze_data()

        flash(result)
        return render_template('index.html', filename=filename)

    else:
        flash('Allowed file types are - tar, gz, zip')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

 
if __name__ == '__main__':
    app.run(debug=True)