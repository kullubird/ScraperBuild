from riotwatcher import RiotWatcher
import json


lines_list = open('newMatchIds.txt').read().splitlines()


print(lines_list)

print(lines_list[1])

print(str(len(lines_list)))