from flask import Flask, render_template, redirect, url_for, request
import json
import os

app = Flask(__name__)


PEOPLE_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

words = []
defenitions = []
terms = [] 

@app.route('/', methods=['GET'])
def main():
    data = json.load(open("data.json"))  
    return render_template('main.html', words=words, defenitions = defenitions, data = data)

@app.route('/search_word', methods=['POST'])
def add_word():
    text = request.form['text']  
    data = json.load(open("data.json"))
    defenition = ""
    defenitions.clear()
    if text in data:
        defenition =  data[text][0]
    else:
        defenition = "Такого термина нет!"
    words.append(text)
    defenitions.append(defenition)
    return redirect(url_for('main'))

@app.route('/graph', methods=['GET','POST'])
def mid_map():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'graph.png')
    return render_template("graph.html", user_image = full_filename)

@app.route('/clear', methods=['GET'])
def clear_history():
    words.clear()
    return redirect(url_for('main'))
  
app.run(host='0.0.0.0', port=81)
