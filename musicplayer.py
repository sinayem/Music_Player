#Importing Modules
#Pylance ---for video gaming , but here we use it only for sound component
#Tkinter 
#Filedialog from tkinter
#Os
#Askdirectory from filedialog
from tkinter.constants import YES
import pygame
import tkinter
from tkinter.filedialog import askdirectory
import os
from pygame.constants import BUTTON_X2

from pygame.mixer import stop

musicplayer = tkinter.Tk()   #Window
musicplayer.title("Music Player")
musicplayer.geometry("450x350")


directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tkinter.Listbox(musicplayer,font=("arial 20 bold"),bg="green",selectmode=tkinter.SINGLE)

for item in songlist:
    pos = 0
    playlist.insert(pos,item)
    pos = pos + 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkinter.ACTIVE))
    var.set(playlist.get(tkinter.ACTIVE))
    pygame.mixer.music.play()

def exitmusicplayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

#Button

button1 = tkinter.Button(musicplayer,width=5,height=3,font="helvetica 12 bold",text="Play",command=play,bg="yellow",fg="black")
button2 = tkinter.Button(musicplayer,width=5,height=3,font="helvetica 12 bold",text="Stop",command=exitmusicplayer,bg="yellow",fg="black")
button3 = tkinter.Button(musicplayer,width=5,height=3,font="helvetica 12 bold",text="Pause",command=pause,bg="yellow",fg="black")
button4 = tkinter.Button(musicplayer,width=5,height=3,font="helvetica 12 bold",text="Unpause",command=unpause,bg="yellow",fg="black")


#Var for song title
var = tkinter.StringVar()
songtitle = tkinter.Label(musicplayer,font="Helvetica 12 bold",textvariable=var)

#packing
songtitle.pack()
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
playlist.pack(fill="both",expand=YES)

musicplayer.mainloop()