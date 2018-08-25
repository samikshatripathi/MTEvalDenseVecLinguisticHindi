#import gensim
#model = gensim.models.Word2Vec.load('Models_With_Wiki150/epochs125.bin')

import json
#countdict={}
#total_sum = 0

#for word in model.wv.vocab.keys():
#	countdict[word] = model.wv.vocab[word].count
#	total_sum += countdict[word]
#jsonn = json.dumps(countdict)
#f = open("frqDict.json","w")
#f.write(jsonn)
#f.close()
with open("frqDict.json","r",encoding="utf-8") as f:
	#lines = f.read()
	countdict = json.load(f)
print(countdict['आँखें'],': आँखें')
#print(countdict['आँख'],': आँख')
#print(countdict['रात'],': रात')
#print(countdict['रातें'],': रातें')
