from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for q in question_data:
    question_bank.append(Question(q["text"],q["answer"]))

print(question_bank)

qb=QuizBrain(question_bank)
# answer=qb.next_question()
# print(answer)

while(qb.still_has_questions()):
    answer=qb.next_question()
print(f"Your final score is {qb.score}")