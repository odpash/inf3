from tkinter import *

def main(sourceSmile, sourceText, result):
    ansSecond = ''
    for i in range(len(sourceText)):
        ansSecond += sourceText[i]
        if i % 100 == 0:
            ansSecond += '\n'
    root = Tk()
    root.geometry('800x1080')
    root.title("Lab #3")
    label1 = Label(text=sourceSmile, fg="#eee", bg="#333")
    label1.pack()
    label2 = Label(text=ansSecond, justify=LEFT)
    label2.place(relx=.1, rely=.2)
    label3 = Label(text=result, justify=LEFT)
    label3.pack()
    root.mainloop()