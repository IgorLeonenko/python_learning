from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for el in question_data:
  new_question = Question(el["question"], el["correct_answer"])
  question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()

print("You fifnish the quiz")
print(f"Your final score is: {quiz.final_score()}")