from tkinter import *
import pytube
from tkinter import messagebox

# заголовок формы
lb=Label(root, text="---Загрузка видео с YouTube---", font=('Arial, 15, bold'),bg='#D3D3D3')
lb.pack(pady=15)
# пояснительный текст для поля с адресом
lb1=Label(root,text='Ссылка на видео :', font=('Arial, 15, bold'), bg='#D3D3D3')
lb1.place(x=10,y=80)

# поле ввода адреса видео
link1=StringVar()
En1=Entry(root, textvariable=link1,font=('Arial, 15, bold'))
En1.place(x=230,y=80)

# кнопка скачивания
btn1=Button(root, text='Скачать', font=('Arial,10,bold'),bd=4,command=download)
btn1.place(x=330,y=130)

# кнопки очистки и выхода
btn2=Button(root, text='Очистить',font=('Arial',10,bold),bd=4,command=reset)
btn2.place(x=160,y=190)
btn3=Button(root,text=" Выход ",font=('Arial',10,bold),bd=4,command=Exit)
btn3.place(x=250,y=290)

# запускаем окно
root.mainloop()