from tkinter import *
from tkinter import ttk
import os

root = Tk()
root.geometry("300x200")
root.resizable(False,False)
root.title('Reformer')


# Создаем контейнер для размещения текста и поля ввода на одной строке
path = Frame(root)
path.pack(anchor=NW, padx=10, pady=10)
files = Frame(root)
files.pack(anchor=NW,padx=10, pady=20)
choice = Frame(root)
choice.pack(anchor=NW,padx=10, pady=5)


# Добавляем текстовый лейбл слева от поля ввода
label = Label(path, text="Path:")
label.pack(side=LEFT)
label_1 = Label(files, text='Changing the:')
label_1.pack(side = LEFT)
label_1 = Label(files, text=" 's")
label_1.pack(side=RIGHT)
label = Label(choice, text="To:")
label.pack(side=LEFT)

# Поле для ввода текста
way = ttk.Entry(path, width=30)
way.pack(side=LEFT, padx=5)

way1 = ttk.Entry(files, width=10)
way1.pack(side=LEFT, padx=5)

way2 = ttk.Entry(choice, width=10)
way2.pack(side=LEFT, padx=5)
def show_message():
    message_label.config( text = 'Done!')
    root.after(2000,hide_message)

def hide_message():
    message_label.config(text='')
def click_button():
    formats = ['txt','rtf','docx','csv','doc','wps','wpd','msg','wma','snd',
               'jpg','png','webp','gif','tif','bmp','eps','mp3','c','cpp',
               'wav','ra','au','aac','mp4','3gp','avi','mpg','mov','wmv',
               'java','py','js','ts','cs','swift','dta','pl','sh','bat','com',
               'rar','zip','hqx','arj','tar','arc','sit','gz','z','html',
               'htm','xhtml','asp','css','aspx','rss','pdf','docx','exe','md']
    p = os.path.normpath(way.get())
    if '\\' not in p:
        message_label.config(text='Incorrect path!')
        return None
    w = way1.get()
    if w not in formats:
        message_label.config(text='Incorrect format! {1}')
        return None
    g = way2.get()
    if g not in formats:
        message_label.config(text='Incorrect format! {2}')
        return None

    for filename in os.listdir(p):
        old_file_path = os.path.join(p, filename)

        if os.path.isfile(old_file_path):
            if filename.endswith('.'+w):
                new_filename = filename.replace(('.'+w), ('.'+g))
                new_file = os.path.join(p, new_filename)
                os.rename(old_file_path, new_file)

    show_message()


message_label = Label(root,text='', font=('Arial',10))
message_label.pack(pady=1)
# Кнопка для кликов

btn = ttk.Button(root, text="Reform!", command=click_button)
btn.pack(pady=10,padx=10)

root.mainloop()


