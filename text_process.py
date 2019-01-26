import pythainlp as ptn
import re

class text_process:
    __text_in = None
    __text_out = None
    def __init__(self, name_text_in, name_text_out):
        self.__text_in = open(name_text_in, "r", encoding='utf-8')
        self.__text_out = open(name_text_out, "w", encoding='utf-8')
        self.__new_vocab = open(name_text_in, "r", encoding='utf-8')
        self.__text_filter()
        self.__text_in.close()
        return
    
    def __text_filter(self):
        for i in self.__text_in:
            print("b_text{}".format(i))
            e_text = re.sub(r'[.][-]|[฿]', r' บาท' , i)
            e_text = re.sub(r'[-][/t][^0-9]', r'', e_text)
            e_text = re.sub(r'TOT|tot|ToT|WOW|wow|WoW|55+5|๕๕+๕', r'', e_text) # text emotion
            e_text = re.sub(r'[-]', r'ss', e_text)
            e_text = re.sub(r'[/d{1}?][.]|[/d{1}?][)]|', r' ', e_text)
            e_text = re.sub(r'[^A-Za-z0-9ก-๙]', r' ', e_text)
            print("e_text{}".format(e_text))
            self.__text_out.write(e_text+"\n")
        self.__text_out.close()
        return