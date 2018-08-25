from gensim.models import word2vec
from gensim.models import KeyedVectors
model = KeyedVectors.load('Models_Entire_Corpus150/epochs175.bin')
model.wv.save_word2vec_format('word2Vec.txt', binary=False)
