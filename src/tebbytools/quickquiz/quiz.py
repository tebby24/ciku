import random
from typing import List


class Question:
    def __init__(self, term):
        self.term = term
        self.priority = 0

    def __str__(self):
        return f"term: {self.term}, priority: {self.priority}"


class Quiz:
    def __init__(self, questions: List[Question] = []):
        self.questions = questions
        self.current_question = self.get_next_question()

    def __str__(self):
        curr_question_str = (
            self.current_question.__str__() if self.current_question else "None"
        )
        questions_str = "\n".join([str(question) for question in self.questions])
        return f"current_question: {curr_question_str}\nquestions:\n{questions_str}\n\n"

    def add_questions(self, terms):
        """Add questions to the quiz"""
        for term in terms:
            self.questions.append(Question(term))

    def get_next_question(self):
        """Choose a question"""
        if self.questions == []:
            self.current_question = None
            return
        lowest_priority = min([question.priority for question in self.questions])
        lowest_priority_questions = [
            question
            for question in self.questions
            if question.priority == lowest_priority
        ]
        self.current_question = random.choice(lowest_priority_questions)

    def pass_current_question(self):
        """Remove the question from the questions list"""
        if self.current_question is None:
            return
        self.questions = [
            question
            for question in self.questions
            if question.term != self.current_question.term
        ]
        self.get_next_question()

    def fail_current_question(self):
        """Increase the priority of the question"""
        if self.current_question is None:
            return
        self.current_question.priority += 1
        self.get_next_question()
