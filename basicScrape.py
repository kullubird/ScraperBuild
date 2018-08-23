from riotwatcher import RiotWatcher
import json



#API key setter and region
watcher = RiotWatcher('RGAPI-a0e37b3e-fc36-4fdf-8939-05cb5046f9fa')
my_region = 'na1'

#initilisting lists
newMatchIds=open('newMatchIds.txt').read().splitlines()
doneMatchIds=open('doneMatchIds.txt').read().splitlines()
newUserIds=open('newUserIds.txt').read().splitlines()
doneUserIds=open('doneUserIds.txt').read().splitlines()


accountDetails = watcher.summoner.by_name(my_region, 'pseudonym117')

currentAccountId=accountDetails['accountId']

# 1514745000000 is jan 1st 2018

matchList=watcher.match.matchlist_by_account(my_region,accountDetails['accountId'])

filePointer=open("newMatchIds.txt","a+")
	

# getting all match ids from history of a current account of a paticular id	
for m in matchList['matches']:
	gId = str(m['gameId'])
	filePointer.write(gId + "\n")


filePointer.close()

filePointer=open("doneUserIds.txt","a+")
currentAccountId=str(currentAccountId)
filePointer.write(currentAccountId)
filePointer.close()


#jsonMatchList=json.loads(matchList)
#print(matchList)


# all objects are returned (by default) as a dict
# lets see if i got diamond yet (i probably didnt)

#my_ranked_stats = watcher.league.positions_by_summoner(my_region, me['id'])
#print(my_ranked_stats)

# Lets some champions
#static_champ_list = watcher.static_data.champions(my_region)
#print(static_champ_list)

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