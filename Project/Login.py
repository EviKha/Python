Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
=============================== RESTART: Shell ===============================
>>> #импорт библиотек
from tkinter import *
from tkinter import messagebox
#всплывающие окна

#отрисовываем окно
root = Tk()
root.geometry("300x500")
root.title("LogIn")

#создаем функцию регистрации
def registation():
    text = Label(text="зарегаться")
    text_log = Label(text = "кликуха")
    reqistr_login = Entry()
    text_password1 = Label(text= "шифр")
    reqistr_password1 = Entry()
    text_password2 = Label(text="конечный шифр")
    reqistr_password2 = Entry(show="*") #show = "*" для скрывания букв
    button_registr = Button("Зарегаться")
#адыкватная расстановка
    text.pack()
    text_log.pack()
    reqistr_login.pack()
    text_password1.pack()
    reqistr_password1.pack()
    text_password2.pack()
    reqistr_password2.pack()
    button_registr.pack()
#проверка
registation()
#запуск окна
root.mainloop()
