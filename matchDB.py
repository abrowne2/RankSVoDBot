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
	allMatch = allMatch.split()
	#binary search algorithm on the list.
	left = 0; right = len(allMatch) - 1
	while left <= right:
		mid = int((left + right) / 2)
		if allMatch[mid] == match_id:
			return True
		elif allMatch[mid] < match_id:
			left = mid + 1
		elif allMatch[mid] > match_id:
			right = mid - 1
	return False
