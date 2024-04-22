from flask import Flask, render_template


class QuickQuiz:
    def __init__(self):
        self.app = Flask(__name__)

        @self.app.route("/")
        def index():
            return render_template("index.html")

        # Add more routes and functionality here

    def start(self):
        self.app.run()
