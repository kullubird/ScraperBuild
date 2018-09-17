import csv
from riotwatcher import RiotWatcher

#custom class to store Api Key
from ApiKey import ApiKey

#handling for errors
from requests import HTTPError

from pathlib import Path


apiKeyInstance = ApiKey()
#API key setter and region
watcher = RiotWatcher(apiKeyInstance.key)
region = 'na1'


#read all chamions as dictionary for refference

reader = csv.reader(open('Scraped Data/Champions.csv', 'r'))
d={}
for  k,v in reader:
	d[k] = v



tempMatchId=2860069405


# listNewMatchIds=open('newMatchIdsNa1.txt').read().splitlines()
# listDoneMatchIds=open('doneMatchIdsNa1.txt').read().splitlines()


#check if file exists


matchDataFilePath=Path("Scraped Data/"+str(region)+"/MatchData.csv")
if matchDataFilePath.is_file():
	fileFlag=1
else:
	fileFlag=0


#open Match data file

matchDataFile=open("Scraped Data/"+str(region)+"/MatchData.csv",'a')


fnames = ['matchId','seasonId','gameDuration','gameCreation','win','team','firstBlood','firstTower','firstInhibitor','firstDragon','firstRiftHerald','firstBaron','playerKills','towerKills','inhibitorKills','dragonKills','riftHeraldKills','baronKills','ban1','ban2','ban3','ban4','ban5','pick1','pick2','pick3','pick4','pick5']
writerMain = csv.DictWriter(matchDataFile, fieldnames=fnames,lineterminator = '\n')    

if fileFlag==0:
	writerMain.writeheader()



    



#converting lists into sets so no all unique values
# setNewMatchIds=set(listNewMatchIds)
# setDoneMatchIds=set(listDoneMatchIds)



# for tempMatchId in setNewMatchIds


try:
	matchDetails=watcher.match.by_id(region,tempMatchId)
	matchTimeline=watcher.match.timeline_by_match(region,tempMatchId)


	matchId=tempMatchId
	seasonId=matchDetails['seasonId']
	gameDuration=matchDetails['gameDuration']
	gameCreation=matchDetails['gameCreation']



#data for matchData file
	#initializing list to count kills
	playerKills=[0,0]

	#counting kills of both teams and storing it to player kills
	for frames in matchTimeline['frames']:
		for events in frames['events']:
			if events['type'] == "CHAMPION_KILL":
				#ensure which team scored the kill and count it
				if events['killerId']>=0 and events['killerId']<=4:
					playerKills[0]+=1
				elif events['killerId']>=5 and events['killerId']<=9:
					playerKills[1]+=1



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


				
		writerMain.writerow({'matchId':tempMatchId,'seasonId':seasonId,'gameDuration':gameDuration,'gameCreation':gameCreation,'win':win,'team':team,'firstBlood':firstBlood,'firstTower':firstTower,'firstInhibitor':firstInhibitor,'firstDragon':firstDragon,'firstRiftHerald':firstRiftHerald,'firstBaron':firstBaron,'playerKills':playerKills[teamNo],'towerKills':towerKills,'inhibitorKills':inhibitorKills,'dragonKills':dragonKills,'riftHeraldKills':riftHeraldKills,'baronKills':baronKills,'ban1':ban1,'ban2':ban2,'ban3':ban3,'ban4':ban4,'ban5':ban5,'pick1':pick1,'pick2':pick2,'pick3':pick3,'pick4':pick4,'pick5':pick5})


#this data will be used to fill the match timeline file 

# min
# gold,level,minions
# team1 gold and team 2 gold

# 


#opening file with name as match ID
	tempFileName="Scraped Data/"+str(region)+"/TimelineData/"+str(tempMatchId)+".csv"
	#print(tempFileName)
	matchTimelineFile = open(tempFileName,'a')

	fnames = ['minutes','levelPlayer1','levelPlayer2','levelPlayer3','levelPlayer4','levelPlayer5','levelPlayer6','levelPlayer7','levelPlayer8','levelPlayer9','levelPlayer10','minionScorePlayer1','minionScorePlayer2','minionScorePlayer3','minionScorePlayer4','minionScorePlayer5','minionScorePlayer6','minionScorePlayer7','minionScorePlayer8','minionScorePlayer9','minionScorePlayer10','totalGoldPlayer1','totalGoldPlayer2','totalGoldPlayer3','totalGoldPlayer4','totalGoldPlayer5','totalGoldPlayer6','totalGoldPlayer7','totalGoldPlayer8','totalGoldPlayer9','totalGoldPlayer10','totalGoldTeam1','totalGoldTeam2']
	writer = csv.DictWriter(matchTimelineFile, fieldnames=fnames,lineterminator = '\n')    
	writer.writeheader()

	minute=0

	for frames in matchTimeline['frames']:

		minute+=1

		totalGoldPlayer1=frames['participantFrames']['1']['totalGold']
		levelPlayer1=frames['participantFrames']['1']['level']
		minionScorePlayer1=frames['participantFrames']['1']['minionsKilled']

		totalGoldPlayer2=frames['participantFrames']['2']['totalGold']
		levelPlayer2=frames['participantFrames']['2']['level']
		minionScorePlayer2=frames['participantFrames']['2']['minionsKilled']

		totalGoldPlayer3=frames['participantFrames']['3']['totalGold']
		levelPlayer3=frames['participantFrames']['3']['level']
		minionScorePlayer3=frames['participantFrames']['3']['minionsKilled']

		totalGoldPlayer4=frames['participantFrames']['4']['totalGold']
		levelPlayer4=frames['participantFrames']['4']['level']
		minionScorePlayer4=frames['participantFrames']['4']['minionsKilled']

		totalGoldPlayer5=frames['participantFrames']['5']['totalGold']
		levelPlayer5=frames['participantFrames']['5']['level']
		minionScorePlayer5=frames['participantFrames']['5']['minionsKilled']

		totalGoldPlayer6=frames['participantFrames']['6']['totalGold']
		levelPlayer6=frames['participantFrames']['6']['level']
		minionScorePlayer6=frames['participantFrames']['6']['minionsKilled']

		totalGoldPlayer7=frames['participantFrames']['7']['totalGold']
		levelPlayer7=frames['participantFrames']['7']['level']
		minionScorePlayer7=frames['participantFrames']['7']['minionsKilled']

		totalGoldPlayer8=frames['participantFrames']['8']['totalGold']
		levelPlayer8=frames['participantFrames']['8']['level']
		minionScorePlayer8=frames['participantFrames']['8']['minionsKilled']

		totalGoldPlayer9=frames['participantFrames']['9']['totalGold']
		levelPlayer9=frames['participantFrames']['9']['level']
		minionScorePlayer9=frames['participantFrames']['9']['minionsKilled']

		totalGoldPlayer10=frames['participantFrames']['10']['totalGold']
		levelPlayer10=frames['participantFrames']['10']['level']
		minionScorePlayer10=frames['participantFrames']['10']['minionsKilled']



#calculating the team gold per minute
		totalGoldTeam1=totalGoldPlayer1+totalGoldPlayer2+totalGoldPlayer3+totalGoldPlayer4+totalGoldPlayer5	
		totalGoldTeam2=totalGoldPlayer6+totalGoldPlayer7+totalGoldPlayer8+totalGoldPlayer9+totalGoldPlayer10

		writer.writerow({'minutes':minute,'levelPlayer1':levelPlayer1,'levelPlayer2':levelPlayer2,'levelPlayer3':levelPlayer3,'levelPlayer4':levelPlayer4,'levelPlayer5':levelPlayer5,'levelPlayer6':levelPlayer6,'levelPlayer7':levelPlayer7,'levelPlayer8':levelPlayer8,'levelPlayer9':levelPlayer9,'levelPlayer10':levelPlayer10,'minionScorePlayer1':minionScorePlayer1,'minionScorePlayer2':minionScorePlayer2,'minionScorePlayer3':minionScorePlayer3,'minionScorePlayer4':minionScorePlayer4,'minionScorePlayer5':minionScorePlayer5,'minionScorePlayer6':minionScorePlayer6,'minionScorePlayer7':minionScorePlayer7,'minionScorePlayer8':minionScorePlayer8,'minionScorePlayer9':minionScorePlayer9,'minionScorePlayer10':minionScorePlayer10,'totalGoldPlayer1':totalGoldPlayer1,'totalGoldPlayer2':totalGoldPlayer2,'totalGoldPlayer3':totalGoldPlayer3,'totalGoldPlayer4':totalGoldPlayer4,'totalGoldPlayer5':totalGoldPlayer5,'totalGoldPlayer6':totalGoldPlayer6,'totalGoldPlayer7':totalGoldPlayer7,'totalGoldPlayer8':totalGoldPlayer8,'totalGoldPlayer9':totalGoldPlayer9,'totalGoldPlayer10':totalGoldPlayer10,'totalGoldTeam1':totalGoldTeam1,'totalGoldTeam2':totalGoldTeam2})

	




except HTTPError as err:
	if err.response.status_code == 404:
		print("Data not found")
	else:
		print("Pie")
    