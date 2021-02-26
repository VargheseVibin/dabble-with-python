class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0

    def next_question(self):
        curr_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q{self.question_number}. {curr_question.question_text} (True/False):")
        self.check_answer(user_answer,curr_question.answer)

    def still_has_questions(self):
        if (len(self.question_list)>=self.question_number+1):
            return True
        else:
            return False

    def check_answer(self, user_answer, right_answer):
        if (user_answer.lower()==right_answer.lower()):
            print("Well Done.. That's the right answer")
            self.score+=1
        else:
            print("Sorry! You've got the wrong answer")
        print(f"The right answer is:{right_answer}")