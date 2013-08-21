#!/usr/bin/python
from __future__ import division
import sys
import human_curl as requests

#Read URL list
try:
    ins = open(sys.argv[1],"r")
    url = []
    for line in ins:
        url.append(line)
    ins.close()
except IOError:
   print "\033[91m Can't open the file!\033[0m" 
   sys.exit()
except LookupError:
    print "\033[91m No file specified!\033[0m"
    print " Hurly usage: \"hurly.py file\" where file contains the sites to be tested"
    sys.exit()

failed = 0

for dest in url:
    httpcode = ""
#Establish the HTTP(S) connection
    try:
        r = requests.get(dest)
#Raise an exception if it fails (couldn't resolve, port not listening, ...)
#We will set up our httpcode to 666 to catch this later
    except:
        result = "\033[93m [???] KO       \033[0m" + dest.rstrip() + " could not be resolved."
        httpcode = 666

#If we were able to connect, save the status code in httpcode    
    if httpcode <> 666:    
        httpcode = r.status_code
    
#Evaluate the status code and print on the screen the result
    if httpcode == 200:
        result = "\033[92m [" + str(httpcode) + "] OK      \033[0m " + dest.rstrip()
    elif httpcode == 301 or r.status_code == 302: 
        result = "\033[94m [" + str(httpcode) + "] REDIRECT\033[0m " + dest.rstrip()
    elif httpcode == 666:
        failed =+ 1
    else:
        result = "\033[91m [" + str(httpcode) + "] KO       \033[0m" + dest.rstrip()
        failed += 1
    print result
#Cleanup
    result = ""

#Calculate % of failed sites
if failed > 0:
    failedpct = failed/len(url)*100
else:
    failedpct = 0

#Print overall result
print ("\n\n %s%% of the listed sites were \033[91mdown\033[0m!" % failedpct)
