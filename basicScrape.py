from riotwatcher import RiotWatcher
import json

apiKey='RGAPI-9f43ee03-30db-471a-9bfd-a5cbafe64a1c'

#API key setter and region
watcher = RiotWatcher(apiKey)
my_region = 'na1'

#initilisting lists
listNewMatchIds=open('newMatchIds.txt').read().splitlines()
listDoneMatchIds=open('doneMatchIds.txt').read().splitlines()
listNewUserIds=open('newUserIds.txt').read().splitlines()
listDoneUserIds=open('doneUserIds.txt').read().splitlines()

#converting lists into sets so no all unique values
setNewMatchIds=set(listNewMatchIds)
setDoneMatchIds=set(listDoneMatchIds)
setNewUserIds=set(listNewUserIds)
setDoneUserIds=set(listDoneUserIds)



# 1514745000000 is jan 1st 2018

while len(setNewUserIds)!=0:


	for newId in setNewUserIds:


		# removing item from new set and inserting into done set
		currentAccountId=newId
		setNewUserIds.remove(newId)
		setDoneUserIds.add(newId)

		# getting all match ids from history of a current account of a paticular id

		matchList=watcher.match.matchlist_by_account(my_region,currentAccountId)

		for m in matchList['matches']:

			#will add the tracing for ids of each match here
			setNewMatchIds.add(m)







# Error checking requires importing HTTPError from requests

from requests import HTTPError

# For Riot's API, the 404 status code indicates that the requested data wasn't found and
# should be expected to occur in normal operation, as in the case of a an
# invalid summoner name, match ID, etc.
#
# The 429 status code indicates that the user has sent too many requests
# in a given amount of time ("rate limiting").

try:
    response = watcher.summoner.by_name(my_region, 'this_is_probably_not_anyones_summoner_name')
except HTTPError as err:
    if err.response.status_code == 429:
        print('We should retry in {} seconds.'.format(e.headers['Retry-After']))
        print('this retry-after is handled by default by the RiotWatcher library')
        print('future requests wait until the retry-after time passes')
    elif err.response.status_code == 404:
        print('Summoner with that ridiculous name not found.')
    else:
        print("pie")


 #refill the files

filePointer=open("newUserIds.txt","w")
for lines in setNewUserIds:
	temp=str(lineL)
	filePointer.write("%s\n"%temp)
filePointer.close()

filePointer=open("doneUserIds.txt","w")
for lines in setDoneUserIds:
	temp=str(lineL)
	filePointer.write("%s\n"%temp)
filePointer.close()

filePointer=open("newMatchIds.txt","w")
for lines in setNewMatchIds:
	temp=str(lineL)
	filePointer.write("%s\n"%temp)
filePointer.close()

filePointer=open("doneMatchIds.txt","w")
for lines in setDoneMatchIds:
	temp=str(lineL)
	filePointer.write("%s\n"%temp)
filePointer.close()