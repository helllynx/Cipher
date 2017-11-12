import glob
from chardet.universaldetector import UniversalDetector

#SHIT CODE, I KNOW


def get_encoding(file):
    detector = UniversalDetector()
    # for filename in glob.glob('/home/gene/MIET/7_semestr/EXP/OTIK/ОТИК/ОТИК лаб/Лаб_3_Кодировки/Тексты/unix-iso8859-5.txt'):
    # for filename in file:
    for line in open(file, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    print("FILE ENCODING - "+detector.result.get('encoding'))
    return detector.result.get('encoding')


def convert_encoding(data, old_coding ,new_coding='UTF-8'):
    if new_coding.upper() != old_coding.upper():
        return data.decode(old_coding).encode(new_coding)



def get_readable_text(file):
    lines = b''
    with open(file, 'rb') as myfile:
        for line in myfile:
            lines+=line
    return convert_encoding(lines, get_encoding(file_path), 'UTF-8').decode('UTF-8')


file_path = '/home/yenq/MIET/LABS/Cipher/lab3/3encode.txt'

with open('output.txt', 'w') as myfile:
    myfile.write(get_readable_text(file_path))