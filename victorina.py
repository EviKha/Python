from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Викторина")
root.geometry("250x250")

def que_one():
    question = Label(root,text="Сколько ног у таракана?")
    answer = Entry()
    btn = Button(root, text ="Ответить", command=lambda: game1(que_two))
    question.grid(row=0)
    answer.grid(row=1)
    btn.grid(row=2)

    def game1(que_two):
         if answer.get().lowercase() == "Шесть":
             que_two()
         else :
             messagebox.showerror("ЛОХ", "Нет друзей")

        

def que_two():
    question_2 = Label(root, text="Как быть?")
    answer_2 = Entry()
    btn = Button(root, text = "Ответить")
    question_2.grid(row=0)
    answer_2.grid(row=1)
    btn.grid(row=2)
que_one()

root.mainloop()




