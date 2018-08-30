from riotwatcher import RiotWatcher
import	json
#custom class to store Api Key
from ApiKey import ApiKey

listNewMatchIds=open('newMatchIdsNa1.txt').read().splitlines()

apiKeyInstance = ApiKey()
#API key setter and region
watcher = RiotWatcher(apiKeyInstance.key)
my_region = 'na1'

setNewMatchIds=set(listNewMatchIds)

# for i in setNewMatchIds:
# 	matchList=watcher.match.timeline_by_match(my_region,i)
# 	counter=0

	# for m in matchList['frames']:
	# 	counter+=1

	# 	for playerCount in range(10):
matchList=watcher.match.timeline_by_match(my_region,2848135168)

print("Participant " + str(matchList['frames']))
				#+ "has gold of "+matchList['frames'][playerCount]['totalGold']+" at min " +counter)



