from flask import Flask, render_template, request, redirect, session
import random # import the random module

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    if not session.get('result'):
        result = random.randint(1, 100) 		# random number between 1-100
        session['result'] = result
    if not session.get('guessnumber'):
        message = -1
    elif int(session['result']) == int(session['guessnumber']):
        message = 1
    elif int(session['result']) > int(session['guessnumber']):
        message = 2
    elif int(session['result']) < int(session['guessnumber']):
        message = 3
    return render_template('index.html', message = message )

@app.route('/guess', methods=['POST'])
def guess():
    session['guessnumber'] = request.form['guessnumber']
    return redirect('/')

@app.route('/clear')
def clearsession():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)