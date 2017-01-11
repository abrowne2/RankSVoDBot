import os, glob, subprocess

def upload(vid_info):
	file = glob.glob(r'C:\Users\Adam\Videos\*.avi')
	num_files = len(file)
	title = vid_info[0]; desc = vid_info[1]; keywords = vid_info[2]
	with open('Video ' + file[num_files-1], 'w') as de:
		de.write(title)
		de.write(desc)
		de.write(keywords)
	return 'done'


