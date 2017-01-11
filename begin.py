from input import PressKey, ReleaseKey
import win32api as win
import time, os, win32gui

'''
Getting the Start Tick (Round 1):
1.) Erase log of Console.
2.) Bootup CS:GO, firing the listimportantticks 
3.) Kill CS:GO, inspect the console and get the start tick.
4.) Write the starttick into the config.
'''

def startTick():
	cnsl = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo\\"
	with open(cnsl + 'console.log', 'w') as f:
		f.write("")
	path = r'C:\"Program Files (x86)"\Steam\Steam.exe -applaunch 730'
	os.system("start " + path)
	time.sleep(45)
	hwnd = win32gui.FindWindow(None, "Counter-Strike: Global Offensive")
	win32gui.SetForegroundWindow(hwnd); time.sleep(2)
	PressKey(0x2D)
	time.sleep(1)
	ReleaseKey(0x2D)
	time.sleep(3)
	os.system("taskkill /f /im csgo.exe"); tick = ''
	with open(cnsl + 'console.log', 'r') as f:
		tick = f.read()
	b = tick.find(' ', tick.find("Tick:", tick.find("bomb_pickup")))
	#get the start tick.
	start = tick[b+1:tick.find(' ', b+1)-1]; cur = ''
	with open(cnsl + 'cfg\\config.cfg', 'r') as cfg:
		cur = cfg.read()
	#write the start tick to the bind so we can begin recording there.
	with open(cnsl + 'cfg\\config.cfg', 'w') as cfg:
		beg = cur.find(' ', cur.find("gototick")); end = cur.find('"', beg) 
		cfg.write(cur[:beg] + start + cur[end:])
	return 'done'
