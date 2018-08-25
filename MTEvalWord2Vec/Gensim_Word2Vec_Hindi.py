import os
import argparse
import numpy as np
import io
import re
import datetime
import argparse
from Utils.getFiles import All_FileList




def make_wordvectors(path):
    '''
        Makes Word Vectors
        Input: Tokenized sentences seperated by newline.
        Output: Word2Vec Models
    '''
    import gensim
    import pickle as pickle
    import math
    import csv
    print("Making sentences as list...")
    sents = []
    File_List = All_FileList(path)
    for i,filename in enumerate(File_List):
        print(i,filename)
        with open(filename, 'r',encoding="utf-8") as fin:
            lines = fin.read().splitlines()
            for line in lines:
            	sents.append(line.split())
    print(len(sents),len(sents[1]))
    print("Making word vectors...")
    vecSize = 150
    print(vecSize)
    model = gensim.models.Word2Vec(sents,size=150, window=10, min_count=2, workers=4,iter=1)
    total_epochs = 200  #Change This to vary number of epoches
    loss=[]    
    with open("loss150EntireCorpus.csv","w") as filee:
        writer = csv.writer(filee)
        writer.writerow(['Epochs','Loss','Error','Time'])
        for epoch in range(total_epochs):
            error = "No Error"
            losss=0
            try:
                model.train(sents,total_examples=model.corpus_count,epochs=model.epochs,compute_loss=True)	
                losss = model.get_latest_training_loss()
                print ("loss with",epoch,"epoches, is: ",losss)
                loss.append(losss)
                if epoch%25 == 0:                
                	model.save('Models_Entire_Corpus150/epochs%d.bin'%(epoch))
            except Exception as e:
                error = str(e)
            writer.writerow([epoch,losss,error,str(datetime.datetime.now())])


if __name__=="__main__":
   path = "/home/siddharth/Kwantics/CleanedText/"
   make_wordvectors(path)
