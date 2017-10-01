from func import *
import matplotlib.pyplot as plt

#Ex 1,2
####################################################################################

ListRus1 = fileToFlatternText('text/LNT_WaP.txt')
ListEng1 = fileToFlatternText('text/Kipling.txt')
ListRus2 = fileToFlatternText('text/HeroOurTime.txt')
ListEng2 = fileToFlatternText('text/Frank.txt')

ex12(ListRus1)
ex12(ListRus2)
ex12(ListEng1)
ex12(ListEng2)

print("======================================================================================")

# #Ex 3
####################################################################################
#
#RUS
w, c = CounterToLists(ListRus1)
plotHistOfWords(w, c)
w, c = CounterToLists(ListRus2)
plotHistOfWords(w, c)

#ENG
w, c = CounterToLists(ListEng1)
plotHistOfWords(w, c)
w, c = CounterToLists(ListEng2)
plotHistOfWords(w, c)


print("======================================================================================")

#Ex 4
####################################################################################
#Rus
freqOfWords(ListRus1)

#Eng
freqOfWords(ListEng1)

print("======================================================================================")

#Ex 6
####################################################################################



ListShift = fileToFlatternText('text/bg-ru.txt')

w, c = CounterToLists(ListShift)

plotHistOfWords(w, c)
ex12(ListShift)


plt.show()

