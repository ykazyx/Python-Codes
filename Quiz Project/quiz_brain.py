class QuizBrain:
    def __init__(self, ques_list):
        self.q_number = 0
        self.q_list = ques_list
        self.n = len(self.q_list)
        self.score = 0

    def shq(self):
        return self.q_number < self.n

    def next_question(self):
        current_ques = self.q_list[self.q_number]
        self.q_number += 1
        ans = input(f"Q.{self.q_number}: {current_ques.text} (True/False): ")
        self.score += self.check_answer(ans, current_ques.answer)

    def check_answer(self, ans, correctans):
        if ans == correctans:
            return 1
        else:
            return 0
