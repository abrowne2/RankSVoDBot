'''
Use this to download the archive, and then extract it accordingly.
'''

import cfscrape, os
from pyunpack import Archive

def download(match_id):
	r = cfscrape.create_scraper()
	data = r.get('https://play.esea.net/index.php?s=stats&d=match&id=' + match_id).content.decode('utf-8')
	id_loc = data.find('download_replay&id=')
	has_download = True if id_loc != -1 else False
	if has_download:
		#the beginning of the replay id is 19 increments away.
		id_loc += 19; end = data.find('"', id_loc)
		dl_link = 'https://play.esea.net/index.php?s=servers&d=download_replay&id=' + data[id_loc:end]
		next = data.find('>', data.find('alt="Counter-Strike: Global Offensive" align="absmiddle"'))
		
		#extracts the info about the match and places it in more_info
		more_info = [info.strip() for info in data[next+1:data.find('<acronym', next)-1].split('/')]
		#refine the information down into MM/DD/YY TIME, Duration, Mapchoice, demo filename
		more_info = [more_info[0]+'/'+more_info[1]+'/'+more_info[2], more_info[3], more_info[4], 'esea_match_'+match_id]
		#downloads the match archive, and then once completed, extracts it.
		dl = cfscrape.create_scraper()
		archive_data = dl.get(dl_link).content
		
		with open('match.zip', 'wb') as f:
			f.write(archive_data)
		Archive('match.zip').extractall('C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo')
		modifyConfig(match_id)
		return more_info
	return []

#with the match id, change our config so we can open the demo at the start.
def modifyConfig(match_id):
	os.system("taskkill /f /im steam.exe /im steamwebhelper.exe /im steamservice.exe"); loc_config = ''
	cfg = "C:\\Program Files (x86)\\Steam\\userdata\\137759099\\config\\localconfig.vdf"
	with open(cfg, 'r') as c:
		loc_config = c.read()
	cur_id = loc_config.find("esea_match_") + 11; end = loc_config.find('"', cur_id)
	loc_config = loc_config[:cur_id] + match_id + loc_config[end:]
	with open(cfg, 'w') as c:
		c.write(loc_config)