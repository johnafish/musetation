from tkinter import *

APP_WIDTH = 500
APP_HEIGHT = 500

f = open('./file.txt', 'w')
f.write("var x = [")
f.close()

master = Tk()
master.title("museTation")
screen = Canvas(master, width=APP_WIDTH, height=APP_HEIGHT, background='#0047B2')
screen.pack()

screen.create_text(APP_WIDTH/2, APP_HEIGHT/4, text="museTation", font=("Arial", 50))

start = Button(screen, text='Start', width=25, height=2, bd=2, font=("Sans Serif", 15), fill='gray65')
start.place(x=APP_WIDTH/2, y=APP_HEIGHT/2, anchor='center')

screen.mainloop()