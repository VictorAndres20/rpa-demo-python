# https://likegeeks.com/es/ejemplos-de-la-gui-de-python/
from tkinter import *
from src.rpa.business.process_excel import open_file_excel


def build_label(window):
    lbl = Label(window, text="Hola! Empecemos!", font=("Arial Bold", 20))
    lbl.grid(column=0, row=0)
    return lbl


def build_play_btn(window, lbl):
    def click():
        lbl.configure(text="Procesando")
        open_file_excel()
        lbl.configure(text="Inicar")
    btn = Button(window, text="Play", bg="green", fg="white", command=click)
    btn.grid(column=1, row=0)


def start_app():
    window = Tk()
    window.title("Robot Jake")
    window.geometry('350x200')
    lbl = build_label(window)
    build_play_btn(window, lbl)
    window.mainloop()

