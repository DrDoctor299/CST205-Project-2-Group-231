#Song Object
#Purpose: Define an object which will hold all of the necessary data for each music file

class Song(object):

	def __init__(self, fileName):
		self.fileName = fileName
	
	def addMetadata(self, artist, album, track):
		self.artist = artist
		self.album = album
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
		
	def getMetadata(self):
		return self.artist, self.album, self.track;