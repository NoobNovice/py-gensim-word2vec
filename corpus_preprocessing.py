import pythainlp as ptn
import re
import pickle

class corpus_preprocessing:
    __new_vocab = [["รี","วิว","รีวิว"],["แป","ป","แปป"],["ออ","เด","อร์","ออเดอร์"]]
    def __init__(self):
        # vocab_file = open("vocab.txt", "rb", encoding='utf-8')
        # self.__new_vocab = pickle.load(vocab_file)
        return
    
    def token(self, sentence):
        temp = self.__sentence_filter(sentence)
        token_arr = ptn.word_tokenize(temp, engine='newmm')
        for i in self.__new_vocab:
            if(i[0] in token_arr and i[len(i) - 2] in token_arr):
                index = token_arr.index(i[0])
                token_arr[index] = i[len(i) - 1]
                del token_arr[index + 1:index + (len(i) - 1)]
        while("ss" in token_arr):
                    del token_arr[token_arr.index("ss")]
        while("ๆ" in token_arr):
                    del token_arr[token_arr.index("ๆ")]
        result = self.__sentence_segmentation(token_arr, 20)
        return result

    def __sentence_segmentation(self, token_arr, vocab_range):
        result = []
        space_index = None
        point = 0
        while(True):
            if point >= len(token_arr) - 1:
                while(" " in token_arr):
                    del token_arr[token_arr.index(" ")]
                result.append(token_arr)
                break
            elif point >= vocab_range - 1:
                temp = None
                if space_index != None:
                    temp = token_arr[0:space_index]
                    del token_arr[0:space_index + 1]
                else:
                    temp = token_arr[0:point + 1]
                    del token_arr[0:point + 1]
                while(" " in temp):
                    del temp[temp.index(" ")]
                result.append(temp)
                space_index = None
                point = 0
            elif token_arr[point] == " ":
                space_index = point
            point += 1
        return result

    def __sentence_filter(self, sentence):
        edit_sentence = re.sub(r'[.][-]|[฿]', r' บาท' , sentence)
        edit_sentence = re.sub(r'[-][/t][^0-9]', r'', edit_sentence)
        edit_sentence = re.sub(r'TOT|tot|ToT|WOW|wow|WoW|55+5|๕๕+๕', r'', edit_sentence) # text emotion
        edit_sentence = re.sub(r'[-]', r'ss', edit_sentence)
        edit_sentence = re.sub(r'[0-9?][.]|[0-9?][)]', r'', edit_sentence)
        edit_sentence = re.sub(r'[^A-Za-z0-9ก-๙]', r' ', edit_sentence)
        return edit_sentence