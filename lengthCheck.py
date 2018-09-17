#custom class to store Api Key
from ApiKey import ApiKey

apiKeyInstance = ApiKey()

myRegion = apiKeyInstance.myRegion
capsRegion = apiKeyInstance.capsRegion

listNewMatchIds=open('Scraped Data/'+myRegion+'/newMatchIds'+capsRegion+'.txt').read().splitlines()
listDoneMatchIds=open('Scraped Data/'+myRegion+'/doneMatchIds'+capsRegion+'.txt').read().splitlines()
listNewUserIds=open('Scraped Data/'+myRegion+'/newUserIds'+capsRegion+'.txt').read().splitlines()
listDoneUserIds=open('Scraped Data/'+myRegion+'/doneUserIds'+capsRegion+'.txt').read().splitlines()

#converting lists into sets so no all unique values
setNewMatchIds=set(listNewMatchIds)
setDoneMatchIds=set(listDoneMatchIds)
setNewUserIds=set(listNewUserIds)
setDoneUserIds=set(listDoneUserIds)



print("Region : "+capsRegion)
print("setNewMatchIds= "+str(len(setNewMatchIds)))
print("setDoneUserIds= "+str(len(setDoneUserIds)))

	#refill the files when program is halted
filePointer=open("Scraped Data/"+myRegion+"/newUserIds"+capsRegion+".txt","w")
for lines in setNewUserIds:
	temp=str(lines)
	filePointer.write("%s\n"%temp)
filePointer.close()

filePointer=open("Scraped Data/"+myRegion+"/doneUserIds"+capsRegion+".txt","w")
for lines in setDoneUserIds:
	temp=str(lines)
	filePointer.write("%s\n"%temp)
filePointer.close()

filePointer=open("Scraped Data/"+myRegion+"/newMatchIds"+capsRegion+".txt","w")
for lines in setNewMatchIds:
	temp=str(lines)
	filePointer.write("%s\n"%temp)
filePointer.close()

filePointer=open("Scraped Data/"+myRegion+"/doneMatchIds"+capsRegion+".txt","w")
for lines in setDoneMatchIds:
	temp=str(lines)
	filePointer.write("%s\n"%temp)
filePointer.close()


##have to do more for euw1