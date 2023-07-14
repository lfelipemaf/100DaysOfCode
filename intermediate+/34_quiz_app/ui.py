from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterFace:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_lbl = Label(text="Score:x",fg="white", bg=THEME_COLOR)
        self.score_lbl.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300,bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="question",
            fill="black",
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50, padx=50)

        true = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true, highlightthickness=0, highlightbackground=THEME_COLOR,
                               highlightcolor=THEME_COLOR, command=self.true_answer)
        self.true_btn.grid(column=0, row=2)

        false = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false, highlightthickness=0, highlightbackground=THEME_COLOR,
                                highlightcolor=THEME_COLOR, command=self.false_answer)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_lbl.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"You've completed the quiz\n"
                                                       f"Your final score was:"
                                                       f" {self.quiz.score}/{self.quiz.question_number}")
            self.score_lbl.config(text="")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
