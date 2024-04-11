class QuizBrain:
    def __init__(self, p_quiz):
        self.question_number = 0
        self.score = 0
        self.question_list = p_quiz

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(answer, question.answer)

    def still_has_questions(self):
        remaining_questions = True

        while remaining_questions:
            if self.question_number < len(self.question_list):
                self.next_question()
            else:
                remaining_questions = False

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
            print(f"Current score is: {self.score}/{len(self.question_list)}")
        else:
            print("Wrong!")
        print(f"The correct answer was: {correct_answer}")
