from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    question_bank.append((Question(questions["text"], questions["answer"])))

# print(question_bank[0].text)

my = QuizBrain(question_bank)

while my.shq():
    my.next_question()

print(my.score)