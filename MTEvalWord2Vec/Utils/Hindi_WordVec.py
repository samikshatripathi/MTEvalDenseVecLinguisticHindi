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
    global vocab_size
    print("Making sentences as list...")
    sents = []
    sentence=""
    File_List = All_FileList(path)
    for filename in File_List:
        print(filename)
        with open(filename, 'r',encoding="utf-8") as fin:
            lines = fin.read().splitlines()
            for line in lines:
            	sents.append(line.split())
    print(len(sents),len(sents[1]))
    print("Making word vectors...")
    loss = []
    model = gensim.models.Word2Vec(sents,size=150, window=10, min_count=2, workers=4,iter=1)
    total_epochs = 1000  #Change This to vary number of epoches    
    with open("loss.csv","w") as file:
        writer = csv.writer(file)
        for epoch in range(total_epochs):
            model.train(sents, total_examples=model.corpus_count, epochs=model.epochs, compute_loss=True)
            error = model.get_latest_training_loss() 
            writer.writerow([epoch,error])
            print ("loss with",epoch,"epoches, is: ",error)
            loss.append(error)
            if epoch%25 == 0:                 #Change this to control number of saved states
                model.save('Models/epochs%d.bin'%epoch)
