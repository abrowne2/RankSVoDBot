'''
Write some code here to begin the recording process.
'''

import download as vod
from scite import find_window, send_input, make_input_objects

import time, os
#0xBD for the '-' which you'll use to record.
#just catch the info here, to stop the next keystroke from firing...
# more_info = vod.download('8754553')
csgo = find_window("Counter-Strike: Global Offensive")
l_keys = [ ]; inp = ((0x6D,0))
l_keys.extend(inp)
csinputs = make_input_objects(l_keys)
t = send_input(csgo, csinputs)
# time.sleep(more_info[1])
# win32api.keybd_event(0x6D,0,0)
# time.sleep(5)
# os.system("taskkill /f /im csgo.exe")