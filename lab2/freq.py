from func import *
import matplotlib.pyplot as plt

#Ex 1,2
####################################################################################
print("EX 1 and 2 ======================================================================================")

ListRus1 = fileToFlatternText('text/LNT_WaP.txt')
ListEng1 = fileToFlatternText('text/Kipling.txt')
ListRus2 = fileToFlatternText('text/HeroOurTime.txt')
ListEng2 = fileToFlatternText('text/Frank.txt')

ex12(ListRus1)
ex12(ListRus2)
ex12(ListEng1)
ex12(ListEng2)



# #Ex 3
####################################################################################

print("EX 3 ======================================================================================")

# RUS
w, c = CounterToLists(ListRus1)
plotHistOfWords(w, c)
w, c = CounterToLists(ListRus2)
plotHistOfWords(w, c)

#E NG
w, c = CounterToLists(ListEng1)
plotHistOfWords(w, c)
w, c = CounterToLists(ListEng2)
plotHistOfWords(w, c)


#Ex 4
####################################################################################

print("EX 4 ======================================================================================")


#Rus
freqOfWords(ListRus1)

#Eng
freqOfWords(ListEng1)


#Ex 5
####################################################################################
print("EX 5 ======================================================================================")

plt.figure()

width = 0.8


w, c = CounterToLists(ListRus1[::1000])
plt.subplot(221)
indexes = numpy.arange(len(w))
plt.bar(indexes, c, width)
plt.xticks(indexes + width, w)

w, c = CounterToLists(ListRus2[::1000])
plt.subplot(222)
indexes = numpy.arange(len(w))
plt.bar(indexes, c, width)
plt.xticks(indexes + width, w)

w, c = CounterToLists(ListRus1)
plt.subplot(223)
indexes = numpy.arange(len(w))
plt.bar(indexes, c, width)
plt.xticks(indexes + width, w)

w, c = CounterToLists(ListRus2)
plt.subplot(224)
indexes = numpy.arange(len(w))
plt.bar(indexes, c, width)
plt.xticks(indexes + width, w)


#Ex 6
####################################################################################

# print("EX 6 ======================================================================================")


ListShift = fileToFlatternText('text/bg-ru.txt')

w, c = CounterToLists(ListShift)

plotHistOfWords(w, c)
ex12(ListShift)


plt.show()

