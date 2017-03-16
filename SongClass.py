#---------------------------------------------------------------------------------------------------------------------------------------------------
#Playlist Generator
#Joshua Williams, Fernando Madrigal, Austin Gray
#CST 205 - Section 2
#3/16/2017
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
#Song Object
#Purpose: Define an object which will hold all of the necessary data for each music file

class Song(object):

	def __init__(self, fileName):
		self.fileName = fileName
		self.artist = ""
		self.album = ""
		self.track = ""
		self.dance = ""
		self.energy = ""
		self.loudness = ""
		self.speech = ""
		self.acoustic = ""
		self.instrumental = ""
		self.liveness = ""
		self.tempo = ""
		
	
	def addArtist(self, artist):
		self.artist = artist
		
	def addAlbum(self, album):
		self.album = album
		
	def addTrack(self, track):
		self.track = track
	
	def addFeatures(self, dance, energy, loudness, speech, acoustic, instrumental, liveness, tempo):
		self.dance = dance
		self.energy = energy
		self.loudness = loudness
		self.speech = speech
		self.acoustic = acoustic
		self.instrumental = instrumental
		self.liveness = liveness
		self.tempo = tempo
