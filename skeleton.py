#File used to call all methods

import methodHeaders
import SongClass

path = ""
methodHeaders.initList();

methodHeaders.getMp3s(PathFromUIElement);
for SongObjects in musicList:
	methodHeaders.getID3(path, SongObjects);
for SongObjects in musicList:
	methodHeaders.getAudioFeatures(SongObjects, methodHeaders.getSpotifyID(SongObjects.getMetadata()))