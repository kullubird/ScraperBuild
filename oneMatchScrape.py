from riotwatcher import RiotWatcher
import	json
import numpy as np
#custom class to store Api Key
from ApiKey import ApiKey


listNewMatchIds=open('newMatchIdsNa1.txt').read().splitlines()

apiKeyInstance = ApiKey()
#API key setter and region
watcher = RiotWatcher(apiKeyInstance.key)
my_region = 'na1'

setNewMatchIds=set(listNewMatchIds)

for matchId in setNewMatchIds:
 	matchData=watcher.match.timeline_by_match(my_region,matchId)

	for frames in matchList['frames']:

	 	for participantFrames in range(10):

			#print("Participant " + str(matchList['frames'][0]['participantFrames']['1']))
			tempTotalGold

#need an array to store 
	goldArray1[]
	goldArray2[]
