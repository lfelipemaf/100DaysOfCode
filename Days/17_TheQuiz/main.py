import os

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os
os.system("cls || clear")
question_bank = []
for i in question_data:
    n_question = Question(i['question'], i['correct_answer'])
    question_bank.append(n_question)

end_game = False
quiz = QuizBrain(question_bank)
while quiz.still_has_question():

    quiz.next_question()

os.system("cls || clear")
print(f"\nYou`ve completed the quiz\n"
      f"Your final score was: {quiz.score}/{len(quiz.question_list)}")