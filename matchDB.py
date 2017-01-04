'''
Storage Module for RankSVoDBot
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Important Design Information:
===========================================================
1. Have a Storage File for current matches (ones not uploaded.)
2. Store completed matches; the container should act as a queue
3. File format: MatchLink | DownloadLink | Duration | Date
4. Suggested: Sort all matches so you can run Binary Search.
===========================================================
'''

class matchWriter:
	'''
		Upon the initialization of a matchWriter,
		Ensure uniqueness of matches.
	'''
	def __init__(self):
		with open('storage/completedMatches.txt', 'r') as db:
			self.completed = [record.split('|') for record in db.read().split('\n')]
		print(self.completed)
		self.queue = open('storage/curMatches.txt', 'w')

	def done(self):
		if !self.queue.closed()
			self.queue.close()

	def newCurMatch(self, matches):
		for match in matches:
			self.queue.write()
