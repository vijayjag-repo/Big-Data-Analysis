import urllib2
import json
from urllib2 import HTTPError, URLError
from bs4 import BeautifulSoup

key = 'jv6tjGOI5q3eM3wOGevF0BxImHJOVNo2'
count = 1
value = 1
while (count < 11):
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=NHL&sort=newest&fl=web_url&api-key=' + key + '&page=' + str(
        count)
    dataurl = urllib2.urlopen(url)
    data_string = dataurl.read()
    data_json = json.loads(data_string)
    print("Data Block" + str(count))
    print(data_json)
    for item in range(len(data_json['response']['docs'])):
        web = data_json['response']['docs'][item]['web_url']
        if ("http" not in web):
            continue
        try:
            read_url = urllib2.urlopen(web)
        except URLError as e:
            continue
        except HTTPError as e:
            continue

        web_doc = read_url.read()
        soup = BeautifulSoup(web_doc, 'html.parser')
        file = open("./NHL/NHL_File_" + str(value) + ".txt",'w')
        for article in soup.find_all('article'):
            for para in article.find_all('p'):
                file = open("./NHL/NHL_File_" + str(value) + ".txt", 'a')
                file.write(para.get_text().encode('utf-8'))
        file.close()
        value+=1

    for data in data_json['response']['docs']:
        with open("./NHL_URL/NHL_URLSet_" + str(count) + ".json", 'w') as out_json:
            json.dump(data_json, out_json)
            out_json.close()
    dataurl.close()
    count += 1