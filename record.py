'''
Write some code here to begin the recording process.
'''

import download as vod
import time, os, win32com.client

#0xBD for the '-' which you'll use to record.
#just catch the info here, to stop the next keystroke from firing...
more_info = vod.download('8754553')
shell = win32com.client.Dispatch("WScript.Shell")
shell.AppActivate("Counter-Strike: Global Offensive")
shell.SendKeys("-")
time.sleep(more_info[1])
shell.SendKeys("-")
time.sleep(5)
os.system("taskkill /f /im csgo.exe")