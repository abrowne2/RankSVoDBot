'''
Write some code here to begin the recording process.
'''

import download as vod
import time, os, win32api, win32ui

#0xBD for the '-' which you'll use to record.
#just catch the info here, to stop the next keystroke from firing...
# more_info = vod.download('8754553')
shell = win32ui.FindWindow(None, "Counter-Strike: Global Offensive")
shell.SetForegroundWindow()
shell.SetFocus()
win32api.keybd_event(0x6D,0,0)
# time.sleep(more_info[1])
# win32api.keybd_event(0x6D,0,0)
# time.sleep(5)
# os.system("taskkill /f /im csgo.exe")