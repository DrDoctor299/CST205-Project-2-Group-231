import matplotlib.pyplot as plt
import Tkinter
import tkMessageBox

top = Tkinter.Tk()

#call this method when the playlist has been compiled

def displayPlaylist():#potentially add the playlist data as an argument, multiple ways to do this
   tkMessageBox.showinfo( "Song list goes here")

#where it says insert method, input the first method that starts compiling playlist
B1 = Tkinter.Button(top, text ="Studying", command = displayPlaylist())
B2 = Tkinter.Button(top, text ="Easy Listening", command = displayPlaylist())
B3 = Tkinter.Button(top, text ="Working Out", command = displayPlaylist())
B4 = Tkinter.Button(top, text ="Ready to Go Out", command = displayPlaylist())
B5 = Tkinter.Button(top, text ="Gaming", command = displayPlaylist())


B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
top.mainloop()