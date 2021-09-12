from flask import Flask
from flask_cors import CORS
import json
from db import data

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/<name>')
def my_view_func(name):
    new_data=data(name)
    js = json.dumps(new_data)
    return js




if __name__ == '__main__':
    app.run()  # run our Flask app
