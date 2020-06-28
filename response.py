import requests
from bs4 import BeautifulSoup
import time

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
s = requests.Session()


sampleFile = open("words.txt", 'r')
subdomain = [line.replace("\n","") for line in sampleFile.readlines()]

# subdomain = ['cpanel','hello','webmail']

counter = 0
for i in subdomain:
    url = "http://"
    url += i
    url += ".brainstation.com.bd/"
    counter = counter + 1
    print(counter)
    try:
        file1 = open("Status.txt", "a+")

        r = s.head(url, headers=headers)
        mod = str(r.status_code)
        file1.write(url+" "+"[" + mod + "]" + "\n")
        print(url)

        file1.close()
    except:
        pass

# url = "http://dhakacitycollege.edu.bd"
# r = s.head(url, headers=headers)
# print(r.status_code)


