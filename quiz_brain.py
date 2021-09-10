class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank

    def next_question(self):
        next_question = self.question_list[self.question_number]
        input(f"Q{self.question_number} {next_question.question} (True/False): ")
