

def create(cnt):
	infile = "../src/result/" + str(cnt) + ".txt"
	fp = open(infile, 'r')
	title = fp.readline()
	title = title.strip()
	body = fp.read()
	body = body.strip()
	fp.close()

	lines = body.split("|")
	for line in lines:
    		#print(line)
       		temp = line.split(":")
       		key = temp[0]
       		#print(key)
       		if key == "Born":
           		print(temp[1])
       		if key == "Nationality":
        		print(temp[1])
       		if key == "Occupation":
       			print(temp[1])



def main():
	for i in range(1, 11):
		create(i)

if __name__ == "__main__":
	main()