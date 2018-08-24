from riotwatcher import RiotWatcher
import json

apiKey='RGAPI-9f43ee03-30db-471a-9bfd-a5cbafe64a1c'

#API key setter and region
watcher = RiotWatcher(apiKey)
my_region = 'na1'

#initilisting lists
listNewMatchIds=open('newMatchIdsNa1.txt').read().splitlines()
listDoneMatchIds=open('doneMatchIdsNa1.txt').read().splitlines()
listNewUserIds=open('newUserIdsNa1.txt').read().splitlines()
listDoneUserIds=open('doneUserIdsNa1.txt').read().splitlines()

#converting lists into sets so no all unique values
setNewMatchIds=set(listNewMatchIds)
setDoneMatchIds=set(listDoneMatchIds)
setNewUserIds=set(listNewUserIds)
setDoneUserIds=set(listDoneUserIds)


#reset set to lists to ensure no repeated values
listNewMatchIds=list(setNewMatchIds)
listDoneMatchIds=list(setDoneMatchIds)
listNewUserIds=list(setNewUserIds)
listDoneUserIds=list(setDoneUserIds)

# 1514745000000 is jan 1st 2018
beignTime=1514745000000

flag=1
i=0
try:
	

	while len(listNewUserIds)!=0:


		for newId in listNewUserIds:


			# removing item from new set and inserting into done set
			if newId not in listDoneUserIds:

				currentAccountId=newId
				listNewUserIds.remove(str(newId))
				listDoneUserIds.append(str(newId))

			# getting all match ids from history of a current account of a paticular id

			matchList=watcher.match.matchlist_by_account(my_region,currentAccountId,begin_time=beignTime,season=11,queue=420)

			for m in matchList['matches']:

			#check match id to see if done
				if tempMatchId not in listDoneMatchIds:	
				#will add the tracing for ids of each match here
					tempMatchId=m['gameId']
					print("current match id is " + str(tempMatchId))


				#first we request for json response on match details
					matchDetails=watcher.match.by_id(my_region,tempMatchId)
				
				#for each match we try to get id of all new players
					for participants in matchDetails['participantIdentities']:
						
						tempMatchPlayerID=str(participants['player']['accountId'])
						
						if tempMatchPlayerID not in listDoneMatchIds:
							listNewUserIds.append(str())

					listDoneMatchIds.append(tempMatchId)





except KeyboardInterrupt:

	#set all lists back to sets

	listNewMatchIds=set(setNewMatchIds)
	listDoneMatchIds=set(setDoneMatchIds)
	listNewUserIds=set(setNewUserIds)
	listDoneUserIds=set(setDoneUserIds)
	#refill the files when program is halted
	filePointer=open("newUserIdsNa1.txt","w")
	for lines in setNewUserIds:
		temp=str(lineL)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("doneUserIdsNa1.txt","w")
	for lines in setDoneUserIds:
		temp=str(lineL)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("newMatchIdsNa1.txt","w")
	for lines in setNewMatchIds:
		temp=str(lineL)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("doneMatchIdsNa1.txt","w")
	for lines in setDoneMatchIds:
		temp=str(lineL)
		filePointer.write("%s\n"%temp)
	filePointer.close()




#again untill i put it into a function
	#set all lists back to sets

	listNewMatchIds=set(setNewMatchIds)
	listDoneMatchIds=set(setDoneMatchIds)
	listNewUserIds=set(setNewUserIds)
	listDoneUserIds=set(setDoneUserIds)
	#refill the files when program is halted
	filePointer=open("newUserIdsNa1.txt","w")
	for lines in setNewUserIds:
		temp=str(lineL)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("doneUserIdsNa1.txt","w")
	for lines in setDoneUserIds:
		temp=str(lineL)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("newMatchIdsNa1.txt","w")
	for lines in setNewMatchIds:
		temp=str(lineL)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("doneMatchIdsNa1.txt","w")
	for lines in setDoneMatchIds:
		temp=str(lineL)
		filePointer.write("%s\n"%temp)
	filePointer.close()





