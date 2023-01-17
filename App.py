from flask import Flask, render_template,request
from pdf2docx import parse

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/pdf', methods=['POST'])
def predict():
    if request.method=="POST":
        pdf=request.form.get('pdf')
        filename=request.form.get('filename')
        parse(pdf, filename, start=0, end=None)

    return "File Succesfull Convert"

        


if __name__ == '__main__':
   app.run()