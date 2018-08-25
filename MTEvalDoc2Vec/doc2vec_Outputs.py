import gensim
import os
import collections
import smart_open


fullpath=os.path.abspath("home/kwantics/Doc2Vec/Input")


def fileread(fileIp):

	fpath = os.path.abspath(fileIp)
	final_list=[]
	with open(fpath,'r',encoding="utf-8", errors="ignore") as fi : 
		dataReadFile=fi.read()   
		dataL=dataReadFile.splitlines()
		for i in range(len(dataL)):
			Alltokens=dataL[i].split()
			final_list.append(Alltokens)
		return (final_list)

       

def All_filesList(CommonPath):
	AllFolderList=os.listdir(CommonPath)
	AllFolderList=[CommonPath +i for i in AllFolderList]
	AllFolderList.sort()
	return AllFolderList

#AlltokensinList(AllfilePath)         

if __name__=='__main__':

	filename = "/home/kwantics/Doc2Vec/Models/epochs100.bin"
	model = gensim.models.doc2vec.Doc2Vec.load(filename)
	model.random.seed(0)
	AllfilepathH=All_filesList("/home/kwantics/Doc2Vec/Practice/SimilarityMeasure/H/")
	print(AllfilepathH)
	AllfilepathG=All_filesList("/home/kwantics/Doc2Vec/Practice/SimilarityMeasure/G/")
	print(AllfilepathG)
	totalTextFiles = len(AllfilepathH)
	print("##", totalTextFiles)
	
	for i in range(totalTextFiles):
		humanTokens=fileread(AllfilepathH[i])
		googleTokens=fileread(AllfilepathG[i])
		simVec = []
		totalSent = len(humanTokens)
		print("$$$", totalSent)
		for j in range(totalSent):
			model.random.seed(0)
			vecH = model.infer_vector(humanTokens[j])
			model.random.seed(0)
			vecG = model.infer_vector(googleTokens[j])
			vecHH = gensim.matutils.dense2vec(vecH)
			vecGG = gensim.matutils.dense2vec(vecG)
			sim = gensim.matutils.cossim(vecHH, vecGG)
			simVec.append(sim)
		
			with open("output.txt", 'a', encoding='utf-8', errors='ignore') as fw:
				fw.write("######### Statement ##########" + "\n")
				fw.write("HToken List: " + str(humanTokens[j]) + "\n")
				fw.write("GToken List: " + str(googleTokens[j]) + "\n")
				fw.write("Similarity Measure: " + str(sim) + "\n")
				
		with open("output.txt", 'a', encoding='utf-8', errors='ignore') as fw:
			fw.write("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" + "\n")		
			fw.write("Text Similarity: " + str(sum(simVec)/len(simVec)) + "\n")
			fw.write("@@@@@@@@@@@ Statement Ends @@@@@@@@@@@@@@@" + "\n\n")
			
	




