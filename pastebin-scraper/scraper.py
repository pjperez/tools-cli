#!/usr/bin/python
# Based on p99will's newpastebin.py
# ~pj
import urllib, time, thread, urllib2, os

proxycheck = 0 #set to 1 if you want it to tell you what proxies arnt working and are just wasteing time.
 
 
try:
    print("loading proxies...")
    current = open('proxy.txt', 'r')
    proxies = []
    for line in current:
        proxies.append(line)
    current.close()
except:
    print("Unable to read 'proxy.txt'. Please make sure the file exists and contains a list of proxy servers.")
    print("Also make sure you have read permissions.")
    exit()
print("Proxies loaded. Current proxies:")
     
for i in proxies:
      print i
print('\n')
 
pnum = 0
 
urllib.FancyURLopener.prompt_user_passwd = lambda *a, **k: (None, None)

if not os.path.isdir("./paste")
    os.system("mkdir paste")
 
 
def download(url,proxy,name):
    global lister
    global passes
   
    try:
        proxy_support = urllib2.ProxyHandler({"http":"http://"+proxy})
        opener = urllib2.build_opener(proxy_support)
        urllib2.install_opener(opener)
        html = urllib2.urlopen(url).read()
        try:
            c=open('paste/'+name+'.txt', 'w')
            c.write(html)
            c.close
        except:
            print("Can't save the file, exiting...")
    except:
        if proxycheck == 1:
            print("Proxy: "+proxy+" doesn't work. Please consider removing it from the list.")
        else:
            pass
    else:
        #print("proxy: "+proxy+" Connected successfully")
        lister.append(name)
        temp.append(name)
       
lister = []
temp = []
passes = []
print('Starting...')
while True:
    try:
        data = urllib.urlopen("http://pastebin.com/archive").read()
        data = data.split('<table class="maintable" cellspacing="0">')
        data = data[1]
        data = data.split('</table>')
        data = data[0]
 
 
        data = data.replace('<td><img src="/i/t.gif"  class="i_p0" alt="" border="0" /><a href="/', "!!HTML!!")
        data = data.replace('</a>', "!!HTML!!")
        data = data.split("!!HTML!!")
        for i in data:
            i = i.split("\">")
            i = i[0]
            if not (("</td>" in i) or ("<tr class=" in i)):
                if not ( i in lister):
                    i2 = i
                    i=("http://pastebin.com/raw.php?i="+i)
                    thread.start_new_thread(download, (i,proxies[pnum],i2))
                    pnum += 1
                    if pnum >= len(proxies):
                        pnum = 0
                        time.sleep(10)
                        try:
                            c2=open('index.txt', 'a')      
                            for b in temp:
                                c2.write(b+'\n')
                                print b
                                pass
                            c2.close
                        except:
                            print("Can't write index file, exiting...")
                           
                        temp = [""]
    except:
        print("Couldn't connect to Pastebin. If your proxy settings are correct you may have been banned.")
       
    print("\n-----------New load------------\n")
    time.sleep(10)