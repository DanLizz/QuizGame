from question_model import  Question
from data import question_data as qd
from quiz_brain import QuizBrain

question_bank = []

for key in qd:
    question_text = key["text"]
    question_answer = key["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
loop = True

while loop:
    quiz.next_question()
    loop = quiz.end_of_quiz()

print("You have completed the quiz")
quiz.final_score()
