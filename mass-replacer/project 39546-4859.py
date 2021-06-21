import tkinter
import smtplib

main_window = tkinter.Tk()
main_window.geometry('800x600')

lbl_upper = tkinter.Label(
    text="Добро пожаловать в почтовый клиент 'Вестовой' MK2A. Пожалуйста, убедитесь,"
         "что у вас есть соединение с интернетом.",
    width=115,
    height=5
    )
lbl_upper.grid(column=0, row=0)

main_window.mainloop()

