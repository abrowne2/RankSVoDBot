import os, glob, subprocess

def upload(vid_info):
	video = glob.glob(r'C:\\Users\\Adam\\Videos\\*.avi')[0]
	file = 'C:\\Users\\Adam\\Videos\\' + video
	title = vid_info[0]; desc = vid_info[1]; keywords = vid_info[2]
	cmd = 'python ' + os.getcwd() + 'ytapi.py --file="'+file+'" --title="'+title+'" --description="'+desc+'" --keywords="'+keywords+'" --category="20"'
	u = subprocess.Popen(cmd, shell=True)
	b = u.communicate()
	isUploading = u.wait()
	#os.remove(file)
	return 'done'


upload(['This is a test!', 'Test description', 'blah,test,test1'])

