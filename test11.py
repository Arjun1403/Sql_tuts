from tkinter import Tk, Frame, Label, Button
import json
import random
import os
import pymysql

from time import sleep

#
# master = Tk()
# master.geometry("3000x1000")
# master.configure(bg='#c5dae6')
window = Tk()

window.geometry("3000x1000")
window.configure(bg='#c5dae6')


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
        view = Frame(window, padx=16, pady=16)
        view.place(x=500, y=300)
        a = Label(view, text=self.question, font=('Verdana', 14, 'bold'), bg='#dddddd')
        a.grid(row=2, column=2)

        def looping(loop_answers, rows, columns):
            if len(loop_answers) == 0:
                return

            Button(view, text=loop_answers[0],
                   command=lambda *kwargs: self.check(self.answers.index(loop_answers[0]), view, rows, columns)).grid(
                row=rows,
                column=columns)
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
              text=f"Thank you for answering the questions\n Your percentage is {right * 100 / total_questions} ").place(
            x=500, y=500)

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


# file = open("questions.txt", "r")
# line = file.readline()
# while(line != ""):
#     questionString = line
#     answers = []
#     for i in range (4):
#         answers.append(file.readline())
#
#     correctLetter = file.readline()
#     correctLetter = correctLetter[:-1]
#     questions.append(Question(questionString, answers, correctLetter))
#     line = file.readline()
# file.close()
total_questions = 3
index = -1
right = 0
questions = get_questions("questions.json")
number_of_questions = len(questions)

button = Button(window, text="GET STARTED", font=('times', 30, 'bold'), command=askQuestion, bd=20)
button.place(x=500, y=300)

window.mainloop()
