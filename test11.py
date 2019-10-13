from tkinter import Tk, Frame, Label, Button
import json
import os
import pymysql


from time import sleep
window = Tk()

window.geometry("3000x1000")
window.configure(bg='#999999')

class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        print(letter)
        if (letter == self.correctLetter):
            label = Label(view, text="Right!")
            right += 1
        else:
            label = Label(view, text="Wrong!")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))

    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question).pack()

        def looping(loop_answers):
            if len(loop_answers) == 0:
                return

            Button(view, text=loop_answers[0],
                   command=lambda *kwargs: self.check(self.answers.index(loop_answers[0]), view)).pack()
            looping(loop_answers[1:])
            return

        looping(self.answers)

        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()


def askQuestion():
    global questions, window, index, button, right, number_of_questions
    if (len(questions) == index + 1):
        Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(
            number_of_questions) + " questions answered right").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()


def get_questions(json_file_name):
    main_questions = []

    with open(json_file_name) as f:
        questions_dict = json.load(f)

    for question in questions_dict["Questions"]:
        main_questions.append(Question(question['question'], question['options'], question['answer_index']))
    return main_questions


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

index = -1
right = 0
questions = get_questions("questions.json")
number_of_questions = len(questions)


button = Button(window, text="GET STARTED",font=('times', 30, 'bold'), command=askQuestion,bd=20)
button.place(x=500,y=300)
window.mainloop()
