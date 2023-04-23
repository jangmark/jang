from flask import render_template,Flask
import tkinter as tk
import pandas as pd
from PIL import Image, ImageTk

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# 사용자 입력값 받기


if __name__ == '__main__':
    app.run(debug=True)
