from Utils.getFiles import All_FileList

eng_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
newdoc = ""
with open('questions.txt', 'r',encoding="utf-8") as fin:
	lines = fin.read().splitlines()
	for line in lines:
		hasEng = False
		for character in eng_char:
			if character in line:
				hasEng = True
				break
		if hasEng:
			continue
		else:
			newdoc +=line+'\n'

with open('cleanQuestions.txt','w',encoding='utf-8',errors = 'ignore') as f:
	f.write(newdoc)
