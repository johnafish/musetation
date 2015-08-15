from tkinter import *
import museServer
import sys
from threading import *

APP_WIDTH = 500
APP_HEIGHT = 500

class StoppableThread(Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, target):
        super(StoppableThread, self).__init__()
        self._stop = Event()
        self._target = target

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

def startServer():
	global start, screen, end, serverThread
	start.destroy()
	end = Button(screen, text='End Session', width=25, height=2, bd=2, font=("Sans Serif", 15), activebackground='#4D94FF', background='#4D94FF', command=endServer)
	end.place(x=APP_WIDTH/2, y=APP_HEIGHT/8*5, anchor='center')
	screen.update()
	f = open('./file.txt', 'w')
	f.write("var x = [")
	f.close()
	museServer.initArrays()
	serverThread = StoppableThread(museServer.runMuseServer)
	serverThread.start()

def endServer():
	global end, screen, start, serverThread, master
	serverThread.stop()
	f = open('./file.txt', 'a')
	f.write("]")
	f.close()
	master.destroy()

master = Tk()
master.title("museTation")
screen = Canvas(master, width=APP_WIDTH, height=APP_HEIGHT, background='#0047B2')
screen.pack()

screen.create_text(APP_WIDTH/2, APP_HEIGHT/4, text="museTation", font=("Arial", 50))

start = Button(screen, text='Start', width=25, height=2, bd=2, font=("Sans Serif", 15), activebackground='#4D94FF', background='#4D94FF', command=startServer)
start.place(x=APP_WIDTH/2, y=APP_HEIGHT/8*5, anchor='center')

screen.mainloop()