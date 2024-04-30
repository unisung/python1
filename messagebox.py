from tkinter import *
import tkinter.messagebox
main=Tk()
def btnclick():
    if tkinter.messagebox.askyesno("질문",
                                   "당신은 미성년자입니까?"):
       tkinter.messagebox.showwarning("경고",
                                      "애들은 가라")
    else:
        tkinter.messagebox.showinfo("환영",
                                    "어서오세요,고객님")
btn = Button(main,  text="입장", foreground="Blue",
             command=btnclick())
btn.pack()
main.mainloop()