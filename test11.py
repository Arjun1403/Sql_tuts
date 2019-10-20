from tkinter import Tk, Frame, Label, Button
import json
import random
import os
window = Tk()
window.geometry("3000x1000")
window.configure(bg='#c5dae6')
from PIL import Image, ImageTk

root_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'images')


i1 = Image.open(os.path.join(root_path, "te.jpg"))
te = ImageTk.PhotoImage(i1)
l2 = Label(window, image=te, width=1420, height=700)
l2.place(x=1, y=2)


class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view, rows, columns):
        global right
        print(letter)
        if (letter == self.correctLetter):
            label = Label(view, text="Right!").grid(row=rows + 10, column=columns)
            right += 1
        else:
            label = Label(view, text="Wrong!").grid(row=rows + 10, column=columns)
        # label.pack()
        view.after(1000, lambda *args: self.unpackView(view))
        view.pack_forget()

    def getView(self, window):
        view = Frame(window, padx=12, pady=12)
        view.place(x=300, y=200)
        view.configure(bg='#696969')
        a = Label(view, text=self.question, font=('Verdana', 15, 'bold'), bg='#696969')
        a.grid(row=2, column=2)

        def looping(loop_answers, rows, columns):
            if len(loop_answers) == 0:
                return

            Button(view, text=loop_answers[0],
                   command=lambda *kwargs: self.check(self.answers.index(loop_answers[0]), view, rows, columns)).grid(
                row=rows,
                column=columns,sticky="ew")
            looping(loop_answers[1:], rows + 1, columns)

            return

        looping(self.answers, 3, 2)

        return view

    def unpackView(self, view):
        view.place_forget()
        askQuestion()


def askQuestion():
    global questions, window, index, button, right, number_of_questions
    if (len(questions) == index + 1):
        Label(window,
              text=f"Thank you for answering the questions\n Your percentage is {right * 100 / total_questions} ",font=('Verdana', 20, 'bold'),bg="#696969").place(
            x=400, y=500)

        return
    button.pack_forget()
    button.place_forget()
    index += 1
    questions[index].getView(window)


def get_questions(json_file_name):
    main_questions = []

    with open(json_file_name) as f:
        questions_dict = json.load(f)

    for question in questions_dict["Questions"]:
        main_questions.append(Question(question['question'], question['options'], question['answer_index']))
    print(len(questions_dict["Questions"]))
    random_questions = random.sample(range(0, len(main_questions)), total_questions)
    print(random_questions)
    selected_questions = []
    for rand_val in random_questions:
        selected_questions.append(main_questions[rand_val])
    return selected_questions

total_questions = 10
index = -1
right = 0
questions = get_questions("questions.json")
number_of_questions = len(questions)

button = Button(window, text="GET STARTED", font=('times', 30, 'bold'), command=askQuestion, bd=20)
button.place(x=500, y=300)

window.mainloop()
