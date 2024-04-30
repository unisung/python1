from tkinter import *
main = Tk()
c = Canvas(main, width=400, height=200)
c.pack()

c.create_line(10, 10, 100, 100)
c.create_line(10, 100, 100, 10, fill="blue")
c.create_rectangle(110, 10, 200, 100, outline="red", width=5)
c.create_oval(210, 10, 300, 100, width=3, fill="yellow")

main.mainloop()