import os
from __main__ import app
from flask import Flask, render_template, url_for, request, redirect

from image_predictor import predict

upload_folder = os.path.join('static', 'tmp')
app.config['UPLOAD'] = upload_folder

@app.route('/upload', methods=["GET","POST"])
def upload_file():
    if request.method == 'POST':
        file = request.files['img'] # 'img' is the id passed in input file form field
        filename = file.filename

        if not os.path.exists(app.config['UPLOAD']):
            os.makedirs(app.config['UPLOAD'])

        file.save(os.path.join(app.config['UPLOAD'], filename))
        print("Upload completed")
        return redirect('/prediction/{}'.format(filename))
    return redirect('/')


@app.route("/prediction/<filename>", methods=["GET","POST"])
def prediction(filename):
    digit_prediction = predict(filename)
    os.remove(os.path.join(app.config['UPLOAD'], filename)) # remove image as it no longer needed
    return render_template('index.html', digit_prediction=digit_prediction)