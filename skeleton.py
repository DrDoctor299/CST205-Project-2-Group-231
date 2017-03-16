#File used to call all methods
from methodHeaders import runBackend

import Tkinter
import tkMessageBox
import tkFileDialog

top = Tkinter.Tk()

#call this method when the playlist has been compiled

def displayPlaylist():#potentially add the playlist data as an argument, multiple ways to do this
    tkMessageBox.showinfo( "Dis a play list", "Songs Songs Songs")
    #tkMessageBox.showmessage("Is anyone out there?")


directory = tkFileDialog.askdirectory()

#where it says insert method, input the first method that starts compiling playlist
B1 = Tkinter.Button(top, text ="Dance", command = displayPlaylist)
B2 = Tkinter.Button(top, text ="Energy", command = displayPlaylist)
B3 = Tkinter.Button(top, text ="Instrumental", command = displayPlaylist)
B4 = Tkinter.Button(top, text ="Acoustic", command = displayPlaylist)
B5 = Tkinter.Button(top, text ="Loudness", command = displayPlaylist)
B6 = Tkinter.Button(top, text ="Speech", command = displayPlaylist)
B7 = Tkinter.Button(top, text ="Tempo", command = displayPlaylist)
B8 = Tkinter.Button(top, text ="Liveness", command = displayPlaylist)

print("I'm running")


B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
B6.pack()
B7.pack()
B8.pack()
top.mainloop()

runBackend(path)



