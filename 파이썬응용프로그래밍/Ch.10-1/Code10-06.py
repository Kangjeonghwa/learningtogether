from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("강아지 버튼","강아지가 귀엽죠?^^")

window=Tk()

photo=PhotoImage(file="C:\\Users\\강정화\\Desktop\\PythonWorkSpace\\파이썬응용프로그래밍\\Ch.10-1\\GIF\\dog2.gif")
button1=Button(window, image=photo, command=myFunc)

button1.pack()

window.mainloop()