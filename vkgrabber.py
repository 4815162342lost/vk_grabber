#!/usr/bin/python3.4
import sys
import requests
import json
import os
import urllib
import math
import urllib.request

def parsing(link):
	"""Function for parsing"""
	if int(link.find("album"))!=-1:
		print ("Downloading album")
		people_id=link[link.find("album")+5:link.find("_")]
		album_id=link[link.find("_")+1:]
		if album_id=="0":
			album_id="profile"
		elif album_id=="00":
			album_id="wall"
		elif album_id=="000":
			album_id="saved"
		metod='https://api.vk.com/method/photos.get'
		params={'owner_id': people_id, 'album_id': album_id, 'rev': 0, 'extended' : 0, 'version': 5.40, 'photo_sizes': "0"}
		r=requests.get(metod, params=params)
		data = json.loads(r.text)
		for i in data['response']:
			try:
				url =i['src_xxxbig']
				downloading(url)
			except KeyError:
				try:
					url =i['src_xxbig']
					downloading(url)
				except KeyError:
					try:
						url =i['src_xbig']
						downloading(url)
					except KeyError:
						try:
							url =i['src_big']
							downloading(url)
						except KeyError:
							url =i['src_smal']
							downloading(url)
	if int(link.find("audio"))!=-1:
		print ("Downloading audios")
		people_id=link[link.find("audios")+6:]
		metod='https://api.vk.com/method/audio.get'
		params={'owner_id': people_id, 'need_user': 0 , 'version': 5.40}
		r=requests.get(metod, params=params)
		data = json.loads(r.text)
	if int(link.find("video"))!=-1:
		print ("Downloading videos")

	return 0
def downloading(url):
	"""Function for downloading"""
	print(url)
	file_name=url[url.rfind("/")+1:]
	response = urllib.request.urlopen(url)
	data = response.read()
	f=open(str(file_name), 'wb')
	f.write(data)
	f.close
print ("Hello! It is program for downloading media from vk.com")
link=input("Enter the link")
parsing(link)
