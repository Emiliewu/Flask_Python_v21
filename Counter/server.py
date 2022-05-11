from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    if not session.get('visit'):
        session['visit'] = 1
    else:
        session['visit'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroysession():
    session.clear()
    return redirect('/')

@app.route('/addtwo')
def addtwo():
    session['visit'] += 1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)