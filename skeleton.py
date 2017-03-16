#File used to call all methods

import methodHeaders
import SongClass
from methodHeaders import musicList
from methodHeaders import selectedMusicList

path = "/home/ubuntu/workspace/proj2-205/Music/"
methodHeaders.initList();

methodHeaders.getMp3s(path);
for SongObjects in methodHeaders.musicList:
	methodHeaders.getID3(path, SongObjects);
for SongObjects in methodHeaders.musicList:
	methodHeaders.getAudioFeatures(SongObjects, methodHeaders.getSpotifyID(SongObjects.artist, SongObjects.album, SongObjects.track))