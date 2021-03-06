from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
