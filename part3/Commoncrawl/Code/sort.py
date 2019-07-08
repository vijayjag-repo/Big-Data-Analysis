import csv
from operator import itemgetter

def main():

	text_file = open("./co-output/co-stncaaop/part-00000", "r")
	f = []
	for line in text_file:
		s,n = line.split()
		if(s!="v"):
			f.append([s,int(n)])
	f = sorted(f,key=itemgetter(1),reverse=True)
	final = f[0:30]
	#raise NotImplementedError
	with open("./co-output/co-stncaaop/ncaa.csv",'w') as csv_file:
		writer = csv.writer(csv_file)
		for item in final:
			writer.writerow([item[0],item[1]])

if __name__ == "__main__":
	main()	