#Imports Song Class for use in methods below
import SongClass.py
#Importing libraries used in various functions
import os
import mutagen
import re

#Imports python library built to interface with Spotify API
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
#Spotipy API: http://spotipy.readthedocs.io/en/latest/
#Spotify API for;
	#Audio Features: https://developer.spotify.com/web-api/get-audio-features/
	#Search: https://developer.spotify.com/web-api/search-item/
	#Client Credentials: https://developer.spotify.com/web-api/authorization-guide/#client-credentials-flow

#Create two lists (CURRENTLY UNUSED)
#Purpose: Initialize the list named "musicList" which will contain the Song objects, 
#and the list named "selectedMusicList", which will contain only the Song objects selected as having a desired audio feature
#retuns nothing
def initList():
	global musicList = []
	global selectedMusicList = []
	return;

#Load Music from folder
#Purpose: takes in a path to a folder, finds the names of all mp3 files within that folder
#Creates music objects as Song(fileName) for each, calls the addToList() function to add those objects to "musicList"
#Returns nothing
def getMp3s(path):
	for fileName in os.listdir(path):
	    if fileName.endswith(".mp3"):
			tempSong = Song(fileName)
			addToList(musicList, tempSong)
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
	ID3List = tags.splitlines()
	
	#Creates re (regular expression) objects to compare strings in the provided tags (We will find artist, track and album if they exist)
	artist = re.compile("^u'artist=")
	album = re.compile("^u'album=")
	track = re.compile("^u'title=")
	#Compares all tags for the song against the previously created artist, album and track regular expression objects. On success, these are added to the appropriate Song object's attribute
	for tags in ID3List:
		if re.match(artist, tags, flags=0):
			SongObject.artist = tags.split('=')[1]
		else if re.match(album, tags, flags=0):
			SongObject.album = tags.split('=')[1]
		else if re.match(track, tags, flags=0):
			SongObject.track = tags.split('=')[1]
	return;

#Use metadata to find spotify id
#Purpose: Take in artist name, album name and track 
#Look up track id using search (use all three arguments as keyword inputs)
#return spotify trackID
def getSpotifyID(artist, album, track):
	
	#Store three individual search terms in a variable (each seperated by a space)
	searchTerm = artist + " " + album + " " + track
	
	#Create Spotipy object
	sp = spotipy.Spotify()
	
	#Use spotify object to access the 'search' endpoint of the spotify web API
	#Search using the terms passed in as arguments
	#The three options other than searchTerm mean that the search will return the first Track object (and nothing else)
	#API Link: https://developer.spotify.com/web-api/search-item/
	result = sp.search(searchTerm, limit = 1, offset = 0, type = "track")
	
	#Parse the returned JSON object, accessing the URI
	uri = result['tracks']['items'][0]['uri']
	
	#Split up the URI into its component parts, and save the 3rd part (the spotifyID) into variable spotifyID
	uriList = uri.split(":")
	spotifyID = uriList[2]
	
	return spotifyID;
	
#Use spotifyID to find audio features of each song
#Purpose: Take in "spotifyID" (from findSpotifyID()) and filename
#Use the "audio_features" method in the spotify api to get a list of category scores
#add the category scores to the appropritate Song object using .addAudioFeatures()
#return nothing
def getAudioFeatures(index, spotifyID):
	
	#Generate a authorization token for the application to use
	token = SpotifyClientCredentials('8f4c4bd785ff459f9d3ac53afff5c054', 'c5a47df5d779437b8a14ec418cc6b779')
	#Create a spotipy object using the credentials we generated
	sp = spotipy.Spotify(client_credentials_manager = token)
	
	#Uses the 'audio features' endpoint of the Spotify API
	#API Doc Link: https://developer.spotify.com/web-api/get-audio-features/
	features = sp.audio_features(spotifyID)
	
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
	
	musicList[index].addFeatures(dance, energy, loudness, speech, acoustic, instrumental, liveness, tempo)
	
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


	
#-------------------------------------------------------------------------------------
#Purpose: Use OS to prompt for path to music folder
#Saves selected path in variable "path" as a string
#Also Returns path

#Display category buttons/Take button inputs
#Linked to 

#Create reference array to table only using songs that pass criteria (one for each criteria spotify judges)

#generate output UI

#Export playlist to spotify
