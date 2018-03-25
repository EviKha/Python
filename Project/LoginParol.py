from tkinter import *
from tkinter import messagebox
import tkinter as tk
import pickle #процесс преобразоватия объектов питон в байты
root = Tk()
root.title("LogIn")
root.geometry("300x500")
def registration():
    text = Label(text="зарегаться")
    text_log = Label(text="кликуха")
    register_login = Entry()
    text_password1 = Label(text="шифр")
    register_password1 = Entry()
    text_password2 = Label(text="конечный шифр")
    register_password2 = Entry(show="*")
    button_register = Button(text="Зарегаться", command = lambda : save())

    text.pack()
    text_log.pack()
    register_login.pack()
    text_password1.pack()
    register_password1.pack()
    text_password2.pack()
    register_password2.pack()
    button_register.pack()
    def save(): #проверка данных
        login_pas_save = {}
        login_pas_save [register_login.get()]=register_password1.get() #чтобы все работало
        #текстовый документ где будет все сохраняться
        f = open ("login.txt", "wb")
        pickle.dump(login_pas_save, f) #сохраняет  введенный логит пас сэйв в текст ф
        f.close()
        login()
#вход в систему
def login():
    text_log = Label ( text = "Входите")
    text_enter_login = Label (text = "Ввод кликухи")
    enter_login = Entry()
    text_enter_pass = Label (text = "го шифр")
    enter_password = Entry (show = "*")
    button_enter = Button(text = "Войти", command = lambda :log_pass())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_password.pack()
    button_enter.pack()

    def log_pass():
        f = open ("login.txt", "rb") #rb записываем wb читаем
        a = pickle.load(f)#выгружениеданных
        f.close()
        if enter_login.get() in a: #условие, если ли необходимый логин в выгруженном словаре
            if enter_password.get() == a [enter_login.get()]: #если введенный пароль соответсвует имени в выгруженном файле, то используем меассаге бокЮВход
                messagebox.showinfo("Ок","Дороооу, чо как?!")
            else:
                messagebox.showerror("не ок","у тебя память, как у рыбки")
        else:
            messagebox.showerror("Oshibka","Эррор")

registration()

root.mainloop()
