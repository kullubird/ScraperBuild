from riotwatcher import RiotWatcher
import json

apiKey='RGAPI-9f43ee03-30db-471a-9bfd-a5cbafe64a1c'

#API key setter and region
watcher = RiotWatcher(apiKey)
my_region = 'na1'


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
matchList=watcher.match.matchlist_by_account(my_region,currentAccountId)

for m in matchList['matches']:
	tempMatchId=m['gameId']
	print("current match id is " + str(tempMatchId))

	#first we request for json response on match details
	matchDetails=watcher.match.by_id(my_region,tempMatchId)
	
	#for each match we try to get id of all new players
	for participants in matchDetails['participantIdentities']:
		print(participants['player']['accountId'])
	

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