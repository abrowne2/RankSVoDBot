'''
Write some code here to begin the recording process.
'''

import download as vod
import win32api as win
import time, os, win32gui
from input import PressKey, ReleaseKey


def createVod(more_info):
	hwnd = win32gui.FindWindow(None, "Counter-Strike: Global Offensive")
	win32gui.SetForegroundWindow(hwnd)
	time.sleep(2)
	PressKey(0x21)
	time.sleep(1)
	ReleaseKey(0x21)
	time.sleep(2)
	PressKey(0x1E)
	time.sleep(1)
	ReleaseKey(0x1E)
	time.sleep(more_info[1])
	PressKey(0x1E)
	time.sleep(1)
	ReleaseKey(0x1E)
	time.sleep(5)
	os.system("taskkill /f /im csgo.exe")
	de = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo\\esea_match_"+more_info[3]+'.dem'
	os.remove(de)
	#Video Title, Description, and Keywords:
	return ['Rank S ' + more_info[0] + ' ('+more_info[2]+')', 'ESEA Match: https://play.esea.net/index.php?s=stats&d=match&id='+more_info[3],
	'Csgo,esea,faceit,major,eleague,esports,gaming']