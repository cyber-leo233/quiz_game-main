class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    # check to see if question we are on is the last question in the list
    # if that is true return false because there is no more questions
    # otherwise return true
    def still_has_questions(self):
        num_of_questions = len(self.question_list)
        question_num = self.question_number
        return question_num < num_of_questions

    def next_question(self):
        next_question = self.question_list[self.question_number]
        self.question_number += 1
        users_answer = input(f"Q{self.question_number} {next_question.question} (True/False): ")
        self.check_answer(users_answer.lower(), next_question.answer.lower())

    def check_answer(self, users_answer, correct_answer):
        if users_answer == correct_answer:
            self.score += 1
            print("Correct!")

        else:
            print("Incorrect")
        print(f"The correct Answer was {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")

    def final_score(self):
        print("You've completed the quiz")
        print(f"Your final score was: {self.score}/{self.question_number}")
