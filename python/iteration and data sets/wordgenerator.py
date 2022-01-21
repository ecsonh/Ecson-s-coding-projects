# Submitter: ecsonh(Hsu, Ecson)
# Partner  : ricarddr(Reyes, Ricardo)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming
import goody
from goody import irange
import prompt
from random import choice
import re
import random

# For use in read_corpus: leave unchanged in this file
def word_at_a_time(file : open):
    for line in file:
        for item in line.strip().split():
            yield item


def read_corpus(os : int, file : open) -> {(str):[str]}:
                    
    corpus = dict() # defaultdict(list)
    file = word_at_a_time(file)
    key =[next(file) for _i in irange(os)]
    for w in file:
        if tuple(key) not in corpus or w not in corpus[tuple(key)]: # w not in corpus[tuple(key)]:
            corpus.setdefault(tuple(key),list()).append(w)
        key.pop(0)
        key.append(w)
    return corpus


def corpus_as_str(corpus : {(str):[str]}) -> str:
    d = dict(sorted(corpus.items()))
    string = ''
    for k,v in d.items():
        string += '  '+str(k) + ' can be followed by any of ' + str(v) + '\n'
    
    mx = 0
    mn = 10
    for i in corpus.values():
        if len(i)>mx:
            mx =len(i)
        if len(i)<=mn:
            mn = len(i)
    string += 'min/max list lengths = '+ str(mn)+'/'+str(mx)+'\n'
    
    return string


def produce_text(corpus : {(str):[str]}, start : [str], count : int) -> [str]:
    
    list1 = list(start)
    while len(list1) < count + 2:
        options = corpus.get((list1[-2], list1[-1]), None)
        if options is None:
            list1.append(options)
            return list1
        list1.append(random.choice(options))
    return list1

        
if __name__ == '__main__':
    # Write script here
    
    """num = int(input('Input an order statistic: '))
    file = open(input('Input the file name detailing the text to read: '))
    print('Corpus')
    dict1 = read_corpus(num, word_at_a_time(file))
    
    for v in dict1:
        print(" ", v, "can be followed by any of", dict1[v])
    
    print("min/max list lengths =", str(min([len(p) for t, p in dict1.items()])) + "/" + str(max([len(p) for t, p in dict1.items()])))    
    
    print('\nInput',num, 'words at the start of the list')
    list_10 = []
    
    for i in range(1,num+1):
        in_word = input('Input word '+ str(i)+': ')
        list_10.append(in_word)
    num_word = int(input('Input # of words to append to the end of the list: '))
    print('Random text =', produce_text(dict1,list_10, num_word))"""
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()