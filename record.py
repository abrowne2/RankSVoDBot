'''
Write some code here to begin the recording process.
'''

import download as vod
import win32api as win
import win32con, time, os

#0xBD for the '-' which you'll use to record.
#just catch the info here, to stop the next keystroke from firing...
more_info = vod.download('8754553')
win.keybd_event(0xBD, 0,0,0)
time.sleep(.05)
win.keybd_event(0xBD,0,win32con.KEYEVENTF_KEYUP,0)
time.sleep(more_info[1])
win.keybd_event(0xBD, 0,0,0)
time.sleep(.05)
win.keybd_event(0xBD,0,win32con.KEYEVENTF_KEYUP,0)
time.sleep(5)
os.system("taskkill /f /im csgo.exe")