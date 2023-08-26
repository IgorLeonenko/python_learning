class QuizBrain:
  def __init__(self, q_list):
    self.question_number = 0
    self.question_list = q_list
    self.score = 0

  def next_question(self):
    current_element = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q.{self.question_number}: {current_element.text} (True/False): ")
    self.check_answer(user_answer, current_element.answer)

  def check_answer(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
      print("You right!")
      self.score += 1
    else:
      print("You wrong!")
    print(f"The correct answer is: {correct_answer}")
    print(f"Your score is: {self.score}/{self.question_number}")

  def final_score(self):
    return f"{self.score}/{self.question_number}"


  def still_has_questions(self):
    return self.question_number < len(self.question_list)
