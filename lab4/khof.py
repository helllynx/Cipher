import sys
import os
import operator
import errno
from collections import Counter



def haffman (a):
    if(type(a) == list):
        #result = dict.fromkeys(a.keys(),"")
        keys = [x for (x,y) in a]
        values = [ "" for (x,y) in a]
        result = dict(zip(keys,values))
        #result = [(i," ") for i in a.keys()]

        #a = a.items()
        while len(a)>1:
            a = sorted(a,key=lambda x: x[1],reverse=1)
            temp = [i for i in a[-2:]]
            for j in temp[0][0]:
                result[j] = "0"+ result[j]

            for j in temp[1][0]:
               result[j] = "1"+result[j]

            a = a[:-2]
            temp2 = tuple([x for x in temp[0][0]]+[x for x in temp[1][0]])

            a.append((temp2,temp[0][1]+temp[1][1]))

        return result

def archive(fileName,archivefile,signature):
    listFiles = []
    listDirs = []
    if os.path.isfile(fileName):
        listFiles.append(fileName)
    else:
        list = os.walk(fileName)


        for d, dirs, files in list:
            listDirs.append(d)
            for f in files:
                path = os.path.join( d, f)
                listFiles.append(path)

            for dir in dirs:
                path = os.path.join( d, dir)
                listDirs.append(path)

    symb = []
    tempListFile = listFiles.copy()
    for i in tempListFile:
        k = 0
        for j in open(i, 'r').read():
            symb.append(j)
            k += 1
        listFiles.append((i, k))
        listFiles.remove(i)

    alphabet = sorted(Counter(symb).items(), key=operator.itemgetter(1))

    af = open(archivefile, 'w')

    af.write(signature)

    result = "{"
    for i in alphabet:
        result += str(i[0])+": "+str(i[1])+"|"
    result = result[:-1]+"}"

    af.write(result)


    codehaf = haffman(alphabet)


    result = "{"
    for i in listDirs:
        result += i+"|"

    result+="}{"

    for i in listFiles:
        result += i[0]+"("+str(i[1])+")|"
    result = result[:-1]+"}"

    af.write(result)

    result = ""
    for i in symb:
        result += str(codehaf[i]).strip()

    while len(result)%4 != 0:
        result  +="0"

    stroka = result
    result = ""
    #print(len(stroka))
    while len(stroka) > 3:
        result += format((int(stroka[:4],2)),'x')
        stroka = stroka[4:]

    af.write(result)

def decodeS(string,codes,length):
    codes = dict(zip(codes.values(),codes.keys()))
    result = ""
    k = length
    count = 0
    while k > 0:
        p = 1
        while codes.get(string[:p],-1) == -1:
            p+=1
        result +=codes.get(string[:p])
        string = string[p:]
        k-=1
        count+=p
    return (result,count)

def unarchive(archiveFile,newName,signature):
    file = open(archiveFile,'r').read()

    if file[:4] != signature:
        sys.exit()

    file = file[4:]
    alphabet = []
    temp = file[1:file.find('}{')]
    temp = temp.replace("'","")
    for i in temp.split('|'):
        temp2 = i.split(': ')
        alphabet.append((temp2[0],int(temp2[1])))


    codehaf = haffman(alphabet)
    listFiles = []


    file = file[file.find('}{') + 2:]
    temp = file[:file.find('}')]

    for i in temp.split('|'):
        newDir = os.path.join(newName,i)
        try:
            os.makedirs(newDir)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(newDir):
                pass
            else:
                raise

    file = file[file.find('}') + 2:]
    temp = file[:file.find('}')]
    for i in temp.split('|'):
        k = int(i[i.rfind('(')+1:-1])
        listFiles.append((os.path.join(newName, i[:i.rfind('(')]),k))
    #
    file = file[file.find('}') + 1:]
    #print(file)


    file = file.replace('0','0000')
    file = file.replace('1','0001')
    file = file.replace('2','0010')
    file = file.replace('3','0011')
    file = file.replace('4','0100')
    file = file.replace('5','0101')
    file = file.replace('6','0110')
    file = file.replace('7','0111')
    file = file.replace('8','1000')
    file = file.replace('9','1001')
    file = file.replace('a','1010')
    file = file.replace('b','1011')
    file = file.replace('c','1100')
    file = file.replace('d','1101')
    file = file.replace('e','1110')
    file = file.replace('f','1111')

    for i in listFiles:
        (a,b) = decodeS(file,codehaf,i[1])
        newFile = open(i[0],'w')
        newFile.write(a)
        newFile.close()
        file = file[b+1:]


#
# -u archiveFilePath newDirectoryPath
# -u archiveFilePath
# filePathForArchive or directoryPathForArchive

archiveName = "archive"
newDirName = "archiveDir"
signature = "LoIs"

#archive("1.txt","aa",signature)
#unarchive("3","3.3",signature)


if len(sys.argv) >4 | len(sys.argv) <1:
    print("Not correct count arguments!")
    sys.exit()

# filePathForArchive or directoryPathForArchive
if len(sys.argv) == 2:
    archive(sys.argv[1],archiveName,signature)

# -u archiveFilePath
# filePathForArchive or directoryPathForArchive fileNameArchive
if len(sys.argv) == 3:
    if sys.argv[1] == "-u":
        unarchive(sys.argv[2],newDirName,signature)
    else:
        archive(sys.argv[1],sys.argv[2],signature)


# -u archiveFilePath newDirectoryPath
if len(sys.argv) == 4:
    if sys.argv[1] == "-u":
        unarchive(sys.argv[2],sys.argv[3],signature)
    else:
        sys.exit()