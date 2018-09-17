from riotwatcher import RiotWatcher

#custom class to store Api Key
from ApiKey import ApiKey

#handling for errors
from requests import HTTPError


apiKeyInstance = ApiKey()
#API key setter and region
watcher = RiotWatcher(apiKeyInstance.key)
my_region = 'na1'

#reading data into csvFile
listNewMatchIds=open('newMatchIdsNa1.txt').read().splitlines()
listDoneMatchIds=open('doneMatchIdsNa1.txt').read().splitlines()

#converting lists into sets so no all unique values
setNewMatchIds=set(listNewMatchIds)
setDoneMatchIds=set(listDoneMatchIds)

#matchList[‘teams’][0-1][‘bans’][0-4][‘championId’] 

#first we request for json response on match details
matchDetails=watcher.match.by_id(my_region,2852863489)
				
#for each match we try to get banned players
for i in range(2):
	for j in range(5):
		print(matchDetails['teams'][0]['bans'][0]['championId'])
