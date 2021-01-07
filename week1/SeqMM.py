import math

#method were we process the entire sequence

def processSeq(seq,tr,strt,ind):
    for i in range(len(seq)):
        if i==0:
            strt[ind[seq[i]]] += 1
        else:
            tr[ind[seq[i-1]]][ind[seq[i]]] += 1

#declare the count variables to calculate the markov probabilities

counts= [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
start_counts = [0,0,0,0]
index = {'a':0,'c':1,'t':2,'g':3}


f = open("sequences.txt","r")

current_seq = ""
#Train model based on the sequences

for line in f:
    if line.startswith(">") or line.startswith("Random"):
        continue
    elif line.startswith("\n") or line.strip()=="":
        processSeq(current_seq, counts, start_counts,index)
        current_seq = ""
    else:
        current_seq += line.strip()
processSeq(current_seq, counts, start_counts,index)

#Markovs probabilties

sum_row = sum(start_counts)
start_probability = [e/sum_row for e in start_counts]
tr_probs = []
for l in counts:
    sum_row = sum(l)
    prob_vector = [j/sum_row for j in l]
    tr_probs.append(prob_vector)

#Read the test and calculate the probabilities from the matrixes

f = open("test.txt","r")
test_seq = ""
line_count = 0
for line in f:
    line_count += 1
    if line_count > 2:
        test_seq += line.strip()
log_prob = 0
for i in range(len(test_seq)):
    if i==0:
        log_prob += math.log(start_probability[index[test_seq[i]]])
    else:
        log_prob += math.log(tr_probs[index[test_seq[i-1]]][index[test_seq[i]]])
print("Probability for first order MM: " + str(log_prob) ,"\n")
print("Where " + str(log_prob), "is the computed probabilities.\n")
