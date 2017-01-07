'''
Runner for Rank S (& Face-it?) Archive
Automation Application
'''
from aggregation import getCurMatches
import download as vod
from matchDB import isCompleted

'''
How this Should Work:
-=-=-=-=-=-=-=-=-=-=-
1. Make a Request to the Match using the ID
2. Parse the important about the match;
the download link, duration, and other info.
3. Perform the download and extract the .dem file to the required folder.
(?). Maybe store the filename so you can do playdemo <file_name> while in CS:GO.
4. Begin the Recording phase, which we'll need:
	-> a.) Hotkeys and a Video Recorder that configures properly.
	-> b.) Windowed CS:GO, the required commands to open it up.
	-> c.) [TIMER?] for the duration of the recording.
	-> d.) Afterwards, begin the YouTube upload process.
'''

while True:
	current_matches = getCurMatches()
	current_matches.sort()
	for match in current_matches:
		if isCompleted(match) == False:
			match_info = vod.download(match)
			if len(match_info) > 0:
				