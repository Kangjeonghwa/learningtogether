# 교과서 445 페이지 Code12-06
from tkinter import *

window=Tk()
window.geometry("600x600")

photo=PhotoImage(file="C:/Users/강정화/Desktop/PythonWorkSpace/자료구조/14주차/pet01.gif")

paper=Label(window,image=photo)
paper.pack(expand=1,anchor=CENTER)
window.mainloop()