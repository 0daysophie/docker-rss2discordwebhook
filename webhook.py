# RSS feed fetcher for Discord webhooks
# change this script accordingly

# current config is for BleepingComputer

import requests
import feedparser
import time

feedtitles = []
feedtexts = []
feedlinks = []
feedarray = []
raw = []

user = "BleepingComputer News Bot"
newsfeedurl = "https://www.bleepingcomputer.com/feed/"
# CHANGE THE WEBHOOK PARAMETER
webhook = ""
avatarurl = "https://yt3.googleusercontent.com/ytc/AIdro_n6mgiaiLKfyhYL_Vot9wfs4xgJyAaQhoYBBv4Gr2M2FA=s160-c-k-c0x00ffffff-no-rj"

def sendmessage(message):
	data = {
		"content" : f"{message}",
		"username" : f"{user}",
		"avatar_url" : f"{avatarurl}"
	}
	
	api = requests.post(webhook, json = data)
	
	result = int(api.status_code)
	textresult = str(api.text)
	
	if result == int(200) or int(204):
		print("STATUS 200/204 OK")
	else:
		print("STATUS " + str(result) + " ERROR")
		print("ERROR: " + textresult)

def clearfeed():
	feedtitles = []
	feedtexts = []
	feedlinks = []
	feedarray = []
	raw = []

def processfeed():
	clearfeed()
	
	raw = feedparser.parse(newsfeedurl)
	feedarray = raw["items"]

	for item in feedarray:
		feedtitles.append(item["title"])
		feedtexts.append(item["summary"])
		feedlinks.append(item["link"])

def messagecomposer():
	for title in feedtitles:
		rawmessage = ""
		titleindex = ""
		titleindex = feedtitles.index(title)
		rawmessage = f'# {title}\n{feedtexts[titleindex]}\n\nURL: {feedlinks[titleindex]}'
		sendmessage(rawmessage)
		time.sleep(10)

while True:
	processfeed()
	messagecomposer()
	time.sleep(86400)
