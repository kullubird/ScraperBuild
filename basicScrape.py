from riotwatcher import RiotWatcher

#custom class to store Api Key
from ApiKey import ApiKey

apiKeyInstance = ApiKey()
#API key setter and region
watcher = RiotWatcher(apiKeyInstance.key)
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
beignTime=151474500000

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


			#add api key as its not calling
			
			matchList=watcher.match.matchlist_by_account(my_region,currentAccountId,queue=[420,430,440],begin_time=beignTime,season=11)

			for m in matchList['matches']:

				tempMatchId=m['gameId']

			#check match id to see if done
				if tempMatchId not in listDoneMatchIds:	

					i=i+1
				#will add the tracing for ids of each match here
					print(str(i)+"th current match id is " + str(tempMatchId))


				#first we request for json response on match details
					matchDetails=watcher.match.by_id(my_region,tempMatchId)
				
				#for each match we try to get id of all new players
					for participants in matchDetails['participantIdentities']:
						
						tempMatchPlayerID=str(participants['player']['accountId'])
						
						if tempMatchPlayerID not in listDoneMatchIds:
							listNewUserIds.append(tempMatchPlayerID) 	

					listNewMatchIds.append(tempMatchId)

			print("\n\nReached end of iteration")





except KeyboardInterrupt:

	#set all lists back to sets

	setNewMatchIds=set(listNewMatchIds)
	setDoneMatchIds=set(listDoneMatchIds)
	setNewUserIds=set(listNewUserIds)
	setDoneUserIds=set(listDoneUserIds)
	#refill the files when program is halted
	filePointer=open("newUserIdsNa1.txt","w")
	for lines in setNewUserIds:
		temp=str(lines)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("doneUserIdsNa1.txt","w")
	for lines in setDoneUserIds:
		temp=str(lines)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("newMatchIdsNa1.txt","w")
	for lines in setNewMatchIds:
		temp=str(lines)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("doneMatchIdsNa1.txt","w")
	for lines in setDoneMatchIds:
		temp=str(lines)
		filePointer.write("%s\n"%temp)
	filePointer.close()




#again untill i put it into a function
	#set all lists back to sets

	setNewMatchIds=set(listNewMatchIds)
	setDoneMatchIds=set(listDoneMatchIds)
	setNewUserIds=set(listNewUserIds)
	setDoneUserIds=set(listDoneUserIds)
	#refill the files when program is halted
	filePointer=open("newUserIdsNa1.txt","w")
	for lines in setNewUserIds:
		temp=str(lines)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("doneUserIdsNa1.txt","w")
	for lines in setDoneUserIds:
		temp=str(lines)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("newMatchIdsNa1.txt","w")
	for lines in setNewMatchIds:
		temp=str(lines)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("doneMatchIdsNa1.txt","w")
	for lines in setDoneMatchIds:
		temp=str(lines)
		filePointer.write("%s\n"%temp)
	filePointer.close()





