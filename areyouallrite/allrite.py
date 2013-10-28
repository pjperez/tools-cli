#!/usr/bin/python
import sys
from bs4 import BeautifulSoup
import requests
import re

try:
	url = sys.argv[1]
	string = sys.argv[2]
	if sys.argv[3] == "False":
		allowredirect = False
	else:
		allowredirect = sys.argv[3] 
except:
	print "Syntax Error!\n\n"
	print "Are you all rite? Usage:"
	print "# allrite <url> <\"string to match\"> <followredirects?>"
	print "e.g.: # allrite http://www.fluffcomputing.com \"cloud\" False\n"
	sys.exit()
	
results = {0:"KO. Reason: Unable to connect", 1:"KO. Reason: String not found", 2:"KO. Reason: Unexpected status code ", 3:"It\'s alive!", 301: "301 Redirect", 302: "302 Redirect", 404: "404 Object not found", 200: "200 OK"}

def getSoup(url, allowredirect):
	try:
		r  = requests.get(url, allow_redirects=allowredirect)
	except:
		result_index = 0
		print results[result_index]
		sys.exit()
	htmlsite = r.text
	soup = BeautifulSoup(htmlsite)
	return r, soup

def healthCheck(string, r, soup):
	if r.status_code == 200:
		if soup.find(text = re.compile(string)) >= 1:
			result_index = 3
			#print results[result_index]
			return result_index, r.status_code
		else:
			result_index = 1
			#print results[result_index]
			return result_index, r.status_code
	else:
		result_index = 2
		#print results[result_index] + str(r.status_code)
		return result_index, r.status_code


def runCheck():
	r, soup = getSoup(url, allowredirect)	
	index = healthCheck(string, r, soup)
	print results[index[0]]
	print "Status code: " + str(results[index[1]])

runCheck()
