#custom class to store Api Key
from ApiKey import ApiKey

apiKeyInstance = ApiKey()

myRegion = apiKeyInstance.myRegion
capsRegion = apiKeyInstance.capsRegion

    
listNewMatchIds=open("Scraped Data/"+str(myRegion)+"/newMatchIds"+str(capsRegion)+".txt")
listDoneUserIds=open("Scraped Data/"+str(myRegion)+"/doneUserIds"+str(capsRegion)+".txt")


#converting lists into sets so no all unique values
setNewMatchIds=set(listNewMatchIds)
setDoneUserIds=set(listDoneUserIds)

print("Region : "+capsRegion)
print("setNewMatchIds= "+str(len(setNewMatchIds)))
print("setDoneUserIds= "+str(len(setDoneUserIds)))


##have to do more for euw1