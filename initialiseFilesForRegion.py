import csv
from riotwatcher import RiotWatcher

#custom class to store Api Key
from ApiKey import ApiKey

#handling for errors
from requests import HTTPError

apiKeyInstance = ApiKey()
#API key setter and region
watcher = RiotWatcher(apiKeyInstance.key)
my_region = 'na1'


#read all chamions as dictionary for refference

reader = csv.reader(open('Scraped Data/Champions.csv', 'r'))
d={}
for  k,v in reader:
	d[k] = v


tempMatchId=2860069405
    # fnames = ['playerInfo','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70']
    # writer = csv.DictWriter(f, fieldnames=fnames,lineterminator = '\n')    


# listNewMatchIds=open('newMatchIdsNa1.txt').read().splitlines()
# listDoneMatchIds=open('doneMatchIdsNa1.txt').read().splitlines()



#converting lists into sets so no all unique values
# setNewMatchIds=set(listNewMatchIds)
# setDoneMatchIds=set(listDoneMatchIds)

# f = open('matchData.csv', 'a')
# with f:

# fnames = ['matchId','seasonId','gameDuration','win','team','firstBlood','firstTower','firstInhibitor','firstDragon','firstRiftHerald','firstBaron','playerKills','towerKills','inhibitorKills','dragonKills','riftHeraldKills','baronKills','ban1','ban2','ban3','ban4','ban5','pick1','pick2','pick3','pick4','pick5']
# writer = csv.DictWriter(f, fieldnames=fnames,lineterminator = '\n')    


# for tempMatchId in setNewMatchIds


try:
	matchDetails=watcher.match.by_id(my_region,tempMatchId)
	matchTimeline=watcher.match.timeline_by_match(my_region,tempMatchId)

	matchId=tempMatchId
	seasonId=matchDetails['seasonId']
	gameDuration=matchDetails['gameDuration']


	#initializing list to count kills
	playerKills=[0,0]


	for teamNo in range(2):


#check if team is on red or blue side
		if matchDetails['teams'][teamNo]['teamId']==100:
			team=1
		else:
			team=0

#check if team won the match
		if matchDetails['teams'][teamNo]['win']=="Win":
			win=1
		else:
			win=0


#check for firstBlood
		if matchDetails['teams'][teamNo]['firstBlood']==True:
			firstBlood=1
		else:
			firstBlood=0

#check for firstTower
		if matchDetails['teams'][teamNo]['firstTower']==True:
			firstTower=1
		else:
			firstTower=0

#check for firstInhibitor
		if matchDetails['teams'][teamNo]['firstInhibitor']==True:
			firstInhibitor=1
		else:
			firstInhibitor=0			

#check for firstDragon
		if matchDetails['teams'][teamNo]['firstDragon']==True:
			firstDragon=1
		else:
			firstDragon=0

#check for firstRiftHerald
		if matchDetails['teams'][teamNo]['firstRiftHerald']==True:
			firstRiftHerald=1
		else:
			firstRiftHerald=0

#check for firstBaron
		if matchDetails['teams'][teamNo]['firstBaron']==True:
			firstBaron=1
		else:
			firstBaron=0



		towerKills=matchDetails['teams'][teamNo]['towerKills']
		inhibitorKills=matchDetails['teams'][teamNo]['inhibitorKills']
		dragonKills=matchDetails['teams'][teamNo]['dragonKills']
		riftHeraldKills=matchDetails['teams'][teamNo]['riftHeraldKills']
		baronKills=matchDetails['teams'][teamNo]['baronKills']


		ban1=matchDetails['teams'][teamNo]['bans'][0]['championId']
		ban2=matchDetails['teams'][teamNo]['bans'][1]['championId']
		ban3=matchDetails['teams'][teamNo]['bans'][2]['championId']
		ban4=matchDetails['teams'][teamNo]['bans'][3]['championId']
		ban5=matchDetails['teams'][teamNo]['bans'][4]['championId']


		if(teamNo==0):
			pick1=matchDetails['participants'][0]['championId']
			pick2=matchDetails['participants'][1]['championId']
			pick3=matchDetails['participants'][2]['championId']
			pick4=matchDetails['participants'][3]['championId']
			pick5=matchDetails['participants'][4]['championId']

		else:
			pick1=matchDetails['participants'][5]['championId']
			pick2=matchDetails['participants'][6]['championId']
			pick3=matchDetails['participants'][7]['championId']
			pick4=matchDetails['participants'][8]['championId']
			pick5=matchDetails['participants'][9]['championId']



		#refferencing dictionary to gete champion names from id
		ban1=d[str(ban1)]
		ban2=d[str(ban2)]
		ban3=d[str(ban3)]
		ban4=d[str(ban4)]
		ban5=d[str(ban5)]

		pick1=d[str(pick1)]
		pick2=d[str(pick2)]
		pick3=d[str(pick3)]
		pick4=d[str(pick4)]
		pick5=d[str(pick5)]	


	for frames in matchTimeline['frames']:
		for events in frames['events']:
			if events['type'] == "CHAMPION_KILL":
				#ensure which team scored the kill and count it
				if events['killerId']>=0 and events['killerId']<=4:
					playerKills[0]+=1
				elif events['killerId']>=5 and events['killerId']<=9:
					playerKills[1]+=1

# print(pick1+pick2+pick3+pick4+pick5+ban1+ban2+ban3+ban4+ban5)
#print("matchId"+str(matchId)+"seasonId"+str(seasonId)+"gameDuration"+str(gameDuration)+"firstBlood"+str(firstBlood)+"firstTower"+str(firstTower)+"firstInhibitor"+str(firstInhibitor)+"firstDragon"+str(firstDragon)+"firstRiftHerald"+str(firstRiftHerald)+"firstBaron"+str(firstBaron)+str(towerKills)+str(inhibitorKills)+str(dragonKills)+str(riftHeraldKills)+str(baronKills))

	



except HTTPError as err:
	if err.response.status_code == 404:
		print("Data not found")
	else:
		print("Pie")
    