import os
import threading

from flask import Flask, render_template, request

from .quiz import Quiz


class QuickQuiz:
    def __init__(self):
        self.app = Flask(__name__)
        self.quiz = Quiz()

        @self.app.route("/")
        def index():
            terms_string = "\n".join(self.input_terms)
            return render_template("index.html", terms_string=terms_string)

        @self.app.route("/info")
        def info():
            return render_template("info.html")

        @self.app.route("/quiz", methods=["POST", "GET"])
        def quiz():
            if request.method == "POST":
                text = request.form.get("terms")
                if text is not None:
                    terms = [term.strip() for term in text.split("\n") if term.strip()]
                    self.quiz.add_questions(terms)
                    self.quiz.get_next_question()
                    if self.quiz.current_question is not None:
                        return render_template(
                            "quiz.html", term=self.quiz.current_question.term
                        )
            return render_template("index.html", terms=self.input_terms)

        @self.app.route("/pass", methods=["POST"])
        def pass_question():
            self.quiz.pass_current_question()
            if self.quiz.current_question == None:
                return render_template("congratulations.html")
            return render_template("quiz.html", term=self.quiz.current_question.term)

        @self.app.route("/fail", methods=["POST"])
        def fail_question():
            self.quiz.fail_current_question()
            if self.quiz.current_question == None:
                return render_template("congratulations.html")
            return render_template("quiz.html", term=self.quiz.current_question.term)

        @self.app.route("/shutdown", methods=["GET"])
        def shutdown():
            shutdown_server()
            return "Server shutting down..."

    def start(self, terms=[], port=5000):
        """Start the server"""
        self.input_terms = terms
        self.server_thread = threading.Thread(
            target=self.app.run, kwargs={"port": port}
        )
        self.server_thread.start()


def shutdown_server():
    """Shutdown the server"""
    os.kill(os.getpid(), 9)
