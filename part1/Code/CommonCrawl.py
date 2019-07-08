import requests
import argparse
import time
import json
import gzip
import csv
import codecs

from io import StringIO
from io import BytesIO
from bs4 import BeautifulSoup

import sys


ap = argparse.ArgumentParser()
ap.add_argument("-d","--domain",required = True,help="Enter the target domain")
args = vars(ap.parse_args())

domain = args['domain']

# Fill with index values
index_list = ["2019-04","2019-09","2019-13"]

def search_index(domain):

	record_list = []
	print ("Trying target domain: %s" % domain)
	for index in index_list:
		print ("Trying index %s" % index)
		cc_url = "http://index.commoncrawl.org/CC-MAIN-%s-index?" % index
		cc_url = cc_url + "url=%s&output=json" % domain
		response = requests.get(cc_url)

		if response.status_code == 200:
			records = response.content.splitlines()
			for record in records:
				record_list.append(json.loads(record.decode('utf-8')))
			print("Added %d results." % len(records))
	print("Found a total of %d hits" % len(record_list))
	return record_list

def download_page(record):

	offset, length = int(record['offset']),int(record['length'])
	offset_end = offset + length - 1

	prefix = "https://commoncrawl.s3.amazonaws.com/"

	resp = requests.get(prefix + record['filename'], headers={'Range': 'bytes={}-{}'.format(offset, offset_end)})
	data = gzip.decompress(resp.content).decode('utf-8')
	response = ""

	if len(data):
		try:
			warc, header, response = data.strip().split('\r\n\r\n', 2)
		except:
			pass
	return response

def main():

	record_list = search_index(domain)
	p_dict = {}
	
	for record in record_list:
		html_content = download_page(record)
		url = record['url']
		id_index = 0
		s_index = 0
		id_index = url.find("25")
		s_index = url.find("/",id_index)
		id = url[id_index : s_index]
		print("Retreived %d bytes for %s" % (len(html_content),record['url']))
		print(id)
		page_content = BeautifulSoup(html_content, "html.parser")
		p_tags = page_content.find_all("p")
		length = len(p_tags)
		print(length)
		#paragraphs = []
		paragraphs = ""
		for i in range(1,length-1):
			#paragraphs.append(p_tags[i].text)
			paragraphs = paragraphs + str(p_tags[i].text) +"\n"
		#print(paragraphs)
		#raise NotImplementedError
		if id in p_dict:
			continue
		else:
			p_dict[id] = paragraphs

	print(len(p_dict))
	with open("./Data/MLB/mlb1_paragraphs.csv",'a') as csv_file:
		writer = csv.writer(csv_file)
		for key,value in p_dict.items():
			writer.writerow([key,value])


if __name__ == "__main__":
	main()	
