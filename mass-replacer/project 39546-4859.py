import tkinter
import smtplib

main_window = tkinter.Tk()
main_window.geometry('800x600')

lbl_upper = tkinter.Label(
    main_window,
    text="Добро пожаловать в почтовый клиент 'Вестовой' MK2A. Пожалуйста, убедитесь,"
         "что у вас есть соединение с интернетом.",
    width=115,
    height=5
    )
lbl_upper.place(relx=0, rely=0.025)

lbl_mid1 = tkinter.Label(
    main_window,
    text="Введите адрес Вашего аккаунта электронной почты:",
)
lbl_mid1.place(relx=0.02, rely=0.2)

email_sender = tkinter.Entry(main_window, width=50)
email_sender.place(relx=0.4, rely=0.205)
sendr = email_sender.get()

lbl_mid2 = tkinter.Label(
    main_window,
    text="Введите пароль (он не будет сохранён после завершения сессии):"
)
lbl_mid2.place(relx=0.02, rely=0.3)

em_send_pass = tkinter.Entry(main_window, width=40)
em_send_pass.place(relx=0.5, rely=0.304)
passwd = em_send_pass.get()

lbl_mid3 = tkinter.Label(
    main_window,
    text="Введите адресата Вашего сообщения:"
)


main_window.mainloop()

