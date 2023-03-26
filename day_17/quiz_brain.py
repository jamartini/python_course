class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        current_answer = input(f"Q{self.question_number}. {current_question.text} (True/False): ")
        self.check_answer(current_answer, current_question.answer)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("You got it right!")
            self.current_score += 1
            print(f"Your current score is {self.current_score}/{self.question_number}")
        else:
            print("That's wrong!")
            print(f"Your current score is {self.current_score}/{self.question_number}")
