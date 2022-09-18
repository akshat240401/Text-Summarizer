# from crypt import methods
from distutils.log import debug
from flask import Flask, render_template, request
from text_summary import summarizer
from text_summary import summarizerhi

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize',methods=['GET','POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        summary,original_txt,len_orig_txt,len_summary = summarizer(rawtext) or summarizerhi(rawtext)
    return render_template('summary.html',summary=summary,original_txt=original_txt,len_orig_txt=len_orig_txt,len_summary=len_summary)

if __name__ == "__main__":
    app.run(debug=True)