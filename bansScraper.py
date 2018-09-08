from riotwatcher import RiotWatcher

#custom class to store Api Key
from ApiKey import ApiKey

apiKeyInstance = ApiKey()
#API key setter and region
watcher = RiotWatcher(apiKeyInstance.key)
my_region = apiKeyInstance.region

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

print(matchDetails['teams'][0]['bans'][0]['championId'])
