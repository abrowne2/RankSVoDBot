'''
Storage Module for the Rank S Archive:
=-==--=-=-=-=-=-==----=-=--=-=-=-=-=-=
* Store all matches by id, sorted.
* Search using binary search
* When you are about to begin a new match,
ensure that it hasn't be done already.
'''

def isCompleted(match_id):
	with open('storage/completed.txt', 'r') as db:
		allMatch = db.read()
	return True if allMatch.find(match_id) != -1 else False
