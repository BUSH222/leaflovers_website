from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return "this works"

@app.route('/based')
def based():
    return render_template('based.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
