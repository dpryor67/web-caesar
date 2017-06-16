from flask import flask
app = Flask(__name__)
app.config['DEBUG'] = True

form = """

"""


@app.route("/")
def index():
    return "Hello World"

app.run()