import csv
import re

def main():
	tweets = {}
	count = 1
	#s = "hello \n hi"
	#s = s.replace("\n","\t")
	#print(s)
	with open("./tweets/NCAA.csv") as csv_file:
		csv_reader = csv.reader(csv_file)
		print("Running")
		for row in csv_reader:
			#print(row)
			tweet = row[0]
			tweet = tweet.replace("\n","\t")
			tweet = re.sub(r'https\S+', '', tweet)
			count = count + 1
			print(tweet)
			#if(count > 10):
			#	raise NotImplementedError
			#raise NotImplementedError
			tweets[count] = tweet
			count = count + 1
		#print(len(tweets))
	
	with open("./formatted_tweets/ncaa.csv",'a') as csv_file:
		writer = csv.writer(csv_file)
		for key,value in tweets.items():
			writer.writerow([key,value])
	

if __name__ == "__main__":
	main()	