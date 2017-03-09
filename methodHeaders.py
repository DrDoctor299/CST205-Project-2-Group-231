#Song Object
#Purpose: Define an object which will hold all of the necessary data for each music file

class Song(object):

	def __init__(fileName):
		self.fileName = fileName
	
	def addMetadata(artist, album, track):
		self.artist = artist
		self.album = album
		self.track = track
	
	def addFeatures(dance, energy, loudness, speech, acoustic, instrumental, liveness, tempo):
		self.dance = dance
		self.energy = energy
		self.loudness = loudness
		self.speech = speech
		self.acoustic = acoustic
		self.instrumental = instrumental
		self.liveness = liveness
		self.tempo = tempo
		
	def getMetadata():
		return self.artist, self.album, self.track;
		
	

	

#Create two lists
#Purpose: Initialize the list named "musicList" which will contain the Song objects, 
#and the list named "selectedMusicList", which will contain only the Song objects selected as having a desired audio feature
#retuns nothing
def initList():

	return;

#Load Music from folder
#Purpose: takes in a path to a folder, finds the names of all mp3 files within that folder
#Creates music objects as Song(fileName) for each, calls the addToList() function to add those objects to "musicList"
#Returns nothing
def getMp3s(path):
	#for(all files in the folder):
		#tempSong = Song(fileName)
		#addToList(tempSong)
	return;
	
#Add songs to "musicList"
#Purpose: takes in a Song object, and appends it to the list "musicList"
#Returns nothing
def addToList(songObject):

	return;
	
#Extract Metadata from file
#Purpose: song object, uses filename from that object to select song from directory 
#From directory, locate MP3 file and extract the ID3 metadata tags to find the Title, Album, and Artist
#Use SongObjectName.addMetadata(artist, album, track) to add to "musicList"
#returns nothing.
def getID3(SongObject):

	return;

#Use metadata to find spotify id
#Purpose: Take in artist name, album name and track 
#Look up track id using search (use all three arguments as keyword inputs)
#return spotify trackID
def getSpotifyID(artist, album, track):

	return spotifyID;

#Use spotifyID to find audio features of each song
#Purpose: Take in "spotifyID" (from findSpotifyID()) and filename
#Use the "audio_features" method in the spotify api to get a list of category scores
#add the category scores to the appropritate Song object using .addAudioFeatures()
#return nothing
def getAudioFeatures(spotifyID):

	return;

#Take in index of "musicList"
#Check single object in "musicList" for specific AudioFeature (uses the appropriate method for that category)
#Returns boolean; true if high in that value, false if not

#Permutations for each catagory:
#dance
def checkDance(index):

	return check;

#energy
def checkEnergy(index):

	return check;
	
#loudness
def checkLoudness(index):

	return check;

#speech
def checkSpeech(index):

	return check;

#acoustic
def checkAcoustic(index):

	return check;
	
#instrumental
def checkInstrumental(index):

	return check;
	
#liveness
def checkLiveness(index):

	return check;
	
#tempo
def checkTempo(index):
	
	return check;

#Take in a keyword for one of the audio features 
#Keywords: dance, energy, loudness, speech, acoustic, instrumental, liveness, tempo
#Iterate through the entire "musicList" and preform a check for the designated audio category (using the check functions above)
#For each check that returns true, add that Song object to a new list "selectedMusicList"
#return nothing
def generatePlaylist(keyword):

	return;
	
#-------------------------------------------------------------------------------------
initList();
getMp3s(PathFromUIElement);
for SongObjects in musicList:
	getID3(SongObjects);
for SongObjects in musicList:
	getAudioFeatures(getSpotifyID(SongObjects.getMetadata()))

	
#-------------------------------------------------------------------------------------
#Purpose: Use OS to prompt for path to music folder
#Saves selected path in variable "path" as a string
#Also Returns path

#Display category buttons/Take button inputs
#Linked to 

#Create reference array to table only using songs that pass criteria (one for each criteria spotify judges)

#generate output UI

#Export playlist to spotify
