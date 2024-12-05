#1. Ask the questions
#2. Checks if the answer is correct
#3. Checks if we're the end of the quiz
from data import question_data

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
    
    def next_question(self):
        question = self.question_list[self.question_number]["text"]
        answer = input(f"Q.{self.question_number + 1}: {question}. (True/False)? ")
        #TODO
        #In Development...