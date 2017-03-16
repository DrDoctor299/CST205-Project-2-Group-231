#Import necessary methods from methodHeaders.py
from methodHeaders import runBackend
from methodHeaders import generatePlaylist
from methodHeaders import printPlaylist
from methodHeaders import musicList
from methodHeaders import checkKeyword

#---------------------------------------------------------------------------------------------------------------------------------------------------
#Playlist Generator
#Joshua Williams, Fernando Madrigal, Austin Gray
#CST 205 - Section 2
#
#The user sets a file path to their existing library of songs
#The application will generate a playlist based on 
#song characteristics the user chooses
#
#Joshua wrote the template for our functions, worked on parsing ID3 tags, accessing the Spotify servers and implementing error checking
#Fernando filled in methods and helped with researching
#Austin filled in methods, researched, and created the GUI for the program to run with (Which we then replaced with a command line interface, for seperate reasons)
#
#Github Link:
#https://github.com/DrDoctor299/CST205-Project-2-Group-231
#---------------------------------------------------------------------------------------------------------------------------------------------------


while True:
       print "-----------------------------------------------------------------------"
       path = raw_input("Please enter your song library file path (Must end with '/' character): ")
       print "Getting song information..."
       dirCheck = runBackend(str(path))
       #Used to reenter directory path, if it raises an error
       if dirCheck == -1:
              continue
       
       print "-----------------------------------------------------------------------"
       
       
       #Infinite loop used to check the keyword input, and to allow the creation of multiple playlists
       while True:
              
              #Takes in an input and saves it in "keyword"
              print("Keywords: dance, energy, loudness, speech, acoustic, instrumental, liveness, tempo")
              keyword = raw_input("Select one of the above keywords to generate a playlist: ")
              print "-----------------------------------------------------------------------"
              
              #Evaluates to true only if the keyword is invalid; if so, it returns to the beginning of the loop
              if checkKeyword(keyword):
                     continue
              
              #Generates and prints the playlist
              generatePlaylist(keyword)
              printPlaylist()
              
              #Another infinite loop, used to check the validity of the yes/no answer
              while True:
                     print "1. Create a new playlist from songs in current directory"
                     print "2. Select a new directory"
                     print "3. Exit application"
                     response = raw_input("Option: ")
                     if response == '1' or response == '2' or response == '3':
                            break
                     else:
                            print "Invalid input"
              
              #If response was 3, break twice (Exit); if 2, break once and continue once (New directory); if 1, continue (New playlist)
              if response == '3':
                     break
              elif response == '2':
                     break
              else:
                     continue
              
       #If response was 3, second break (Exit); if 2, continue (new directory)
       if response == '3':
              break
       else:
              continue