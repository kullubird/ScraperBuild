from riotwatcher import RiotWatcher
import json

apiKey='RGAPI-d9d994f9-d853-4fa9-bd02-c7b1cfe3ce89'

#API key setter and region
watcher = RiotWatcher(apiKey)
my_region = 'na1'
beignTime=1514745000000


listNewMatchIds=open('newMatchIds.txt').read().splitlines()
listDoneMatchIds=open('doneMatchIds.txt').read().splitlines()
listNewUserIds=open('newUserIds.txt').read().splitlines()
listDoneUserIds=open('doneUserIds.txt').read().splitlines()

#converting lists into sets so no all unique values
setNewMatchIds=set(listNewMatchIds)
setDoneMatchIds=set(listDoneMatchIds)
setNewUserIds=set(listNewUserIds)
setDoneUserIds=set(listDoneUserIds)

currentAccountId=44297600
matchList=watcher.match.matchlist_by_account(my_region,currentAccountId,begin_time=beignTime,season=11,queue=420)

for m in matchList['matches']:
	tempMatchId=m['gameId']
	print("current match id is " + str(tempMatchId))

	#first we request for json response on match details
	matchDetails=watcher.match.by_id(my_region,tempMatchId)
	
	#for each match we try to get id of all new players
	for participants in matchDetails['participantIdentities']:
		setNewMatchIds.add(participants['player']['accountId'])
	

filePointer=open("newUserIds.txt","w")
for lines in setNewUserIds:
	temp=str(lines)
	filePointer.write("%s\n"%temp)
filePointer.close()

filePointer=open("doneUserIds.txt","w")
for lines in setDoneUserIds:
	temp=str(lines)
	filePointer.write("%s\n"%temp)
filePointer.close()

filePointer=open("newMatchIds.txt","w")
for lines in setNewMatchIds:
	temp=str(lines)
	filePointer.write("%s\n"%temp)
filePointer.close()

filePointer=open("doneMatchIds.txt","w")
for lines in setDoneMatchIds:
	temp=str(lines)
	filePointer.write("%s\n"%temp)
filePointer.close()