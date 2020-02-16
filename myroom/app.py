from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    return render_template('stars.html')


if __name__ == '__main__':
    app.run(debug=True)
