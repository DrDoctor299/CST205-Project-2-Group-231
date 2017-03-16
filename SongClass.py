#Song Object
#Purpose: Define an object which will hold all of the necessary data for each music file

class Song(object):

	def __init__(self, fileName):
		self.fileName = fileName
		self.artist = ""
		self.album = ""
		self.track = ""
	
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