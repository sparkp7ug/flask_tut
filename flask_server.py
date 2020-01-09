from flask import Flask, flash, redirect, render_template, request, session, abort, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/test")
def test():
    return render_template('test.html')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)