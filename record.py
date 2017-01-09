'''
Write some code here to begin the recording process.
'''

import download as vod
import win32api as win
import win32con, time, os, win32gui
from input import PressKey, ReleaseKey

#0x0C for the '/' which you'll use to record.
#just catch the info here, to stop the next keystroke from firing...
more_info = vod.download('8754553')
hwnd = win32gui.FindWindow(None, "Counter-Strike: Global Offensive")
win32gui.SetForegroundWindow(hwnd)
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