import nltk
import csv
import re
import stemming

from nltk.corpus import stopwords,wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

def main():

	stop_words = stopwords.words('english') + ['advertisement','support']
	print(stop_words)
	#stop_words.append('said')
	#stop_words.append('would')
	#stop_words.append('s')
	#raise NotImplementedError
	ps  = PorterStemmer()
	wnl = WordNetLemmatizer()
	for value in range(1,101):
		text = ""
		with open("./NHL/NHL_File_" + str(value)+ ".txt",'r') as f:
			print("Running")
			for line in f:
				#print(para)
				#para = ["runner","running","run"]
				line = line.lower()
				line = re.sub(r"[^A-Za-z]+",' ',line)
				word_tokens = word_tokenize(line)
				#word_tokens = ["runner","running","run"]
				filtered_sentence = []
				stemmed_words = ""
				for w in word_tokens:
					if w not in stop_words:
						filtered_sentence.append(w)
				for w in filtered_sentence:
					if w.endswith('e') or w.endswith('s') or w.endswith('y') or w.endswith('l'):
						#stemmed_words.append(w +' : '+wnl.lemmatize(w))
						stemmed_words = stemmed_words + wnl.lemmatize(w) + " "
					else:
						#stemmed_words.append(w+' : '+ps.stem(w))
						stemmed_words = stemmed_words + ps.stem(w) + " "
				text = text + stemmed_words
			#print(text)
			text_file = open("./NHL_STEM/NHL_STEM_" +str(value) +".txt", "w")
			text_file.write(text)
			text_file.close()
			#raise NotImplementedError

if __name__ == "__main__":
	main()