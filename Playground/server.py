from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def homepage():
    print("in the homepage function")
    return render_template("index.html", times=3, color="azure")

@app.route("/play/<int:num>")
def play_num(num):
    print("in play_num function")
    print(num)
    return render_template("index.html", times=num, color="azure")

@app.route("/play/<int:num>/<color>")
def play_color(num, color):
    print("in play_color function")
    return render_template("index.html", times=num, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.