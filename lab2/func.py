from collections import Counter
import numpy
import matplotlib.pyplot as plt
import operator

flatten = lambda l: [item for sublist in l for item in sublist]

def freqOfWords(wordlist):
    counter = (Counter(flatten(wordlist)))
    WordSum = sum(counter.values())

    print(WordSum)

    Counts = list(counter.values())
    Words = list(counter.keys())


    for i in range(0, len(Counts)):
        print(str(Words[i]) + " " + str(Counts[i] / WordSum))

    
def ex12(wordlist):
    most_comm4 = (Counter(wordlist)).most_common(4)
    print("\nMost common word in text ")
    print(most_comm4)
    print("Text len " + str(len(wordlist)))
    print("Space / (most comm word) = " + str(most_comm4[0][1] / most_comm4[1][1]))
    print("First most common / Second most common = " + str(most_comm4[1][1] / most_comm4[2][1]))
    print("First most common / Second most common = " + str(most_comm4[2][1] / most_comm4[3][1]) + "\n")



def SortedFreq(wordlist):
    list = sorted((Counter(wordlist)).items(), key=lambda pair: pair[1], reverse=True)
    return list


def fileToFlatternText(file):
    with open(file) as f:
        TextList = [list(line.rstrip()) for line in f]
    return flatten(TextList)


def plotHistOfWords(w, c):
    words = w
    word_counts = c
    indexes = numpy.arange(len(words))
    width = 0.8
    plt.figure()
    plt.bar(indexes, word_counts, width)
    plt.xticks(indexes + width, words)



def CounterToLists(counter):
    words = []
    counts = []
    for i in SortedFreq(counter):
        words.append(i[0])
        counts.append(i[1])
    return [words,counts]