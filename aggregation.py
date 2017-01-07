'''
RankS Match Fetching Here.
'''
#need cfscrape to circumvent esea's cloudflare platform.
import cfscrape
from matchDB import isCompleted

def getCurPlayers():
	standings = 'https://play.esea.net/index.php?s=stats&d=pro'
	results = cfscrape.create_scraper()
	data = results.get(standings).content.decode('utf-8')
	curPos = data.find('/users/'); players = []
	while curPos != -1:
		end = data.find('"', curPos)
		points = data.find('align="right"', curPos)+14; points = data[points:data.find("<",points)]		
		if points != '-' and points != 'Points':
			players.append(data[curPos:end]+'?tab=stats')
		curPos = data.find('/users/', curPos+1)
	return players[1:]


def getCurMatches():
	players = getCurPlayers()
	matcher = cfscrape.create_scraper(); matches = []
	#append /index.php?s=stats&d=match& in front of matches to get their link structure.
	for player in players:
		stats = matcher.get('https://play.esea.net'+player).content.decode('utf-8')
		curPos = stats.find('id=')
		while curPos != -1:		
			matchPos = stats.find('"', curPos)+2
			if stats[matchPos:matchPos+6] == 'Rank S':
				match_id = stats[stats.find("id=", curPos)+3:matchPos-2]
				if isCompleted(match_id) == False:
					matches.append(match_id)
			curPos = stats.find('id=', curPos+1)

	#get unique matches
	return list(set(matches))
