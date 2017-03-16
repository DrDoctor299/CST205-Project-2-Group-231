#File used to call all methods

import methodHeaders
import SongClass

path = ""
methodHeaders.initList();

methodHeaders.getMp3s('/proj2-205/Music');
for SongObjects in methodHeaders.musicList:
	methodHeaders.getID3(path, SongObjects);
for SongObjects in methodHeaders.musicList:
	methodHeaders.getAudioFeatures(SongObjects, methodHeaders.getSpotifyID(SongObjects.getMetadata()))