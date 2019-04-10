from bs4 import BeautifulSoup
import urllib2
import pickle

phone_links=[]

f=open('brandlist.txt','r')
brands=f.readlines()
f.close()


for i in brands:
    url = "http://www.gsmarena.com/"+i.rstrip('\n')
    print "Crawling ",url
    text = urllib2.urlopen(url).read()
    soup = BeautifulSoup(text,features="html5lib")
    
    data = soup.findAll('div',attrs={'class':'makers'})
    for div in data:
        links = div.findAll('a')
        for a in links:
            #print "http://www.gsmarena.com/" + a['href']
            phone_links.append("http://www.gsmarena.com/" + a['href'])
        
f=open('phone_links','wb')
pickle.dump(phone_links,f)
f.close()        
