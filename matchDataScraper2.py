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
myRegion = 'na1'
capsRegion='Na1'


#read all chamions as dictionary for refference

reader = csv.reader(open('Scraped Data/Champions.csv', 'r'))
championsDict={}
for  k,v in reader:
	championsDict[k] = v
#setting -1 for missed bans as blankspace
championsDict[str(-1)]=" "


#read all spells as dictionary for refference
reader = csv.reader(open('Scraped Data/Summoner Spells.csv', 'r'))
spellsDict={}
for  k,v in reader:
	spellsDict[k] = v

#setting -1 for missed bans as blankspace
spellsDict[str(-1)]=" "




#tempMatchId=2860069405


# listNewMatchIds=open('newMatchIdsNa1.txt').read().splitlines()
# listDoneMatchIds=open('doneMatchIdsNa1.txt').read().splitlines()


#check if file exists


matchDataFilePath=Path("Scraped Data/"+str(myRegion)+"/MatchData.csv")
if matchDataFilePath.is_file():
	fileFlag=1
else:
	fileFlag=0


#open Match data file

matchDataFile=open("Scraped Data/"+str(myRegion)+"/MatchData.csv",'a')


fnames = ['matchId','seasonId','gameDuration','gameCreation','win','team','wardsPlaced','firstBlood','firstTower','firstInhibitor','firstDragon','firstRiftHerald','firstBaron','teamKills','towerKills','inhibitorKills','dragonKills','riftHeraldKills','baronKills','ban1','ban2','ban3','ban4','ban5','pick1','pick2','pick3','pick4','pick5','player1Kills','player2Kills','player3Kills','player4Kills','player5Kills','spell1Player1','spell1Player2','spell1Player3','spell1Player4','spell1Player5','spell2Player1','spell2Player2','spell2Player3','spell2Player4','spell2Player5','soloKills','duoKills','trioKills','quadKills','pentaKills']
writerMain = csv.DictWriter(matchDataFile, fieldnames=fnames,lineterminator = '\n')    

if fileFlag==0:
	writerMain.writeheader()



    
listNewMatchIds=open("Scraped Data/"+str(myRegion)+"/newMatchIds"+str(capsRegion)+".txt").read().splitlines()
listDoneMatchIds=open("Scraped Data/"+str(myRegion)+"/doneMatchIds"+str(capsRegion)+".txt").read().splitlines()


#converting lists into sets so no all unique values
setNewMatchIds=set(listNewMatchIds)
setDoneMatchIds=set(listDoneMatchIds)

listDoneMatchIds=list(setDoneMatchIds)
listNewMatchIds=list(setNewMatchIds)

count = 0
flag = 1



# for tempMatchId in setNewMatchIds
while flag == 1:
	for tempMatchId	in listNewMatchIds:


		if flag == 0 :
			break
		else:
			print(str(tempMatchId))



		if tempMatchId not in listDoneMatchIds:
			try:
				matchDetails=watcher.match.by_id(myRegion,tempMatchId)
				matchTimeline=watcher.match.timeline_by_match(myRegion,tempMatchId)


				matchId=tempMatchId
				seasonId=matchDetails['seasonId']
				gameDuration=matchDetails['gameDuration']
				gameCreation="<"+str(matchDetails['gameCreation'])



			#data for matchData file
				#initializing list to count kills
				teamKills=[0,0]
				teamWardsPlaced=[0,0]

				soloKills=[0,0]
				duoKills=[0,0]
				trioKills=[0,0]
				quadKills=[0,0]
				pentaKills=[0,0]





				playerKills=[0,0,0,0,0,0,0,0,0,0,0]
				wardsPlaced=[0,0,0,0,0,0,0,0,0,0,0]

				spell1=["","","","",""]
				spell2=["","","","",""]

				#counting kills of both teams and storing it to player and team kills
				for frames in matchTimeline['frames']:
					tempWardPlaced=0
					tempTimePlaced=0
					for events in frames['events']:
						assistCounter=0
						if events['type'] == "CHAMPION_KILL":
							#ensure which team scored the kill and count it
							tempKillerId=events['killerId']

							if tempKillerId>=0 and tempKillerId<=4:
								teamKills[0]+=1
							elif tempKillerId>=5 and tempKillerId<=9:
								teamKills[1]+=1

							#add it to the respective player's kill count


						#checking how many assists for a kill
							for assists in events['assistingParticipantIds']:
								assistCounter+=1


							if events['killerId'] >=1 and events['killerId'] <=5:
								if assistCounter == 0:
									soloKills[0] += 1
								elif assistCounter == 1:
									duoKills[0] += 1
								elif assistCounter == 2:
									trioKills[0] += 1
								elif assistCounter == 3:
									quadKills[0] += 1
								elif assistCounter == 4:
									pentaKills[0] += 1
								else:
									print("Error" +str(assistCounter))

							else:
								if assistCounter == 0:
									soloKills[1] += 1
								elif assistCounter == 1:
									duoKills[1] += 1
								elif assistCounter == 2:
									trioKills[1] += 1
								elif assistCounter == 3:
									quadKills[1] += 1
								elif assistCounter == 4:
									pentaKills[1] += 1
								else:
									print("Error" +str(assistCounter))




							playerKills[int(tempKillerId)]+=1





						if events['type'] == "WARD_PLACED":
							#ensure that the ward is not a teemo mushroom
							if events['wardType'] != "TEEMO_MUSHROOM":

								if tempWardPlaced != events['creatorId'] and tempTimePlaced != events['timestamp']:

									tempWardPlaced=events['creatorId']
									tempTimePlaced=events['timestamp']


									# teemo shrooms not counted and fix code
									if tempWardPlaced>=0 and tempWardPlaced<=4:
										teamWardsPlaced[0]+=1

									elif tempWardPlaced>=5 and tempWardPlaced<=9:
										teamWardsPlaced[1]+=1




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


					if teamNo==0:
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
					#if id = -1 then ban missed
					ban1=championsDict[str(ban1)]
					ban2=championsDict[str(ban2)]
					ban3=championsDict[str(ban3)]
					ban4=championsDict[str(ban4)]
					ban5=championsDict[str(ban5)]

					pick1=championsDict[str(pick1)]
					pick2=championsDict[str(pick2)]
					pick3=championsDict[str(pick3)]
					pick4=championsDict[str(pick4)]
					pick5=championsDict[str(pick5)]	



					if teamNo == 0:
					# total kill count per player 						
						player1Kills=playerKills[0]
						player2Kills=playerKills[1]
						player3Kills=playerKills[2]
						player4Kills=playerKills[3]
						player5Kills=playerKills[4]

					# summoner spell 1 pick

						for x in range(0,5):
							spell1[x]=spellsDict[str(matchDetails['participants'][x]['spell1Id'])] 

					# summoner spell 2 pick

						for x in range(0,5):
							spell2[x]=spellsDict[str(matchDetails['participants'][x]['spell1Id'])]

					else:

						player1Kills=playerKills[5]
						player2Kills=playerKills[6]
						player3Kills=playerKills[7]
						player4Kills=playerKills[8]
						player5Kills=playerKills[9]

						for x in range(0,5):
							spell1[x]=spellsDict[str(matchDetails['participants'][x+5]['spell1Id'])]	

						for x in range(0,5):
							spell2[x]=spellsDict[str(matchDetails['participants'][x+5]['spell1Id'])]					


							
					writerMain.writerow({'matchId':tempMatchId,'seasonId':seasonId,'gameDuration':gameDuration,'gameCreation':gameCreation,'win':win,'team':team,'wardsPlaced':teamWardsPlaced[teamNo],'firstBlood':firstBlood,'firstTower':firstTower,'firstInhibitor':firstInhibitor,'firstDragon':firstDragon,'firstRiftHerald':firstRiftHerald,'firstBaron':firstBaron,'teamKills':teamKills[teamNo],'towerKills':towerKills,'inhibitorKills':inhibitorKills,'dragonKills':dragonKills,'riftHeraldKills':riftHeraldKills,'baronKills':baronKills,'ban1':ban1,'ban2':ban2,'ban3':ban3,'ban4':ban4,'ban5':ban5,'pick1':pick1,'pick2':pick2,'pick3':pick3,'pick4':pick4,'pick5':pick5,'player1Kills':player1Kills,'player2Kills':player2Kills,'player3Kills':player3Kills,'player4Kills':player4Kills,'player5Kills':player5Kills,'spell1Player1':spell1[0],'spell1Player2':spell1[1],'spell1Player3':spell1[2],'spell1Player4':spell1[3],'spell1Player5':spell1[4],'spell2Player1':spell2[0],'spell2Player2':spell2[1],'spell2Player3':spell2[2],'spell2Player4':spell2[3],'spell2Player5':spell2[4],'soloKills':soloKills[teamNo],'duoKills':duoKills[teamNo],'trioKills':trioKills[teamNo],'quadKills':quadKills[teamNo],'pentaKills':pentaKills[teamNo]})


			#this data will be used to fill the match timeline file 

			# min
			# gold,level,minions
			# team1 gold and team 2 gold

			# 


			#opening file with name as match ID
				tempFileName="Scraped Data/"+str(myRegion)+"/TimelineData/"+str(tempMatchId)+".csv"
				#print(tempFileName)
				matchTimelineFile = open(tempFileName,'a')

				fnames = ['minute','levelPlayer1','levelPlayer2','levelPlayer3','levelPlayer4','levelPlayer5','levelPlayer6','levelPlayer7','levelPlayer8','levelPlayer9','levelPlayer10','minionScorePlayer1','minionScorePlayer2','minionScorePlayer3','minionScorePlayer4','minionScorePlayer5','minionScorePlayer6','minionScorePlayer7','minionScorePlayer8','minionScorePlayer9','minionScorePlayer10','jungleMinionScorePlayer1','jungleMinionScorePlayer2','jungleMinionScorePlayer3','jungleMinionScorePlayer4','jungleMinionScorePlayer5','jungleMinionScorePlayer6','jungleMinionScorePlayer7','jungleMinionScorePlayer8','jungleMinionScorePlayer9','jungleMinionScorePlayer10','totalGoldPlayer1','totalGoldPlayer2','totalGoldPlayer3','totalGoldPlayer4','totalGoldPlayer5','totalGoldPlayer6','totalGoldPlayer7','totalGoldPlayer8','totalGoldPlayer9','totalGoldPlayer10','totalGoldTeam1','totalGoldTeam2']
				writer = csv.DictWriter(matchTimelineFile, fieldnames=fnames,lineterminator = '\n')    
				writer.writeheader()

				minute=0

				for frames in matchTimeline['frames']:

					minute+=1


					totalGoldPlayer1=frames['participantFrames']['1']['totalGold']
					levelPlayer1=frames['participantFrames']['1']['level']
					minionScorePlayer1=frames['participantFrames']['1']['minionsKilled']
					jungleMinionScorePlayer1=frames['participantFrames']['1']['jungleMinionsKilled']


					totalGoldPlayer2=frames['participantFrames']['2']['totalGold']
					levelPlayer2=frames['participantFrames']['2']['level']
					minionScorePlayer2=frames['participantFrames']['2']['minionsKilled']
					jungleMinionScorePlayer2=frames['participantFrames']['2']['jungleMinionsKilled']

					totalGoldPlayer3=frames['participantFrames']['3']['totalGold']
					levelPlayer3=frames['participantFrames']['3']['level']
					minionScorePlayer3=frames['participantFrames']['3']['minionsKilled']
					jungleMinionScorePlayer3=frames['participantFrames']['3']['jungleMinionsKilled']

					totalGoldPlayer4=frames['participantFrames']['4']['totalGold']
					levelPlayer4=frames['participantFrames']['4']['level']
					minionScorePlayer4=frames['participantFrames']['4']['minionsKilled']
					jungleMinionScorePlayer4=frames['participantFrames']['4']['jungleMinionsKilled']


					totalGoldPlayer5=frames['participantFrames']['5']['totalGold']
					levelPlayer5=frames['participantFrames']['5']['level']
					minionScorePlayer5=frames['participantFrames']['5']['minionsKilled']
					jungleMinionScorePlayer5=frames['participantFrames']['5']['jungleMinionsKilled']

					totalGoldPlayer6=frames['participantFrames']['6']['totalGold']
					levelPlayer6=frames['participantFrames']['6']['level']
					minionScorePlayer6=frames['participantFrames']['6']['minionsKilled']
					jungleMinionScorePlayer6=frames['participantFrames']['6']['jungleMinionsKilled']

					totalGoldPlayer7=frames['participantFrames']['7']['totalGold']
					levelPlayer7=frames['participantFrames']['7']['level']
					minionScorePlayer7=frames['participantFrames']['7']['minionsKilled']
					jungleMinionScorePlayer7=frames['participantFrames']['7']['jungleMinionsKilled']

					totalGoldPlayer8=frames['participantFrames']['8']['totalGold']
					levelPlayer8=frames['participantFrames']['8']['level']
					minionScorePlayer8=frames['participantFrames']['8']['minionsKilled']
					jungleMinionScorePlayer8=frames['participantFrames']['8']['jungleMinionsKilled']

					totalGoldPlayer9=frames['participantFrames']['9']['totalGold']
					levelPlayer9=frames['participantFrames']['9']['level']
					minionScorePlayer9=frames['participantFrames']['9']['minionsKilled']
					jungleMinionScorePlayer9=frames['participantFrames']['9']['jungleMinionsKilled']

					totalGoldPlayer10=frames['participantFrames']['10']['totalGold']
					levelPlayer10=frames['participantFrames']['10']['level']
					minionScorePlayer10=frames['participantFrames']['10']['minionsKilled']
					jungleMinionScorePlayer10=frames['participantFrames']['10']['jungleMinionsKilled']



			#calculating the team gold per minute
					totalGoldTeam1=totalGoldPlayer1+totalGoldPlayer2+totalGoldPlayer3+totalGoldPlayer4+totalGoldPlayer5	
					totalGoldTeam2=totalGoldPlayer6+totalGoldPlayer7+totalGoldPlayer8+totalGoldPlayer9+totalGoldPlayer10

					writer.writerow({'minute':minute,'levelPlayer1':levelPlayer1,'levelPlayer2':levelPlayer2,'levelPlayer3':levelPlayer3,'levelPlayer4':levelPlayer4,'levelPlayer5':levelPlayer5,'levelPlayer6':levelPlayer6,'levelPlayer7':levelPlayer7,'levelPlayer8':levelPlayer8,'levelPlayer9':levelPlayer9,'levelPlayer10':levelPlayer10,'minionScorePlayer1':minionScorePlayer1,'minionScorePlayer2':minionScorePlayer2,'minionScorePlayer3':minionScorePlayer3,'minionScorePlayer4':minionScorePlayer4,'minionScorePlayer5':minionScorePlayer5,'minionScorePlayer6':minionScorePlayer6,'minionScorePlayer7':minionScorePlayer7,'minionScorePlayer8':minionScorePlayer8,'minionScorePlayer9':minionScorePlayer9,'minionScorePlayer10':minionScorePlayer10,'jungleMinionScorePlayer1':jungleMinionScorePlayer1,'jungleMinionScorePlayer2':jungleMinionScorePlayer2,'jungleMinionScorePlayer3':jungleMinionScorePlayer3,'jungleMinionScorePlayer4':jungleMinionScorePlayer4,'jungleMinionScorePlayer5':jungleMinionScorePlayer5,'jungleMinionScorePlayer6':jungleMinionScorePlayer6,'jungleMinionScorePlayer7':jungleMinionScorePlayer7,'jungleMinionScorePlayer8':jungleMinionScorePlayer8,'jungleMinionScorePlayer9':jungleMinionScorePlayer9,'jungleMinionScorePlayer10':jungleMinionScorePlayer10,'totalGoldPlayer1':totalGoldPlayer1,'totalGoldPlayer2':totalGoldPlayer2,'totalGoldPlayer3':totalGoldPlayer3,'totalGoldPlayer4':totalGoldPlayer4,'totalGoldPlayer5':totalGoldPlayer5,'totalGoldPlayer6':totalGoldPlayer6,'totalGoldPlayer7':totalGoldPlayer7,'totalGoldPlayer8':totalGoldPlayer8,'totalGoldPlayer9':totalGoldPlayer9,'totalGoldPlayer10':totalGoldPlayer10,'totalGoldTeam1':totalGoldTeam1,'totalGoldTeam2':totalGoldTeam2})

				




			except HTTPError as err:
				if err.response.status_code == 404:
					print("Data not found")
				else:
					print(str(err.response.status_code))



		#remove from new list and add to done
		listNewMatchIds.remove(str(tempMatchId))
		if flag == 1:
			listDoneMatchIds.append(str(tempMatchId))




		count+=1
		print(str(count)+" matches done")

		if count % 2 == 0:
			flag =  input ("Input:\n1 to continue\n0 to quit")
			flag=int(flag)

		if count==20000:
			break

filePointer=open("Scraped Data/"+myRegion+"/doneMatchIds"+capsRegion+".txt","w")
for lines in listDoneMatchIds:
	temp=str(lines)
	filePointer.write("%s\n"%temp)
filePointer.close()
filePointer=open("Scraped Data/"+myRegion+"/newMatchIds"+capsRegion+".txt","w")
for lines in listNewMatchIds:
	temp=str(lines)
	filePointer.write("%s\n"%temp)
filePointer.close()
	    