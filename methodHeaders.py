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

def runBackend(path):
	getMp3s(path);
	for SongObjects in musicList:
		getID3(path, SongObjects);
	for SongObjects in musicList:
		getAudioFeatures(SongObjects, getSpotifyID(SongObjects.artist, SongObjects.album, SongObjects.track))
	return;

#Load Music from folder
#Purpose: takes in a path to a folder, finds the names of all mp3 files within that folder
#Creates music objects as Song(fileName) for each, calls the addToList() function to add those objects to "musicList"
#Returns nothing
def getMp3s(path):
	for fileName in os.listdir(path):
	    if fileName.endswith(".mp3"):
			tempSong = Song(fileName)
			addToList(tempSong)
			del tempSong
	return;
	
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
	
	#Accesses current Song
	audio = MP3(path + SongObject.fileName, ID3=EasyID3)
	#Accesses tags for said Song, then splits all tags up into a list
	ID3 = audio.pprint()
	ID3List = ID3.splitlines()
	
	#Compares all tags for the song against the previously created artist, album and track regular expression objects. On success, these are added to the appropriate Song object's attribute
	for tags in ID3List:
		if re.match("artist=.*", tags, flags=0):
			artistRough = tags.split('=')
			SongObject.artist = artistRough[1]
		elif re.match("album=.*", tags, flags=0):
			albumRough = tags.split('=')
			SongObject.album = albumRough[1]
		elif re.match("title=.*", tags, flags=0):
			trackRough = tags.split('=')
			SongObject.track = trackRough[1]
	return;

#Use metadata to find spotify id
#Purpose: Take in artist name, album name and track 
#Look up track id using search (use all three arguments as keyword inputs)
#return spotify trackID
def getSpotifyID(artist, album, track):
	
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
		print "Could not find song on Spotify"
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
def checkDance(index):
	if(musicList[index].dance > .75):
		
		#index is greater than volume
		#check is set to true
		check = True;
	else:
		check = False;
	
	return check;

#energy
def checkEnergy(index):
	if(musicList[index].energy > .75):
		
		#index is greater than volume
		#check is set to true
		check = True;
	else:
		check = False;
	
	return check;
	
#loudness
def checkLoudness(index):
	if(musicList[index].loudness > 30):
		
		#index is greater than volume
		#check is set to true
		check = True;
	else:
		check = False;
	
	return check;

#speech
def checkSpeech(index):
	if(musicList[index].speech > .33 and musicList[index].speech < .66):
		
		#index is greater than volume
		#check is set to true
		check = True;
	else:
		check = False;
	
	return check;

#acoustic
def checkAcoustic(index):
	if(musicList[index].acoustic > .75):
		
		#index is greater than volume
		#check is set to true
		check = True;
	else:
		check = False;
	
	return check;
	
#instrumental
def checkInstrumental(index):
	if(musicList[index].instrumental > .5):
		
		#index is greater than volume
		#check is set to true
		check = True;
	else:
		check = False;
	
	return check;
	
#liveness
def checkLiveness(index):
	if(musicList[index].liveness > .8):
		
		#index is greater than volume
		#check is set to true
		check = True;
	else:
		check = False;
	
	return check;
	
#tempo
def checkTempo(index):
	if(musicList[index].tempo > 120):
		
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
	for song in musicList:
		if keyword is 'dance':
			if checkDance(song):
				addToList(song)
		elif keyword is 'energy':
			if checkEnergy(song):
				addToList(song)
		elif keyword is 'loudness':
			if checkLoudness(song):
				addToList(song)
			
		elif keyword is 'speech':
			if checkSpeech(song):
				addToList(song)
		
		elif keyword is 'acoustic':
			if checkAcoustic(song):
				addToList(song)
		
		elif keyword is 'instrumental':
			if checkInstrumental(song):
				addToList(song)
			
		elif keyword is 'liveness':
			if checkLiveness(song):
				addToList(song)
			
		elif keyword is 'tempo':
			if checkTempo(song):
				addToList(song)

	return;
	
#-------------------------------------------------------------------------------------
