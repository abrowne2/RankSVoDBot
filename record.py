'''
Write some code here to begin the recording process.
'''

import download as vod
import win32api as win
import win32con, time, os, win32com.client
from input import PressKey, ReleaseKey

#0x0C for the '/' which you'll use to record.
#just catch the info here, to stop the next keystroke from firing...
# more_info = vod.download('8754553')
shell = win32com.client.Dispatch("WScript.Shell")
shell.AppActivate("Counter-Strike: Global Offensive")
sleep(2)
PressKey(0x13)
time.sleep(.2)
ReleaseKey(0x13)
# os.system("taskkill /f /im csgo.exe")