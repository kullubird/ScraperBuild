from riotwatcher import RiotWatcher

#custom class to store Api Key
from ApiKey import ApiKey

#handling for errors
from requests import HTTPError


apiKeyInstance = ApiKey()
#API key setter and region
watcher = RiotWatcher(apiKeyInstance.key)
my_region = 'euw1'

# 1514745000000 is jan 1st 2018
beignTime=151474500000


#initilisting lists
listNewMatchIds=open('newMatchIdsEuw1.txt').read().splitlines()
listDoneMatchIds=open('doneMatchIdsEuw1.txt').read().splitlines()
listNewUserIds=open('newUserIdsEuw1.txt').read().splitlines()
listDoneUserIds=open('doneUserIdsEuw1.txt').read().splitlines()

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
			try:
				matchList=watcher.match.matchlist_by_account(my_region,currentAccountId,queue=420,begin_time=beignTime,season=11)
			except HTTPError as err:
				print("~~~~~~~~~~~~~~~~Outer Loop~Error Code: "+str(err.response.status_code))
				continue


			for m in matchList['matches']:

				tempMatchId=m['gameId']

			#check match id to see if done
				if tempMatchId not in listNewMatchIds:	

					i=i+1
				#will add the tracing for ids of each match here
					print(str(i)+"th current match id is " + str(tempMatchId))


				#first we request for json response on match details
					try:
						matchDetails=watcher.match.by_id(my_region,tempMatchId)
					except HTTPError as err:
						print("~~~~~~~~~~~~~~Inner Loop~Error Code: "+str(err.response.status_code))
						continue

				#for each match we try to get id of all new players
					for participants in matchDetails['participantIdentities']:
						
						tempMatchPlayerID=str(participants['player']['accountId'])
						
						if tempMatchPlayerID not in listDoneMatchIds:
							listNewUserIds.append(tempMatchPlayerID) 	

					listNewMatchIds.append(tempMatchId)

			print("\n\nReached end of iteration")

			tempLen=len(set(listNewMatchIds))
			print(str(tempLen)+" ids traversed")

			if(tempLen>=20000):
				print("~~~~~~~~~~~~congratsssssss~~~~~~~~")
				break






except KeyboardInterrupt:

	#set all lists back to sets

	setNewMatchIds=set(listNewMatchIds)
	setDoneMatchIds=set(listDoneMatchIds)
	setNewUserIds=set(listNewUserIds)
	setDoneUserIds=set(listDoneUserIds)
	#refill the files when program is halted
	filePointer=open("newUserIdsEuw1.txt","w")
	for lines in setNewUserIds:
		temp=str(lines)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("doneUserIdsEuw1.txt","w")
	for lines in setDoneUserIds:
		temp=str(lines)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("newMatchIdsEuw1.txt","w")
	for lines in setNewMatchIds:
		temp=str(lines)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("doneMatchIdsEuw1.txt","w")
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
	filePointer=open("newUserIdsEuw1.txt","w")
	for lines in setNewUserIds:
		temp=str(lines)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("doneUserIdsEuw1.txt","w")
	for lines in setDoneUserIds:
		temp=str(lines)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("newMatchIdsEuw1.txt","w")
	for lines in setNewMatchIds:
		temp=str(lines)
		filePointer.write("%s\n"%temp)
	filePointer.close()

	filePointer=open("doneMatchIdsEuw1.txt","w")
	for lines in setDoneMatchIds:
		temp=str(lines)
		filePointer.write("%s\n"%temp)
	filePointer.close()




