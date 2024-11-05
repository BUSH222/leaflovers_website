from flask import Flask, render_template


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True


def get_number_template(name):
    filename = name + ".html"
    try:
        temp = open("templates/"+filename, 'r')
    except Exception:
        temp = open("templates/test.html", 'r')
    t = temp.name()
    temp.close()
    return t


@app.route('/')
def index():
    return "this works"


@app.route('/temp/<name>')
def id_temp(name):
    """func: allows template access via  name for fast review"""
    return render_template(get_number_template(str(name)))


@app.route('/based')
def based():
    return render_template('based.html')


@app.route('/horse')
def horse():
    return '🐎'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

