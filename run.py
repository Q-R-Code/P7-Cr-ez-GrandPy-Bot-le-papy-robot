#! /usr/bin/env python
from flask import Flask

from botapp import app

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')

if __name__ == "__main__":
    app.run(debug=False)