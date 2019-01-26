from text_process import *
from corpus_preprocessing import *
import pickle
from gensim.models import Word2Vec

test = corpus_preprocessing()
temp = open("text_sentence.txt", "r" , encoding='utf-8')
out = open("result.txt", "w", encoding='utf-8')
out_arr = []
for i in temp:
    out_arr += test.token(i)    
for ii in out_arr:
    out.write("|".join(ii) + "\n")
out.close()
model = Word2Vec(out_arr, size = 10, window=5, min_count=1, workers=10)
model.train(out_arr, total_examples=len(out_arr), epochs=50)
# print(len(model['ก๋วยเตี๋ยว']))
# print(model['ก๋วยเตี๋ยว'])
print(model.most_similar(positive = 'ข้าวผัด', topn = 20))
print(model.similar_by_word('ข้าวผัด'))
model.save("word2vec.model")