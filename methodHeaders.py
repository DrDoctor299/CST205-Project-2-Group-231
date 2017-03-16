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

#Imports Song Class for use in methods below
from SongClass import Song


#Importing libraries used in various functions
import os
import mutagen
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import re

#Imports python library built to interface with Spotify API
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
#Spotipy API: http://spotipy.readthedocs.io/en/latest/
#Spotify API for;
	#Audio Features: https://developer.spotify.com/web-api/get-audio-features/
	#Search: https://developer.spotify.com/web-api/search-item/
	#Client Credentials: https://developer.spotify.com/web-api/authorization-guide/#client-credentials-flow

#Initialize data structures
musicList = []
selectedMusicList = []
badTagsCount = 0
failFindCount = 0

#Purpose: Takes in a path in string form
#Runs all neccessary methods to set up song objects and retrieve neccessary information
#Prints messages to alert user if any songs had no information in their tags, or could not be found on spotify (and how many)
#Returns nothing if success, return -1 if directory could not be found/no mp3s found
def runBackend(path):
	#Clears previous loads into musicList
	global musicList
	musicList = []
	#Searches directory in path, returns to skeleton (with -1) if directory is invalid, otherwise continues
	if getMp3s(path):
		return -1;
	#Iterates over all song objects to find metadata in ID3 tags
	for SongObjects in musicList:
		getID3(path, SongObjects);
	#Iterates over all song objects to find audio features
	for SongObjects in musicList:
		getAudioFeatures(SongObjects, getSpotifyID(SongObjects.artist, SongObjects.album, SongObjects.track))
	#if there were songs not found or that had not tags, prints messages saying so
	if badTagsCount > 0:
		print str(badTagsCount) + " out of " + str(len(musicList)) + " songs did not have tags."
	if failFindCount > 0:
		print str(failFindCount) + " out of " + str(len(musicList)) + " songs could not be located in the Spotify Database"
	return;

#Load Music from folder
#Purpose: takes in a path to a folder, finds the names of all mp3 files within that folder
#Creates music objects as Song(fileName) for each, calls the addToList() function to add those objects to "musicList"
#Returns True if there is an error, returns False if there were no problems
def getMp3s(path):
	noMP3Count = 0
	
	try:
		#Iterate through all files in folder, if they end with '.mp3' add them to 'musicList'
		for fileName in os.listdir(path):
			if fileName.endswith(".mp3"):
				tempSong = Song(fileName)
				addToList(tempSong)
				del tempSong
			else:
				noMP3Count = noMP3Count + 1	
		
		#If the number of non mp3 files is equal to the number of files, print a message saying that there were no MP3s (and return True)
		if noMP3Count == len(os.listdir(path)):
			print "No MP3 files found in directory"
			return True;
		return False;
		
	#If the OS cannot find the directory, print a message saying so (and return True)
	except:
		print "Directory not found"
		return True;
		
	
#Add songs to "musicList"
#Purpose: takes in a Song object and musicList, and appends the Song to the list
#Returns nothing
def addToList(songObject):
	musicList.append(songObject)
	return;
	
def addToSelected(songObject):
	selectedMusicList.append(songObject)
	return;
	
#Extract Metadata from file
#Purpose: song object, uses filename from that object to select song from directory 
#From directory, locate MP3 file and extract the ID3 metadata tags to find the Title, Album, and Artist
#Use SongObjectName.addMetadata(artist, album, track) to add to "musicList"
#returns nothing.
def getID3(path, SongObject):
	#Loop is used with try/except block to catch and fix an input error (missing an ending '/' on inputed path)
	for num in range(2):
		try:
			#Accesses current Song
			audio = MP3(path + SongObject.fileName, ID3=EasyID3)
			#Accesses tags for said Song, then splits all tags up into a list
			ID3 = audio.pprint()
			ID3List = ID3.splitlines()
			
			#Compares all tags for the song against the previously created artist, album and track regular expression objects. On success, these are added to the appropriate Song object's attribute
			for tags in ID3List:
				count = 0
				global badTagsCount
				if re.match("artist=.*", tags, flags=0):
					artistRough = tags.split('=')
					SongObject.artist = artistRough[1]
				elif re.match("album=.*", tags, flags=0):
					albumRough = tags.split('=')
					SongObject.album = albumRough[1]
				elif re.match("title=.*", tags, flags=0):
					trackRough = tags.split('=')
					SongObject.track = trackRough[1]
				else:
					count = count + 1
					if count == len(ID3List):
						badTagsCount = badTagsCount + 1
			return;
			
		#Corrects input error (missing ending '/')
		except:
			path = path + '/'
			continue
		

#Use metadata to find spotify id
#Purpose: Take in artist name, album name and track 
#Look up track id using search (use all three arguments as keyword inputs)
#return spotify trackID
def getSpotifyID(artist, album, track):
	
	global failFindCount
	
	#Store three individual search terms in a variable (each seperated by a space)
	searchTerm = artist + " " + track
	
	#Create Spotipy object
	sp = spotipy.Spotify()
	
	#Use spotify object to access the 'search' endpoint of the spotify web API
	#Search using the terms passed in as arguments
	#The three options other than searchTerm mean that the search will return the first Track object (and nothing else)
	#API Link: https://developer.spotify.com/web-api/search-item/
	result = sp.search(searchTerm, limit = 1, offset = 0, type = "track")
	
	#Parse the returned JSON object, accessing the URI
	try:
		uri = result['tracks']['items'][0]['uri']
	
		#Split up the URI into its component parts, and save the 3rd part (the spotifyID) into variable spotifyID
		uriList = uri.split(":")
		spotifyID = uriList[2]
		return spotifyID;
	except IndexError:
		failFindCount = failFindCount + 1
		return -1;
	
	
#Use spotifyID to find audio features of each song
#Purpose: Take in "spotifyID" (from findSpotifyID()) and filename
#Use the "audio_features" method in the spotify api to get a list of category scores
#add the category scores to the appropritate Song object using .addAudioFeatures()
#return nothing
def getAudioFeatures(SongObject, spotifyID):
	if spotifyID == -1:
		return;
	
	#Generate a authorization token for the application to use
	token = SpotifyClientCredentials('8f4c4bd785ff459f9d3ac53afff5c054', 'c5a47df5d779437b8a14ec418cc6b779')
	#Create a spotipy object using the credentials we generated
	sp = spotipy.Spotify(client_credentials_manager = token)
	
	#Uses the 'audio features' endpoint of the Spotify API
	#API Doc Link: https://developer.spotify.com/web-api/get-audio-features/
	features = sp.audio_features(str(spotifyID))
	
	#dance
	dance = features[0]['danceability']
	#energy
	energy = features[0]['energy']
	#loudness
	loudness = features[0]['loudness']
	#speech
	speech = features[0]['speechiness']
	#acoustic
	acoustic = features[0]['acousticness']
	#instrumental
	instrumental = features[0]['instrumentalness']
	#liveness
	liveness = features[0]['liveness']
	#tempo
	tempo = features[0]['tempo']
	
	SongObject.addFeatures(dance, energy, loudness, speech, acoustic, instrumental, liveness, tempo)
	
	return;


#Permutations for each catagory:
#dance
def checkDance(song):
	#Return true if value of dance is higher than constant
	if(song.dance > .75):
		check = True;
	else:
		check = False;
	
	return check;

#energy
def checkEnergy(song):
	#Return true if value of energy is higher than constant
	if(song.energy > .75):
		check = True;
	else:
		check = False;
	
	return check;
	
#loudness
def checkLoudness(song):
	#Return true if value of loudness is higher than constant
	if(song.loudness > -3 ):
		check = True;
	else:
		check = False;
	
	return check;

#speech
def checkSpeech(song):
	#Return true if value of speech is higher than constant
	if(song.speech > .33 and song.speech < .66):
		check = True;
	else:
		check = False;
	
	return check;

#acoustic
def checkAcoustic(song):
	#Return true if value of acoustic is higher than constant
	if(song.acoustic > .75):
		check = True;
	else:
		check = False;
	
	return check;
	
#instrumental
def checkInstrumental(song):
	#Return true if value of instrumental is higher than constant
	#.5 indicates likely instrumental, closer to 1.0 means higher confidence
	if(song.instrumental > .6):
		check = True;
	else:
		check = False;
	
	return check;
	
#liveness
def checkLiveness(song):
	#Return true if value of liveness is higher than constant
	#API: "A value above 0.8 provides strong likelihood that the track is live."
	if(song.liveness > .8):
		check = True;
	else:
		check = False;
	
	return check;
	
#tempo
def checkTempo(song):
	if(song.tempo > 100):
		
		#index is greater than volume
		#check is set to true
		check = True;
	else:
		check = False;
	
	return check;

#Take in a keyword for one of the audio features 
#Keywords: dance, energy, loudness, speech, acoustic, instrumental, liveness, tempo
#Iterate through the entire "musicList" and preform a check for the designated audio category (using the check functions above)
#For each check that returns true, add that Song object to a new list "selectedMusicList"
#return nothing
def generatePlaylist(keyword):
	
	#Clears selectedMusicList of any residual values
	global selectedMusicList
	selectedMusicList = []
	
	for song in musicList:
		if keyword == 'dance':
			if checkDance(song):
				addToSelected(song)
				
		elif keyword == 'energy':
			if checkEnergy(song):
				addToSelected(song)
				
		elif keyword == 'loudness':
			if checkLoudness(song):
				addToSelected(song)
			
		elif keyword == 'speech':
			if checkSpeech(song):
				addToSelected(song)
		
		elif keyword == 'acoustic':
			if checkAcoustic(song):
				addToSelected(song)
		
		elif keyword == 'instrumental':
			if checkInstrumental(song):
				addToSelected(song)
			
		elif keyword == 'liveness':
			if checkLiveness(song):
				addToSelected(song)
			
		elif keyword == 'tempo':
			if checkTempo(song):
				addToSelected(song)
				
		else:
			print "Not a valid keyword"
			return;

	return;
	
#Purpose: Takes in a string "keyword", and checks to make sure it is valid
#Returns false if valid, and true if not
def checkKeyword(keyword):
	if keyword == 'dance':
		return False;
		
	elif keyword == 'energy':
		return False;
		
	elif keyword == 'loudness':
		return False;
		
	elif keyword == 'speech':
		return False;
	
	elif keyword == 'acoustic':
		return False;
	
	elif keyword == 'instrumental':
		return False;
		
	elif keyword == 'liveness':
		return False;
		
	elif keyword == 'tempo':
		return False;
		
	else:
		print "Not a valid keyword"
		return True;
	
#Prints out the selected playlist on the command line	
#Purpose: Prints out the track name and artist of all songs in selectedMusicList
def printPlaylist():
	
    for song in selectedMusicList:
        print(song.track + " by " + song.artist)
    print "-----------------------------------------------------------------------"
    return;
