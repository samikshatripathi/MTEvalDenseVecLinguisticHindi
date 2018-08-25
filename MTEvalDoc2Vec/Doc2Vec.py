import gensim
import numpy
import sys
import os
import io
import collections
from Utils.CreateLabels import read_corpus
from Utils.getFiles import All_FileList
def doc2Vec(path):
	'''
		Call this to train sentence vectors on text files present in a directory
		input: Path to the directory
		output: Serialized doc2Vec model
	'''
	filenames = All_FileList(path)
	sentences=[]
	for filename in filenames:
		with open(filename,encoding="utf-8",errors="ignore") as f:
			lines = f.read().splitlines()
			for line in lines:
				sentences.append(line)
	train_data = list(read_corpus(sentences))
	print("Initializing model!!")
	model = gensim.models.doc2vec.Doc2Vec(vector_size=150, min_count=2, workers = 4)
	model.build_vocab(train_data)
	total_epochs = 150
	loss = []
	print("model initialized \nstarting traning!!")
	for epoch in range(total_epochs):
		model.train(train_data, total_examples=model.corpus_count)
		if(epoch%30==0):
			model.save('Models/epochs%d.bin'%int(epoch))
		print("traning epoch: ",epoch)


if __name__=='__main__':
	path =("/home/kwantics/Doc2Vec/CleanText/")
	doc2Vec(path)
