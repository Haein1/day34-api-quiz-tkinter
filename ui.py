
import tkinter as tk
from tkinter.ttk import *
from quiz_brain import QuizBrain
from tkinter import messagebox

'''
Feb 11, 2025: 
solved the ttk label problem

Feb 16, 2025: 
finished setting up the UI, 
shows the questions successfully on the window
'''

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):# quiz_brain:QuizBrain  > parameter: its type
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("QuizInterface")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = tk.Label(text="Score: 00", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        # self.score = tkinter.Text("aaa")
        # self.score.grid(column=1, row=0)

        self.canvas = tk.Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Just for Testing",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_image = tk.PhotoImage(file="./images/true.png")
        self.button_true = tk.Button(image=self.true_image, highlightthickness=0, command=self.correct)
        self.button_true.grid(column=0, row=2)

        self.false_image = tk.PhotoImage(file="./images/false.png")
        self.button_false = tk.Button(image=self.false_image, highlightthickness=0, command=self.wrong)
        self.button_false.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()
        # every function should be listed before mainloop(),
        # otherwise it would be executed until the screen gets clicked

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
    def update_score(self):
        self.score.config(text=f"{self.quiz.score}")

    def correct(self):
        if self.quiz.check_answer("True"):
            messagebox.showinfo("result", "You got it!")
        else:
            messagebox.showinfo("result", "Try next time!")
        self.update_score()
        self.get_next_question()

    def wrong(self):
        if self.quiz.check_answer("False"):
            messagebox.showinfo("result", "You got it!")
        else:
            messagebox.showinfo("result", "Try next time!")
        self.update_score()
        self.get_next_question()


