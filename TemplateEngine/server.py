from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    print("in the hello function")
    return render_template("index.html", phrase="hello", times=5)

@app.route("/<name>")
def hello_person(name):
    print("*"*80)
    print("in hello_person function")
    print(name)
    return f"Hello {name}!"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.