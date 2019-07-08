import nltk
import csv
import re
import stemming

from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize 

def main():

	stop_words = set(stopwords.words('english'))
	new_stop_words = ['said','would','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z','ve']
	#print(stop_words)
	#stop_words.add('said')
	for word in new_stop_words:
		stop_words.add(word)
	print(stop_words)
	#raise NotImplementedError
	#ps  = PorterStemmer()
	wnl = WordNetLemmatizer()
	text = ""
	with open("./new_data/ncaa/s_ncaa_paragraphs.csv") as csv_file:
		csv_reader = csv.reader(csv_file)
		print("Running")
		for row in csv_reader:
			para = row[1]
			print(para)
			#para = ["runner","running","run"]
			para = para.lower()
			para = re.sub(r"[^A-Za-z]+",' ',para) 
			word_tokens = word_tokenize(para)
			#word_tokens = ["runner","running","run"]
			filtered_sentence = []
			stemmed_words = ""
			for w in word_tokens:
				if w not in stop_words:
					filtered_sentence.append(w)
			for w in filtered_sentence:
				stemmed_words = stemmed_words + wnl.lemmatize(w) + " "
			#print(stemmed_words)
			#text_file = open("./Stemmed_Output/nba1.txt", "w")
			#text_file.write(stemmed_words)
			#text_file.close()
			#print(wnl.lemmatize("is"))
			text = text + stemmed_words + "\n" +"\n"
		#print(text)
		text_file = open("./Stemmed_Output/scc/s_ncaa_paragraphs.txt", "w")
		text_file.write(text)
		text_file.close()
		#raise NotImplementedError

if __name__ == "__main__":
	main()	