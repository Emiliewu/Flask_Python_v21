from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    session['student_name'] = request.form['student_name'] if request.form.get('student_name') else 'name not submitted'
    session['location'] = request.form['location'] if request.form.get('location') else 'no location'
    languages = request.form.getlist('language') if request.form.getlist('language') else ['no idea']
    print("******************************")
    session['languages'] = languages
    session['initial'] = request.form['initial'] if request.form.get('initial') else 'NA'
    session['comments'] = request.form['comments'] if request.form['comments'] else 'Nothing'

    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html")

@app.route('/clear_session')
def clearsession():
    session.clear()
    return redirect('/')
  
if __name__=="__main__":
    app.run(debug=True)