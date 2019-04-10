from bs4 import BeautifulSoup
import urllib2
import re
import pickle


f=open('phone_links','r')
phone_links=pickle.load(f)
f.close()  

f=open('phone_features','r')
phone_details=pickle.load(f)
f.close()  

      
parameters=['gprstext','dimensions','weight','sim','displaytype','displaysize','displayresolution','os','chipset','cpu','gpu','memoryslot','internalmemory','gps','usb','batdescription1']

for i in phone_links:
    
    features=[]
    url = "http://www.gsmarena.com/"+i.rstrip('\n')
    print "Crawling ",url
    text = urllib2.urlopen(url).read()
    soup = BeautifulSoup(text,features="html5lib")
    
    
    
    
    phone_name=soup.find('h1',attrs={'data-spec':'modelname'}).text
    nettech=soup.find('a',attrs={'data-spec':'nettech'}).text
    features.append(phone_name)
    features.append(nettech)
    for j in parameters:
        try:
            features.append(soup.find('td',attrs={'data-spec':j}).text)
        except:
            features.append('-')
    
    phone_details.append(features)
    
f=open('phone_features','wb')
pickle.dump(phone_details,f)
f.close()        
