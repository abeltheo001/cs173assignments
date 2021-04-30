exit
import re
import nltk
from nltk.corpus import words
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from collections import Counter
from bisect import bisect_left
dictionary = words.words()
lemmatizer = PorterStemmer()

def list_of_words(text): return re.findall(r'\w+',text.lower())

WORDS = Counter(list_of_words(open('words.txt').read()))

def part1():
    base_list=[]
    new_list=[]
    final_list=[]
    with open('mobydick.txt','r') as reader:
        moby_dick = reader.read()
    pre_tokens = word_tokenize(moby_dick)
    tokens = (w.lower() for w in pre_tokens if w.isalpha())

    for t in tokens:
        if lemmatizer.stem(t) in dictionary or t in dictionary:
            pass
        else:
            base_list.append(t)

    for word in base_list:
        if word[-1:] == 'd':
            word_without_d = word[:-1]
            if word_without_d in dictionary:
                pass
            else:
                if word[-2:] == 'ed':
                    word_without_ed = word[:-2]
                    if word_without_ed in dictionary:
                        pass
                    else:
                        if word[-3:] == 'ied':
                            word_without_ied = word[:-3]
                            word_without_ied_y = word_without_ied + 'y'
                            if word_without_ied_y in dictionary:
                                pass
                            else:
                                new_list.append(word)
                        else: 
                            new_list.append(word)
                else:
                    new_list.append(word)

        elif word[-1:] == 's':
            word_without_s = word[:-1]
            if word_without_s in dictionary:
                pass
            else:
                if word[-2:] == 'es':
                    word_without_es = word[:-2]
                    if word_without_es in dictionary:
                        pass
                    else:
                        if word[-3:] == 'ies':
                            word_without_ies = word[:-3]
                            word_without_ies_y = word_without_ies + 'y'
                            if word_without_ies_y in dictionary:
                                pass
                            else:
                                new_list.append(word)
                        else:
                            new_list.append(word)
                else:
                    new_list.append(word)
        else:
            new_list.append(word)
                    
    new_list.sort()
            
    for w in new_list:
        if w not in final_list:
            final_list.append(w)
    return final_list

def part2(misspelled_words):
    def candidates(word):
        if word in WORDS:
            return word
        return known(edits(word))

    def known(known_words):
        known_list = set(w for w in known_words if w in WORDS)
        isEmpty = (known_list == set())
        if not isEmpty:
            return known_list
       
    def edits(word):
        letters     = 'abcdefghijklmnopqrstuvwxyz'
        splits      = [(word[:i], word[i:])         for i in range(len(word) + 1)]
        deletes     = [L + R[1:]                    for L, R in splits if R]
        transposes  = [L + R[1] + R[0] + R[2:]      for L, R in splits if len(R) > 1]
        replaces    = [L + c + R[1:]                for L, R in splits if R for c in letters]
        inserts     = [L + c + R                    for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)
    
    for word in misspelled_words:
        print(word, candidates(word))


def main(): 
    #part 1: take in mobydick.txt and find misspelled words
    x = part1()
    #part 2: take misspelled words and find correct alts
    part2(x)

if __name__ == "__main__":
    main()
