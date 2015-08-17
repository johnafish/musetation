from tkinter import *
import museServer
import sys
from threading import *
import os

master = Tk()
master.title("museTation")
master.attributes("-fullscreen", True)
APP_WIDTH = 1366
APP_HEIGHT = 768

def startServer():
	global start, screen, end, serverThread
	start.destroy()
	end = Button(screen, text='End Session', width=25, height=2, bd=2, font=("Sans Serif", 15), activebackground='#4D94FF', background='#4D94FF', command=endServer)
	end.place(x=APP_WIDTH/2, y=APP_HEIGHT/8*5, anchor='center')
	f = open('./file.json', 'w')
	f.write("var x = [")
	f.close()
	museServer.initArrays()
	museServer.runMuseServer()

def endServer():
	global end, screen, start, serverThread, master
	museServer.endServer()
	f = open('./file.json', 'a')
	f.write("]")
	f.close()
	sys.exit()


screen = Canvas(master, width=APP_WIDTH, height=APP_HEIGHT, background='#0047B2')
screen.pack()

screen.create_text(APP_WIDTH/2, APP_HEIGHT/4, text="museTation", font=("Arial", 50), fill="#FFFFFF")

start = Button(screen, text='Start', width=25, height=2, bd=2, font=("Sans Serif", 15), activebackground='#4D94FF', background='#4D94FF', command=startServer)
start.place(x=APP_WIDTH/2, y=APP_HEIGHT/8*5, anchor='center')

screen.mainloop()