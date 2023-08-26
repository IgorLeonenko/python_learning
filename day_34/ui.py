from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
  def __init__(self, quiz_brain: QuizBrain):
    self.quiz = quiz_brain
    self.window = Tk()
    self.window.title('Quizz')
    self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
    self.add_canvas_elements()
    self.get_next_question()

    self.window.mainloop()

  def add_canvas_elements(self):
    self.score = Label(text="Score: 0", font=("Arial", 12, "italic", "normal"), bg=THEME_COLOR)
    self.score.grid(column=1, row=0, sticky = "e")

    self.canvas_card = Canvas(width=300, height=250, bg="white", highlightthickness = 0)
    self.question_text = self.canvas_card.create_text(150, 125, width=280, text = "Bbas", font=("Arial", 20, "italic", "bold"), fill="black")
    self.canvas_card.grid(column=0, row=1, columnspan=2)

    self.false_image = PhotoImage(file = "images/false.png")
    self.false_button = Button(image = self.false_image, highlightthickness = 0, command=self.false_answer)
    self.false_button.grid(column=0, row=2)

    self.true_image = PhotoImage(file = "images/true.png")
    self.true_button = Button(image = self.true_image, highlightthickness = 0, command=self.true_answer)
    self.true_button.grid(column=1, row=2)

  def get_next_question(self):
    self.canvas_card.config(bg="white")
    if self.quiz.still_has_questions():
      q_text = self.quiz.next_question()
      self.canvas_card.itemconfig(self.question_text, text=q_text)
      self.score.config(text=f"Score: {self.quiz.score}")
    else:
      self.canvas_card.itemconfig(self.question_text, text="You answer all the questions!")

  def false_answer(self):
    is_right = self.quiz.check_answer(user_answer="false")
    self.get_feedback(is_right)

  def true_answer(self):
    is_right =  self.quiz.check_answer(user_answer="true")
    self.get_feedback(is_right)

  def get_feedback(self, is_right):
    if is_right:
      self.canvas_card.config(bg="green")
    else:
      self.canvas_card.config(bg="red")
    self.window.after(1000, self.get_next_question)


