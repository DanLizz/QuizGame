from data import question_data


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number].question
        current_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question}? True or "
                       f"False: ").capitalize()
        self.check_answer(answer=answer, current_answer=current_answer)

    def check_answer(self, answer,current_answer):
        if answer == current_answer:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was: {current_answer}.")
            print(f"Your current score is: {self.score}/{self.question_number}\n")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {current_answer}")
            print(f"Your current score is: {self.score}/{self.question_number}\n")

    def end_of_quiz(self):
        if self.question_number == len(question_data):
            return False
        else:
            return True

    def final_score(self):
        print(f"Your final score is: {self.score}/{self.question_number}\n")
