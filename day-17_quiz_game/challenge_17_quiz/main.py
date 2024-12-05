#https://quiz-game-final.appbrewery.repl.run/

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))
#an 'easier to understand way' of doing
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

QuizBrain(question_bank)

QuizBrain.next_question()