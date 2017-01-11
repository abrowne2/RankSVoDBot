'''
Runner for Rank S (& Face-it?) Archive
Automation Application
'''
from aggregation import getCurMatches
import time, record, os, glob
import download as vod
import upload as yt
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

current_matches = getCurMatches()
if len(current_matches) > 0:
	current_matches.sort()
	for match in current_matches:
		if len(glob.glob(r'C:\Users\Adam\Videos\*.avi')) == 5:
			break
		#Download the demo.
		match_info = vod.download(match)
		if len(match_info) > 0:
			#begin the recording process here.
			vid_info = record.createVod(match_info)
			done = yt.upload(vid_info)
			arch = ''
			with open(os.getcwd()+'\storage\completed.txt', 'r') as db:
				arch = db.read()
			arch += '\n' + match
			with open(os.getcwd()+'\storage\completed.txt', 'w') as db:
				db.write(arch)
