import math
import string

def processSeq(seq,tr,strt,ind):
    for i in range(len(seq)):
        if i==0:
            strt[ind[seq[i]]] += 1
        else:
            tr[ind[seq[i-1]]][ind[seq[i]]] += 1

dictionary = []
f = open("nursery_rhymes.txt", "r")
count = 0
for line in f:
    for word in line.split():
        word = word.translate(None, string.punctuation)
        word = word.lower()
        if word in dictionary:
            continue
        else:
            dictionary.append(word)
            count += 1
        #add word to dictionary

#variables
list_matrix = [0] * count
start_counts = [0] *  count
counts = [[list_matrix],[list_matrix]]
indexs = {i:{j:{k:dictionary[i]}}
for i in range(0, count)
    for j in range(0, count)
        for k in range(0, count)
 }

current_word = ""

processSeq(current_word, counts, start_counts,indexs)
sum_row = sum(start_counts)
start_probs = [e/sum_row for e in start_counts]
tr_probs = []
for l in tr_counts:
    sum_row = sum(l)
    prob_vector = [j/sum_row for j in l]
    tr_probs.append(prob_vector)
#now calculate the test probability
