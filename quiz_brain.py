class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank

    def still_has_questions(self):
        num_of_questions = len(self.question_list)
        question_num = self.question_number
        return question_num < num_of_questions

        # check to see if question we are on is the last question in the list
        # if that is true return false because there is no more questions
        # otherwise return true

    def next_question(self):
        next_question = self.question_list[self.question_number]    
        self.question_number += 1
        input(f"Q{self.question_number} {next_question.question} (True/False): ")
