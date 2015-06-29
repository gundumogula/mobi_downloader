import mechanize
from time import sleep

br = mechanize.Browser()  #Making a browser

br.open('http://inzania.com/temp/kindle/books/')   #website opened

f = open("source.html","w")  #saving the source code of our website in f
f.write(br.response().read())    # in case of errors

files = []

for a in br.links():
    if ".mobi" in str(a):     #searching for files with .mobi file format
        files.append(a)       #adding them to list
        
        
def download(l):              #downloading....
        f = open(l.text,"w")
        br.click_link(l)      #we can even use follow_link - this is even better
        f.write(br.response().read())
        print l.text," has been downloaded" 
        
for l in files:
    sleep(1)                  #may this site survive!
    download(l)
